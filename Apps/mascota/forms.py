from django import forms
from Apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        #creamos tuplas
        fields = [
            'folio',
            'nombre',
            'edad_aproximada',
            'sexo',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels = {
            'folio': 'identidicacion',
            'nombre': 'Nombre',
            'edad_aproximada': 'Edad Aproximada',
            'sexo': 'Genero',
            'fecha_rescate': 'Fecha de Rescate',
            'persona': 'Adoptante',
            'vacuna': 'Tipo de Vacuna',
        }
        #Etiquetas html
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }