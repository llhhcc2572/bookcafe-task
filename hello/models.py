import datetime
from pydoc import describe
from django.db import models
from django.utils import timezone

# Create your models here.
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    """
class PossessingBook(models.Model) :
    title = models.CharField(max_length=200)
    link =  models.CharField(max_length=200)
    image = models.ImageField()
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    describe = models.CharField(max_length=500)
    pubdate = models.DateTimeField('date published')

class WishBook(models.Model):
    title = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    insertdate =models.DateTimeField('insertdate')
    reqstatus = models.CharField(max_length=200)
    statusmsg = models.CharField(max_length=200)
    updatedate = models.DateTimeField('updatedate')
