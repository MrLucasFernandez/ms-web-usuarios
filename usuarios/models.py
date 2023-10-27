from django.db import models

# Create your models here.
class Roles(models.Model):
    id_rol      = models.BigAutoField(db_column="id_rol",primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return str(self.descripcion)

class Usuarios(models.Model):
    id_usuario  = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=30)
    rut         = models.CharField(max_length=9)
    email       = models.CharField(max_length=35)
    direccion   = models.CharField(max_length=50)
    username    = models.CharField(max_length=25, default='DEFAULT VALUE')
    password    = models.CharField(max_length=25, default='DEFAULT VALUE')
    rol         = models.ForeignKey(Roles, related_name='rol_usuario', blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return "ID: "+str(self.id_usuario)+" "+str(self.username)+' '+str(self.email)

