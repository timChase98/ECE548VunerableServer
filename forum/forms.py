from django import forms

class NewThreadForm(forms.Form):
	title = forms.CharField(label='Title', max_length=140)
	user = forms.CharField(label="UserName", max_length=16)
