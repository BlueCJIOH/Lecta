from datetime import datetime

from django.contrib.auth import user_logged_in
from django.contrib.sessions.models import Session
from django.utils import timezone

from user_session.models import UserSession


def user_logged_in_handler(sender, request, user, **kwargs):
    if Session.objects.get(pk=request.session.session_key).expire_date > timezone.now():
        UserSession.objects.get_or_create(
            user=user, session_id=request.session.session_key
        )


user_logged_in.connect(user_logged_in_handler)
