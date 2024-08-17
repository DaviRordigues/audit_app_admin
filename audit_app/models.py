from django.db import models


# Create your models here.
class Audit(models.Model):
    id = models.AutoField(primary_key=True)
    source_app = models.CharField(max_length=30)
    audited_user = models.CharField(max_length=30, verbose_name= "usuário auditado")
    description = models.TextField(verbose_name="descrição")
    creation_date = models.DateTimeField(verbose_name="data de criação")
    action = models.CharField(max_length=30, verbose_name="ação")

    class Meta:
        managed = False
        db_table = 'AUDITS'
