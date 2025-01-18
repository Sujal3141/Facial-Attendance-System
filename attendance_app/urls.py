from django.contrib import admin
from django.urls import path,include
from attendance_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),
    path('new_user', views.user_profile_view, name='user_profile'),
    path('view_profiles',views.view_profiles,name='view_profiles'),
    # path('login/', views.LoginView(template_name='login.html'), name='login')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

