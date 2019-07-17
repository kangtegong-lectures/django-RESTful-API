from django.db import models

# Django로 Web Application을 만들때 Model을 정의하는 것과 다르지 않다

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
