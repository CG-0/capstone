from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        labels = {
            'first_name': 'Your First Name',
            'last_name': 'Your Last Name',
            'email': 'Your Email',
            'subject': 'What Do You Want To Talk About?',
            'message': 'Write Down Your Comment'
        }

        error_messages = {
            'first_name': {
                'required': 'Your first name cannot be empty'
            },
            'last_name': {
                'required': 'Your last name cannot be empty'
            },
        }