from django.db import models
from django.utils.translation import gettext as _
from users.models import User


#********************************************************* tabla de reservas ****************************************************


class Reservas(models.Model):
    id_Reservas = models.AutoField(primary_key=True)
    #id_Cliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Id Cliente"))
    cantidad_Personas = models.IntegerField(verbose_name=_("Cantidad Personas"),default=0)
    ubicacion_Mesa = models.CharField(verbose_name=_("Ubicacion Mesa"), choices=[("Cualquiera","Cualquiera"),("I1","I1"),("I2","I2"),("I3","I3"),("I4","I4"),("D1","D1"),("D2","D2"),("D3","D3"),("D4","D4"),("C1","C1"),("C2","C2"),("C3","C3")],default='Cualquiera')
    estado_Reserva = models.CharField(verbose_name=("Estado"),choices=[('Pendiente', 'Pendiente'), ('Confirmado', 'Confirmado'), ('Denegado', 'Denegado')], default='Pendiente')
    fecha = models.DateField(verbose_name=_("fecha"),null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    