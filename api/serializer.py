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

class AnonymousUserSerializer(serializers.Serializer):
	name = serializers.CharField()
	name_id = serializers.IntegerField()
	def create(self, validated_data):
		return AnonymousUser.objects.create(**validated_data)

class OwnAnswerSerializer(serializers.Serializer):
	name_id = serializers.IntegerField()
	question_id = serializers.IntegerField()
	own_text = serializers.CharField()
	poll_id = serializers.IntegerField()
	

	def create(self, validated_data):
		return Answer.objects.create(**validated_data)

class OneChoiceSerializer(serializers.Serializer):
	name_id = serializers.IntegerField()
	question_id = serializers.IntegerField()
	one_choice_id = serializers.IntegerField()
	poll_id = serializers.IntegerField()

	def create(self, validated_data):
		return Answer.objects.create(**validated_data)


class SeveralChoiceSerializer(serializers.Serializer):
	name_id = serializers.IntegerField()
	question_id = serializers.IntegerField()
	poll_id = serializers.IntegerField()
	
	def create(self, validated_data):
		return Answer.objects.create(**validated_data)

class GetAnswersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('name', 'question', 'one_choice', 'several_choice', 'own_text')