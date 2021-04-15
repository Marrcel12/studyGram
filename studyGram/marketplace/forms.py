from django import forms
from .models import level, subject, topic
class SearchForm(forms.Form):
    search = forms.CharField(label='Twoje wyszukanie', max_length=30,required=False)
class FilterForm(forms.Form):
    choice_levels = forms.ModelChoiceField(queryset=level.objects.all(),to_field_name="id_level",empty_label=None,required=False)
    choice_subjects = forms.ModelChoiceField(queryset=subject.objects.all(), empty_label=None,required=False)
    choice_topics = forms.ModelChoiceField(queryset=topic.objects.all(), empty_label=None,required=False)