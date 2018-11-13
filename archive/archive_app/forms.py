from django import forms
from .models import Question
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = False

    class Meta:
        model = Question
        fields = ('questionName', 'difficulty', 'questionLink', 'solutionLink', 'summary',)
        required=()

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']