from django.urls import path
from .views import homeAdmin,login_view,logout_view,delete_video

urlpatterns = [
    path('profile/', homeAdmin.as_view(), name='hAdmin'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('<int:pk>/delete',delete_video.as_view(),name='delete'),
]

