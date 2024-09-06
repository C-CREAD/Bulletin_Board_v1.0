from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm


# Create your views here.
def authentication(request):
    """Checks if the user is logged in and returns True or redirects user
    back to the login page."""
    if request.user.is_authenticated is False:
        return HttpResponseRedirect(reverse('user_auth:login'))


def post_list(request):
    """
    This function will render a template displaying of all posts

    :param request: HTTP request object.
    :return: Rendered template with a list of posts.
    """
    if request.user.is_authenticated:
        posts = Post.objects.all()

        # Declare a dictionary to store the context of the post
        context = {
            'posts': posts,
            'page_title': 'List of Posts',
        }

        return render(request, 'posts/post_list.html', context)

    else:
        return authentication(request)


def post_detail(request, pk):
    """
    This function will render a template displaying the specific
    post details.

    :param request: HTTP request object.
    :param pk: Primary key of the post.
    :return: Rendered template with details of the specific post.
    """
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'posts/post_detail.html', {'post': post})

    else:
        return authentication(request)


def post_create(request):
    """
    This function will create a new post.

    :param request: HTTP request object.
    :return: Rendered template for creating a new post.
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)

            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('post_list')
        else:
            form = PostForm()

        return render(request, 'posts/post_form.html', {'form': form})
    else:
        return authentication(request)


def post_update(request, pk):
    """
    This function will update an existing post.

    :param request: HTTP request object.
    :param pk: Primary key of the post to be updated.
    :return: Rendered template for updating the specific post.
    """
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)

            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('post_list')
        else:
            form = PostForm(instance=post)
        return render(request, 'posts/post_form.html', {'form': form})
    else:
        return authentication(request)


def post_delete(request, pk):
    """
    This function will delete an existing post.

    :param request: HTTP request object.
    :param pk: Primary key of the post to be deleted
    :return: Redirect to the post list after deletion.
    """
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('post_list')
    else:
        return authentication(request)