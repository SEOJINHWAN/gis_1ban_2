from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        # User에게 입력받을 수 있는 것
        fields = ['content']
