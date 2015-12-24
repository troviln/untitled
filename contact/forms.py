__author__ = 'trigger'

from django import forms

class ContactForm(forms.Form):
    subject = forms. CharField(max_length=20, label='Them')
    email = forms.EmailField(required=False)
    message = forms. CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("To few words")
        return message
