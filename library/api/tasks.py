# Create your tasks here
from library.celery import app
from django.core.mail import send_mass_mail
from django.conf import settings
from api.models import Subscriber, Book

@app.task
def send_mail_to_subs(new_book_id):
    book = Book.objects.get(id=new_book_id)
    subject = 'Oповещение'
    msg = (
        '{sub}, Добрый день!\n'
        'На нашем портале доступна новая книга {book.name} от автора {book.author}!\n\n'
    )
    from_email=settings.DEFAULT_FROM_EMAIL,
    messages = [
        (subject, msg.format(sub=sub, book=book), from_email[0], (sub.email, ))
        for sub in Subscriber.objects.all()
    ]

    return send_mass_mail(messages)

