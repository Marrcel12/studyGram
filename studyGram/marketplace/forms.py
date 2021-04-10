from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Twoje wyszukanie', max_length=30)