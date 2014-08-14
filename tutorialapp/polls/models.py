from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Date published')
    def total_votes(self):
        total = 0
        for choice in self.choice_set.all():
            total += choice.votes
        return total
    def __unicode__(self):
        return self.question
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __unicode__(self):
        return "%s (%i votes)" % (self.choice_text, self.votes)

