from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField

class rules(models.Model):
  name= models.CharField(max_length=60)
  activation= models.CharField(max_length=60)
  rule_description= MarkdownxField()
  penalty= models.CharField(max_length=60)
  creator= models.ForeignKey(User, on_delete=models.DO_NOTHING)

  def __str__(self):
    return self.name
  class Meta:
    verbose_name_plural = "Rules"