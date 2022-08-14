from ensurepip import version
from django.db import models

class EnglishSite(models.Model):

    name=models.CharField(verbose_name="نام سایت", max_length=200)
    url=models.URLField(verbose_name="آدرس سایت",unique=True)

    class Meta:
        verbose_name="سایت خارجی"
        verbose_name_plural="سایت های خارجی"

    def __str__(self) -> str:
        return self.name
       