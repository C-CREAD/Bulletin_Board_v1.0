from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """
    This class will represent a Form for creating and updating
    Post objects.

    Fields:
        - title: The title name of the post
        - content: The content of the post stored in a TextField

    Meta class:
        - Defines the model to use the Post object and the fields
        included in the form.
    """

    class Meta:

        model = Post
        fields = ['title', 'content', 'author']