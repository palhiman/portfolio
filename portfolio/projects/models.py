from django.db import models

# Create your models here.
class Project(models.Model):
    # project id
    projectId = models.BigIntegerField(primary_key=True, null=False)
    # project title
    title = models.CharField(max_length=50)
    createdAt = models.DateTimeField("Crated At")
    updateAt = models.DateTimeField("Updated At")
    publishedAt = models.DateTimeField("Published At")
    # source code link
    source_link = models.TextField()

