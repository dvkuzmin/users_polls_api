from rest_framework import serializers
from .models import Poll, Question, Choice, Answer, AnonymousUser

class PollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poll
		fields = ('name', 'description')

class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ('text', 'question', 'id')		

class QuestionSerializer(serializers.ModelSerializer):
	choices = ChoiceSerializer(many=True)
	class Meta:
		model = Question
		fields = ('text', 'choices', 'type_of_question', 'poll', 'id')


class GetAnswersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('name', 'question', 'one_choice', 'several_choice', 'own_text')