from django.db import models
import random
import string

def random_string(stringLength=30):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Create your models here.
class Checkpoint(models.Model):
    uuid = models.CharField(primary_key=True, default=random_string, editable=True, max_length=200)
    name = models.CharField('Name', max_length=200)
    puzzle = models.URLField('Puzzle', max_length=200, blank=True)
    location = models.CharField('Location', max_length=200, blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField('Name', max_length=200)
    uuid = models.CharField(primary_key=True, default=random_string, editable=True, max_length=200)

    def __str__(self):
        return self.name

class Visit(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    checkpoint = models.ForeignKey(Checkpoint, on_delete=models.CASCADE)
    date_visited = models.DateTimeField()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['team', 'checkpoint'], name='Constraint')
        ]