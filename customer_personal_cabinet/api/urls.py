from django.urls import path
from . import views

app_name = 'customer_management_api'

urlpatterns = [
    path('performed/services', views.PerformedServicesView.as_view(),
         name='performed_services'),
    path('doctor/timetable/create', views.DoctorTimetableCreateView.as_view(), name='doctor-timetable-create'),
    path('doctor/timetable/<int:pk>/detail', views.DoctorTimetableDetail.as_view(), name='doctor-timetable-detail'),

    path('doctor/<str:code>/by_hospital', views.DoctorByHospital.as_view(),
         name='doctor_by_hospital'),

    path('aggregat/free/slots', views.AggregateFreeSlotsView.as_view(),
         name='aggregat_free_slots'),
    path('customer/professional/examination', views.CustomerProfessionalExaminationView.as_view(),
         name='customer_professional_examination'),



]
