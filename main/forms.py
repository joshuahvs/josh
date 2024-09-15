from django.forms import ModelForm
from main.models import joshItem

class joshShopEntryForm(ModelForm):
    class Meta:
        model = joshItem
        fields = ['name', 'price', 'description', 'quantity']