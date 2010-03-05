from django import forms

class LineItemForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput())
    user = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
	if self._errors:
	    return
