from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostListOrCreate.as_view()),
    path('posts/<int:pk>/', views.PostDetailUpdateDelete.as_view()),
    path('api-auth/', include('rest_framework.urls')),#it enable login button in browsable api
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
#Reason for using format_suffix_patterns
'''A common pattern for Web APIs is to use filename extensions on URLs to provide an endpoint for a given media type. For example, ‘http://example.com/api/users.json’ to serve a JSON representation.

Adding format-suffix patterns to each individual entry in the URLconf for your API is error-prone and non-DRY, so REST framework provides a shortcut to adding these patterns to your URLConf.'''