from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Topics'

    def __str__(self):
        """Return a string representation fo the model."""
        return self.text


class Entry(models.Model):
    """Somthing specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"
