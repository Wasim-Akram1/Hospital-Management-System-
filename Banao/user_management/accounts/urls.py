from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('book_appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('appointment_details/<int:appointment_id>/', views.appointment_details, name='appointment_details'),
]
