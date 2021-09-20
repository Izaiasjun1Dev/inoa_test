from celery import shared_task
from django.core.mail import send_mail 
from apps.cotacoes.models import Cotacao, Wallet



@shared_task
def emails_task():
    pass