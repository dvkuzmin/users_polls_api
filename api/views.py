from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Poll, Question, Choice, Answer, AnonymousUser
from .serializer import (
	PollSerializer, QuestionSerializer, 
	OwnAnswerSerializer, OneChoiceSerializer,
	SeveralChoiceSerializer, GetAnswersSerializer,
	AnonymousUserSerializer,
)

class AnonymousUserView(APIView):
	def post(self, request):
		name = request.data.get("user")
		user = AnonymousUser(name=name["name"])
		user.save()
		# serializer = AnonymousUserSerializer(data=name)
		# if serializer.is_valid(raise_exception=True):
		# 	user_saved = serializer.save()
		return Response({"success": f"AnonymousUser {user.name} created"})

class PollView(APIView):
	def get(self, request):
		polls = Poll.objects.all()
		serializer = PollSerializer(polls, many=True)
		return Response({"polls": serializer.data})

class OnePollReturnQuestionsView(APIView):
	def get(self, request, pk):
		poll = Poll.objects.get(pk=pk)
		questions = poll.questions.all()
		serializer = QuestionSerializer(questions, many=True)
		return Response({'questions': serializer.data})

class AnswerView(APIView):
	def post(self, request):
		answer = request.data.get('answer')
		question_type = int(answer["question_id"])
		question = Question.objects.get(pk=question_type)
		if question.type_of_question == "text_answer":
			name = AnonymousUser.objects.get(id=int(answer["name_id"]))
			question = Question.objects.get(pk=int(answer["question_id"]))
			own_text = str(answer["own_text"])
			poll = Poll.objects.get(pk=int(answer["poll_id"]))
			answer = Answer(name=name, question=question, own_text=own_text, poll=poll)
			answer.save()
			# serializer = OwnAnswerSerializer(data=answer)
			# if serializer.is_valid(raise_exception=True):
			# 	answer_saved = serializer.save()
		elif question.type_of_question == "one_choice_answer":
			name = AnonymousUser.objects.get(pk=int(answer["name_id"]))
			question = Question.objects.get(pk=int(answer["question_id"]))
			one_choice = Choice.objects.get(pk=int(answer["one_choice_id"]))
			poll = Poll.objects.get(pk=int(answer["poll_id"]))
			answer = Answer(name=name, question=question, one_choice=one_choice, poll=poll)
			answer.save()
			# serializer = OneChoiceSerializer(data=answer)
			# if serializer.is_valid(raise_exception=True):
			# 	answer_saved = serializer.save()
		elif question.type_of_question == "several_choice_answer":
			name = AnonymousUser.objects.get(pk=int(answer["name_id"]))
			question = Question.objects.get(pk=int(answer["question_id"]))
			poll = Poll.objects.get(pk=int(answer["poll_id"]))
			several_choice = list(answer["several_choice"])
			answer = Answer(name=name, question=question, poll=poll)
			answer.save()
			for i in several_choice:
				answer.several_choice.add(Choice.objects.get(pk=i))
			answer.save()
		return Response({"success": f"Your answer was saved"})

class GetAnswersView(APIView):
	def get(self, request, name_id, poll_id):
		answers = Answer.objects.filter(name_id=name_id, poll_id=poll_id)
		serializer = GetAnswersSerializer(answers, many=True)
		return Response({'answers': serializer.data})	




