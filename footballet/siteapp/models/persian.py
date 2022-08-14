from ensurepip import version
from django.db import models

class PersianSite(models.Model):

    name=models.CharField(verbose_name="نام سایت", max_length=200)
    url=models.URLField(verbose_name="آدرس سایت",unique=True)

    class Meta:
        verbose_name="سایت ایرانی"
        verbose_name_plural="سایت های ایرانی"

    def __str__(self) -> str:
        return self.name
       