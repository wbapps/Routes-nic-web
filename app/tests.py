from django import forms

class buscarRutasForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput())
    def clean(self):
        return self.cleaned_data
