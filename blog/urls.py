from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
   path('',views.all_blogs,name='all-blogs'),
   path('<int:id>/',views.blog_detail,name='blog-detail'),
]