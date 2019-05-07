from django.db import models

# Create your models here.
class Photo(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', verbose_name='入侵人员照片')
    class Meta:
            verbose_name = '照片'
            verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.create_time)
