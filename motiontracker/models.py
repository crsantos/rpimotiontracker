from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from motiontracker import settings

class MotionTracked(models.Model):
	name 			= models.CharField(max_length=30)
	capture 		= models.FileField("Captured", upload_to=settings.CAPTURES_FOLDER+"/", blank=True, null=True)
	created 		= models.DateTimeField(auto_now_add=True)
	last_modified	= models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s - %s" % (self.name, self.created)

	def image_img(self):
		if self.capture:
			print settings.MEDIA_URL
			path=self.capture.url
			return u'<a href="%s"><img src="%s" width="100" heigh="75"/></a>' % (path,path)
		else:
			return '(No image)'
	image_img.short_description = 'Thumb'
	image_img.allow_tags = True

@receiver(pre_delete, sender=MotionTracked)
def delete_old_media(sender, **kwargs):
	obj = kwargs['instance']
	print 'the object '+str(obj)+'is going to be deleted !'
	storage, path = obj.capture.storage, obj.capture.path
	print str(storage)+" "+str(path)
	storage.delete(path)
