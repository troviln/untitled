from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  url(r'^$', views.post_list, name='post_list'),
                  url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
                  url(r'^post/new/$', views.post_new, name='post_new'),
                  url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
                  url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
                  url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
                  url(r'^post/(?P<pk>[0-9]+)/change/$', views.post_change, name='post_change'),
                  url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
                  url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
                  url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
                  url(r'^post/(?P<pk>[0-9]+)/like/$', views.post_likes, name='post_likes'),
                  url(r'^page/(?P<page_number>\d+)/$', views.post_list, name='post_list'),
                  url(r'^tag_search/(?P<tag>\w+)/$', views.post_tag_search, name='post_tag_search'),
                  url(r'^new/tag/$', views.new_tag, name='post_add_tag'),
                  #url(r'^add_message/$', views.add_message_chat, name='add_message_to_chat'),
                  #url(r'^delete_message/$', views.delete_message_chat, name='delete_message_chat'),

                  # -with drf classes
                  url(r'^api/v1/chat/$', views.ChatCollection.as_view()),
                  url(r'^api/v1/chat_member/(?P<pk>[0-9]+)/$', views.ChatMember.as_view()),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
