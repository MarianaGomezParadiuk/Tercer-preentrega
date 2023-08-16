from django.db import models

class Lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido} - {self.id}"
    
class Bibliotecario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}, {self.apellido} - {self.id}"
    
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
class Pedido(models.Model):
    titulo = models.CharField(max_length=50)
    id_lector = models.IntegerField()

    def __str__(self):
        return f"{self.titulo}"