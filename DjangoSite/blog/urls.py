from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    # post views

    # url pattern for function based view
    # path('', views.post_list, name='post_list'),

    # url patterns for class based view
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),
    path('search/', views.post_search, name='post_search'),
    path('subscribe/', views.email_list_signup, name='subscribe'),
    path('account/', include('account.urls')),
]
