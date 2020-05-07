from django.core.mail import send_mail

from sec import celery_app


@celery_app.task(name='send_out_email')
def send_notification_email(subject, message, from_email, recipient_list, fail_silently):
    print('sending')
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        recipient_list=[recipient_list],
        fail_silently=False,
    )
