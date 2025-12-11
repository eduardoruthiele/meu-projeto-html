from django import forms
from .models import ItemRanking

class ItemRankingForm(forms.ModelForm):
    class Meta:
        model = ItemRanking
        fields = ["nome", "icone"]
