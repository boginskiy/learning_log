from django.db import models

class Topic(models.Model):
    """Тема, которую изучает пользователь."""

    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Информация изученная пользователем по теме."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f'{self.text[:50]}...' if len(self.text) > 50 else f'{self.text}'

