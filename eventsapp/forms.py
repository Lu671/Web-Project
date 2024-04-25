from django import forms

class EventForm(forms.Form):
    title = forms.CharField(label='Event Name', max_length=100, required=True)
    date = forms.DateField(label='Event Date', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    description = forms.CharField(label='Event Description', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=True)
    location = forms.CharField(label='Event Location', max_length=100, required=True)