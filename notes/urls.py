from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.user_login,name='login'),
    path('signup',views.signup,name='signup'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('admin_home',views.admin_home,name='home'),
    path('logout',views.Logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('uploadnotes',views.uploadnotes,name='uploadnotes'),
    path('viewmynotes',views.viewmynotes,name='viewmynotes'),
    path('viewallnotes',views.viewallnotes,name='viewallnotes'),
    path('delete_note/<int:id>/',views.delete_note,name='delete_note'),
    path('admin_allnotes',views.admin_allnotes,name='admin_allnotes'),
    path('admin_delete_note',views.admin_delete_note,name='admin_delete_note'),
    path('change_status/<int:id>/',views.change_status,name="change_status"),
    path('admin_viewallusers',views.admin_viewallusers,name='admin_viewallusers'),
    path('admin_deleteuser/<int:id>/',views.admin_deleteuser,name='admin_deleteuser'),
    path('showprofile',views.showprofile,name='showprofile')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)