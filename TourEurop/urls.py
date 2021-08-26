"""TourEurop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from tour_app import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostListView.as_view(), name="tour_app-home"),
    path('about/', views.about, name='tour_app-about'),
    path('help/', views.help_fq, name='tour_app-help'),
    path('profile/', user_views.profile, name='users-profile'),
    path('register/', user_views.register, name='users-register'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="users-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="users-logout"),
    path('post/<int:pk>/', views.PostDetailViews.as_view(), name='tour_app-detail'),
    path('tour/new/', views.PostCreateView.as_view(), name="tour_app-create"),
    path('tour/<int:pk>/update', views.PostUpdateView.as_view(), name="tour_app-update"),
    path('tour/user/<str:username>', views.UserPostListView.as_view(), name="tour_app-user_tours"),
    path('tour/<int:pk>/delete', views.PostDeleteView.as_view(), name="tour_app-delete"),
]
# handler для 404
handler404 = 'tour_app.views.page_not_found'
#handler500 = 'tour_app.views.error_500_view'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
