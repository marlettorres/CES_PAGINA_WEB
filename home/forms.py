from django import forms


class UploadFileForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    archivo_vista = forms.FileField()
    texto = forms.CharField(max_length=1000, required=False)
    pdf = forms.FileField(required=False)
    imagen = forms.FileField(required=False)
    pagina_cecyte_id = forms.IntegerField()
    tipo_bloque = forms.IntegerField()