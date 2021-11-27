import json

from datetime import datetime
from django.db import models
# from requests import request
from user.models import UserProfile


class HealthCondition(models.Model):

    HEALTH_STATES = [
        ('YES', 'Bem'),
        ('NO', 'Não muito bem')
    ]

    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Usuário')
    health_state = models.CharField(max_length=13, choices=HEALTH_STATES, verbose_name='Estado de Saúde')
    prognostic = models.CharField(max_length=2000, verbose_name='Prognósticos', null=True, blank=True)
    create_at = models.DateTimeField(verbose_name="Data de Criação", default=datetime.now())

    class Meta:
        verbose_name = 'Condição de Saúde'
        verbose_name_plural = 'Condições de Saúde'

    def __str__(self):
        return self.user_id.name

    def set_prognostic(self, x):
        self.prognostic = json.dumps(x)

    def get_prognostic(self):
        return json.loads(self.prognostic)
