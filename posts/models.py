from django.db import models

# Create your models here.


class Post(models.Model):
  """
  Post field
  """
  text = models.TextField()

  def __str__(self):
    """
    post object displayed name
    """
    return self.text[:50]
