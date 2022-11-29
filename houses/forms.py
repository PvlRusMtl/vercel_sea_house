from django import forms

class HousesFilterForm(forms.Form):
    min_price = forms.IntegerField(label='from', required=False)
    max_price = forms.IntegerField(label='to', required=False)
    query = forms.CharField(label='description', required=False)
    ordering = forms.ChoiceField(label='sort', required=False, choices=[
        ('name', 'by alphabet'),
        ('price', 'cheap first'),
        ('-price', 'expensive first')
    ])