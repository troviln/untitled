
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post, Comment, Tag, Chat
from .forms import PostForm, CommentForm, TagForm, ChatForm
from django.contrib.auth.decorators import login_required,permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.http import HttpResponse, QueryDict
from django.core.paginator import Paginator
import json
from rest_framework import generics
from .serializers import ChatSerializer
from django.contrib.auth import authenticate, login


def post_list(request, page_number=1):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    current_page = Paginator(posts, 5)

    chat_form = ChatForm

    return render(request, 'blog/post_list.html', {'post': current_page.page(page_number),
                                                   'chat_form': chat_form})


def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    form = CommentForm
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})




def post_tag_search(request, tag, page_number=1):

    tag_tag = get_object_or_404(Tag, tag=tag)
    tag_id = tag_tag.id
    posts = Post.objects.filter(tags=tag_id, published_date__lte=timezone.now()).order_by('-published_date')
    current_page = Paginator(posts,5)
    chat_block = Chat.objects.all
    chat_form = ChatForm
    return render(request, 'blog/post_list.html', {'post': current_page.page(page_number),
                                                   'chat_block': chat_block, 'chat_form': chat_form})


@login_required
@permission_required('blog.add_post', login_url='/blog/')
def post_new(request):
     if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
     else:
        form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})

@login_required
@permission_required('blog.change_post', login_url='/blog/')
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
@permission_required('blog.change_post', login_url='/blog/')
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

@login_required
@permission_required('blog.delete_post', login_url='/blog/')
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    post.image.delete(save=False)

    return redirect('blog.views.post_list')


@login_required
@permission_required('blog.add_post', login_url='/')
def post_likes(request, pk):

    try:

        if pk in request.COOKIES :
            post = get_object_or_404(Post, pk=pk)
            post.likes -= 1
            post.save()
            response = redirect(request.GET.get('next', '/'))
            response.delete_cookie(pk)
            return response
        else:
            post = get_object_or_404(Post, pk=pk)
            post.likes += 1
            post.save()
            response = redirect(request.GET.get('next', '/'))
            response.set_cookie(pk, 'like')
            return response
    except ObjectDoesNotExist:
        raise Http404


@login_required
@permission_required('blog.change_post', login_url='/blog/')
def new_tag(request):
    if request.method == "POST":
         form_tag = TagForm(request.POST)
         if form_tag.is_valid():
             #post = form_tag.exist_tag
             post = form_tag.save(commit=False)
             post.save()
             form_tag.save_m2m()
             return redirect(request.GET.get('next', '/'))

    else:
        form_tag = TagForm()

    return render(request, 'blog/blog_new_teg.html', {'form_tag': form_tag})

@login_required
@permission_required('blog.change_post', login_url='/blog/')
def post_change(request, pk):
    before_edit = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=before_edit)
        if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             form.save_m2m()
             return redirect('post_detail', pk=pk)


    else:
        form = PostForm(instance=before_edit)


    return render(request, 'blog/post_change.html', {'form': form})




def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('blog.views.post_detail', pk=post.pk)



#----------------------chat----------------------------

class ChatCollection(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatMember(generics.RetrieveDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


'''
def add_message_chat(request):

    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Chat(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created_date'] = post.created_date.strftime('%d %B, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def delete_message_chat(request):
    if request.method == 'DELETE':

        post = Chat.objects.get(pk=int(QueryDict(request.body).get('postpk')))

        post.delete()

        response_data = {}
        response_data['msg'] = 'Post was deleted.'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
'''
#----------------------endchat----------------------------

@login_required
@permission_required('blog.change_comment', login_url='/blog/')
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)


@login_required
@permission_required('blog.add_comment', login_url='/blog/')
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)


def chat(request):

    chat_block = get_object_or_404(Chat,)
    chat_form = ChatForm
    return render(request, 'blog/post_list.html', {'post': chat_block, 'chat_form': chat_form})