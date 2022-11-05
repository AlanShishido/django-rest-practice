from django.db import models

# Create your models here.
class Cadastro(models.Model):
  name = models.CharField(max_length=64)
  idade = models.IntegerField()
  email = models.CharField(max_length=32, primary_key=True)

  def __str__(self):
    return self.name

class Comentario(models.Model):
  email = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
  avaliacao = models.IntegerField()
  comentario = models.TextField()
  
  def __str__(self):
    return f'{self.email}'
    