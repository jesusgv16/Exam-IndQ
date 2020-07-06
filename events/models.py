from django.db import models

# Create your models here.
class Event(models.Model):
    title 		  = models.CharField('Titulo', max_length=120)
    description   = models.TextField('Descripcion', max_length=200)
    date 	      = models.DateField('Fecha', auto_now=False)
    imagen 		  = models.ImageField(upload_to='images')
    attendances   = models.IntegerField('Asistencias', blank=True, default=1 )
    WillYouAttend =	models.CharField(max_length=1,choices=[('1','Si'),('0','No')])
    longitud 	  = models.CharField('longitud', max_length=120)
    latitud		  = models.CharField('latitud', max_length=120)

    class Meta:
    	verbose_name="event"
    	verbose_name_plural="events"
        
    def __str__(self):
        return self.title