from django.urls import path,include
from . import views
app_name='app'
urlpatterns=[
    path('',views.UserCreate.as_view(),name="register"),
    path('index',views.index.as_view(),name="index"),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('postjob',views.PostJob.as_view(),name="postjob"),
]