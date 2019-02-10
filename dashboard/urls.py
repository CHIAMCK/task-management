from django.urls import path
import dashboard.views

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard.views.MainDashboardView.as_view(), name='main'),
]