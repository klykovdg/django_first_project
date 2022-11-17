from django.http import HttpResponseRedirect
from django.shortcuts import render
from books.models import Book
from mysite.forms import ContactForm


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'error': error})


def contact(request):
    def send_mail(subject, message, email, list_mails):
        mail = f'\nSubject: %s\nReview: %s\nE-mail: %s\n' % (subject, message, email)
        return mail + 'Review was sent to ' + str(list_mails)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            review = send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com']
            )
            with open('log_file.txt', 'a') as log:
                log.write(review)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': "The best site I've ever seen!"})
    return render(request, 'contact_form.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')
