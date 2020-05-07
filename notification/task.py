from sec import celery_app
from notifications.signals import notify
from team_member.models import TeamMember


@celery_app.task(name='send_notification')
def send_notification(user_id, recipients_id, verb):
    user = TeamMember.objects.get(user_id=user_id).user
    recipient = [TeamMember.objects.get(user_id=recipients_id).user]
    notify.send(user, recipient=recipient, verb=verb)
