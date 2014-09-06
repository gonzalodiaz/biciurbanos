from django.db import models


class Marcador(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MarcadoDeUnUsuario(Marcador):
    #usuario = models.ForeignKey("auth.User", related_name="marcadores")

    class Meta:
        abstract = True


class Bache(MarcadoDeUnUsuario):
    tipo_marcador = models.CharField(max_length="50", default="bache")


