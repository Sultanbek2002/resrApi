from django.db import models
import uuid
# Create your models here.
class Workapi(models.Model):
    id=models.UUIDField(primary_key=True,blank=False,editable=False,default=uuid.uuid4())
    tittle=models.CharField(max_length=300)
    name=models.CharField(max_length=250)
    description=models.TextField()