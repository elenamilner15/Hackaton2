from django import forms
from .models import verbs


# class NameForm(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)
    
# class TranslationForm(forms.Form):
#     meaning = forms.ModelChoiceField(queryset=verbs.objects.all(), empty_label=None, widget=forms.RadioSelect)
#     translation = forms.CharField(label='Translation', max_length=100)
    
# class dic(forms.Form):
#     meaning = forms.ModelChoiceField(label = "meaning", queryset=verbs.objects.all(), empty_label=None, widget=forms.RadioSelect)
#     niqqud_stripped_word = forms.CharField(label='translation', max_length=100)