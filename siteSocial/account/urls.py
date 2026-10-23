from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    # Alteração de senha
    #path('password-change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html'), name='password_change'),
    #path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),

    # Redefinição de senha (Adicione a view faltante aqui)
    #path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]