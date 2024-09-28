from django.db import models

# Definimos el modelo Doctor
class Doctor(models.Model):
    # Campo de texto para el primer nombre del doctor, con un máximo de 100 caracteres
    first_name = models.CharField(max_length=100)
    
    # Campo de texto para el apellido del doctor, con un máximo de 100 caracteres
    last_name = models.CharField(max_length=100)
    
    # Campo de tipo fecha para almacenar la fecha de nacimiento del doctor
    birth_date = models.DateField()
    
    # Campo de texto para almacenar la dirección del doctor, con un máximo de 255 caracteres
    address = models.CharField(max_length=255)
    
    # Campo booleano que indica si el doctor está activo o no (True por defecto)
    is_active = models.BooleanField(default=True)

    # Clase Meta, usada para configurar opciones adicionales del modelo
    class Meta:
        # Nombre singular que aparecerá en la interfaz administrativa
        verbose_name = 'Doctor'
        
        # Nombre plural que aparecerá en la interfaz administrativa
        verbose_name_plural = 'Doctors'
        
        # Orden por defecto: primero por apellido, luego por nombre
        ordering = ['last_name', 'first_name']  

    # Método __str__ para la representación en cadena del objeto
    def __str__(self):
        # Retorna una cadena con el nombre completo del doctor (nombre + apellido)
        return f'{self.first_name} {self.last_name}'



