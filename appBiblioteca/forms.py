from django import forms

class PedidoForm(forms.Form):
    titulo = forms.CharField(max_length=50, required=True)
    id_lector = forms.IntegerField(required=True)

class LectorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    direccion = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    telefono = forms.IntegerField()
    
class BibliotecarioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    contacto = forms.CharField(max_length=50, required=True)
    
class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=50, required=True)
    tipo = forms.CharField(max_length=50, required=True)
    autor = forms.CharField(max_length=50, required=True)
    editorial = forms.CharField(max_length=50, required=True)
    cantidad = forms.IntegerField(required=True)