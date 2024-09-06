from django.db import models


# Create your models here.
class Post(models.Model):
    """
    This class will represent a bulletin board post.

    Fields:
        - title: The title name of the post with a 255-character limit
        - content: The content of the post stored in a TextField
        - created_at: The date and time of when the post was creat stored in a
        DateTimeField.
        - author: The author of the post which will be a ForeignKey
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True,
                               blank=True)


class Author(models.Model):
    """
    This class will represent the author of a bulletin board post.

    Fields:
        - name: The author's name stored in a TextField with a
        255-character limit

    """

    name = models.CharField(max_length=255)
