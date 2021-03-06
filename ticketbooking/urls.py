"""ticketbooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from account.views import LoginView, SignupView, logout_view, EditView, ChangePassword
import announcement.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', announcement.views.dashboard, name="dashboard"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', logout_view, name="logout"),
    path('profile/edit', EditView.as_view(), name="editProfile"),
    path('profile/changepassword', ChangePassword.as_view(), name='changePassword'),
    path('signup', SignupView.as_view(), name="signup"),
    path('booking/', include('booking.urls')),
    path('schedule/', include('schedule.urls')),
    path('transaction', include('transaction.urls')),
    path('announcement/', include('announcement.urls')),
    path('api/', include('api.urls')),
]
