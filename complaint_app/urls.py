from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('addcomplaint',views.addcomplaint, name='addcomplaint'),
    path('mycomplaints',views.mycomplaints, name='mycomplaints'),
    path('viewcomplaint/<int:compt_id>',views.viewcomplaint, name='viewcomplaint'),
    path('allusers',views.allusers, name='allusers'),
    path('complaintreply',views.complaintreply, name='complaintreply'),
    path('logout',views.logout, name='logout'),
]