from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Czego dzisiaj się uczysz?'}))