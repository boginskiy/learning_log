from django.db import models

class Topic(models.Model):
    """Тема, которую изучает пользователь."""

    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Foo():
    def __init__(self, qwerty, asdfg):
        self.qwerty = qwerty
        self.asdfg = asdfg
