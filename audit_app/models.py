from django.db import models


# Create your models here.
class Audit(models.Model):
    id = models.AutoField(primary_key=True)
    source_app = models.CharField(max_length=30)
    audited_user = models.CharField(max_length=30)
    description = models.TextField()
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'AUDITS'
