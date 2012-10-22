from django import forms

class buscarRutasForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'class':'span2', \
                                                            'placeholder':'Ingresa la consulta', \
                                                            'id':'appendedInputButton', \
                                                            'size':'16'}))
    def clean(self):
        return self.cleaned_data
