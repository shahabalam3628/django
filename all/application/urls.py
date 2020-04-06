"""all URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from application import views
from application.views import BookList

urlpatterns = [
    path('company',views.company_home, name='company'),
    path('organization',views.org_home, name='organization'),
    path('mypost',views.mypost, name='mypost'),
    path('getpost',views.getPost, name='getpost'),
    path('person',views.person, name='person'),
    path('registration',views.registration, name='registration'),
    path('setsession',views.setSession, name='setsession'),
    path('getsession',views.getSession, name='getsession'),




     path('contact1',views.contact_us, name='contact1'),
     path('emaildemo',views.home, name='emaildemo'),
     path('sending1',views.sendmail, name='sending1'),





    path('page2',views.post_list, name='page2'),
    path('page3',views.index, name='page3'),
    path('page1', BookList.as_view(), name='page1')
    

    
    
    
    
    #path('index',views.index, name='index'),
    #path('addnew',views.addnew, name='addnew'),
    #path('fetch/',views.get_data, name='fetch'),
    #path('delete/<int:userid>',views.delete_user, name='delete'),
    #path('edit/<int:userid>',views.user_edit, name='edit'),
   # path('update/<int:userid>',views.update_student, name='update'),

]