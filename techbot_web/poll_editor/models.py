from django.db import models
from django.utils.translation import ugettext_lazy as _
from random import choice
from string import ascii_uppercase, digits


# Create your models here.

def id_generator(size=8, chars=ascii_uppercase + digits):
    return ''.join(choice(chars) for _ in range(size))


class User(models.Model):
    name = models.CharField(_('Name'), max_length=128)
    last_name = models.CharField(_('Last name'), max_length=128)
    telegram_id = models.IntegerField()
    register_date = models.DateTimeField(_('Data registration'), auto_now_add=True)

    def __str__(self):
        return '{name} {last_name}'.format(name=self.name, last_name=self.last_name)

    class Meta:
        ordering = ['-name']
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Poll(models.Model):
    owner = models.ForeignKey('User')
    name = models.CharField(_('Poll name'), max_length=128)
    code = models.CharField(_('Code'), max_length=8, unique=True, default=id_generator)
    passes = models.IntegerField(default=0)
    creation_date = models.DateTimeField(_('Date created'), auto_now_add=True)

    def __str__(self):
        return 'Poll {name} by {owner}'.format(name=self.name, owner=self.owner.name)

    class Meta:
        ordering = ['-name']
        verbose_name = _('Poll')
        verbose_name_plural = _('Polls')


class Question(models.Model):
    from_poll = models.ForeignKey('Poll')
    caption = models.CharField(_('Question caption'), max_length=128)

    def __str__(self):
        return '{caption}'.format(caption=self.caption)

    class Meta:
        ordering = ['-caption']
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')


class Answer(models.Model):
    on_question = models.ForeignKey('Question')
    caption = models.CharField(_('Answer caption'), max_length=128)

    def __str__(self):
        return 'Answer: {caption} for question {question_id}'.format(caption=self.caption,
                                                                     question_id=self.on_question.id)

    class Meta:
        ordering = ['-caption']
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
