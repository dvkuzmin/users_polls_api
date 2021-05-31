from django.urls import path

from .views import PollView, OnePollReturnQuestionsView, AnswerView, GetAnswersView, AnonymousUserView

app_name = 'api'

urlpatterns = [
	path('polls/', PollView.as_view()),
	path('poll/<int:pk>/', OnePollReturnQuestionsView.as_view()),
	path('user/', AnonymousUserView.as_view()),
	path('answer/', AnswerView.as_view()),
	path('get_answers/<int:name_id>/<int:poll_id>/', GetAnswersView.as_view()),
]