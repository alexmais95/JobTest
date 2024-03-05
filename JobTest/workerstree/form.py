from django.forms import ModelForm
from workerstree.models import *


class AddWorker(ModelForm):
    class Meta:
        model = Workers
        fields = '__all__'
