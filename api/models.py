from django.db import models
from django.utils import timezone

class AnonymousUser(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Poll(models.Model):
	name = models.CharField(max_length=100)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	description = models.TextField()

	def __str__(self):
		return self.name

	def end_date_not_become(self):
		if end_date > timezone.now():
			return True


QUESTION_TYPES = (
	('text_answer', 'Ответ текстом'),
	('one_choice_answer', 'Ответ с выбором одного варианта'),
	('several_choice_answer', 'Ответ с выбором нескольких вариантов')
)

class Question(models.Model):
	text = models.TextField()
	type_of_question = models.CharField(max_length=40, choices=QUESTION_TYPES)
	poll = models.ForeignKey('Poll', related_name='questions', on_delete=models.CASCADE)

	def __str__(self):
		return self.text

class Choice(models.Model):
	text = models.TextField()
	question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE)

	def __str__(self):
		return self.text

class Answer(models.Model):
	name = models.ForeignKey('AnonymousUser', related_name='answers', null=True, on_delete=models.CASCADE)
	question = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE, null=True, blank=True)	
	one_choice = models.ForeignKey('Choice', related_name='one_choice', on_delete=models.CASCADE, null=True, blank=True)
	several_choice = models.ManyToManyField('Choice', related_name='several_choice')
	own_text = models.TextField(null=True, blank=True)
	poll = models.ForeignKey('Poll', related_name='answers', on_delete=models.CASCADE, null=True)