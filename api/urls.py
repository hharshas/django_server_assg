from django.urls import path
from . import views 
from .views import TimetableListView, TimetableUpdate, UserTimetableView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
    path('timetable/', TimetableListView.as_view(), name='timetable-list'),
    path('timetable/<int:pk>/', TimetableUpdate.as_view(), name='timetable-detail'),
    path('timetable/<str:username>/', UserTimetableView.as_view(), name='user-timetable'),
]