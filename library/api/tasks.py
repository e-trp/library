# Create your tasks here

from library.celery import app

@app.task
def send_mail_to_subs(mailing_list):
    return 

