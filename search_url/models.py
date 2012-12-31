from django.db import models
import base64
# Create your models here.

class synology_conf (models.Model):
	ip_diskstation = models.CharField(max_length=50 ,verbose_name=u'IP Diskstation')
	port = models.IntegerField(default=5000, verbose_name=u'Puerto')
	usuario = models.CharField(max_length=50, verbose_name=u'Usuario')
	password = models.CharField(max_length=50,verbose_name=u'password')

	def __unicode__(self):
		return self.usuario

	def save(self, *args, **kwargs):
		if self.password:
			self.password = base64.b64encode(self.password)
		super(synology_conf, self).save(*args, **kwargs)

		

