from rest_framework import serializers
from .models import Feedback,FeedbackQuestion

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'




class FeedbackQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedbackQuestion
        fields='__all__'

