from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView,\
    RetrieveAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .services import get_services
from .serializers import PerformedServicesSerializer, DoctorTimetableSerializer, DoctorSerializer
from customer_management.models import CustomerInsurance
from customer_personal_cabinet.models import DoctorTimetable, Doctor


# Список выполняемых услуг
class PerformedServicesView(APIView):

    def post(self, request):
        results = PerformedServicesSerializer(data=request.data)
        if results.is_valid(raise_exception=True):
            card_number = request.data.get('card_number')
            try:
                customer = CustomerInsurance.objects.get(card_number=card_number)
                insurance = customer.insurance
                performed_services = get_services(insurance.code, request.data)
                return Response(performed_services)
            except CustomerInsurance.DoesNotExist:
                return Response({'Клиент с указанной картой, не найден!'})
        return Response({})


# Mixin счет реестра
class DoctorMixin:
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


# Список счет реесторов по ИИН
class DoctorByHospital(DoctorMixin, ListAPIView):

    def get_queryset(self):
        queryset = self.queryset.filter(hospital__code=self.kwargs['code'])
        return queryset


# Mixin графика работы доктора
class DoctorTimetableMixin:
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = DoctorTimetable.objects.all()
    serializer_class = DoctorTimetableSerializer


# Создать счет реестр
class DoctorTimetableCreateView(DoctorTimetableMixin, CreateAPIView):
    name = 'doctor-timetable-create'


# Посмотреть детальную информацию счет реестра
class DoctorTimetableDetail(DoctorTimetableMixin, RetrieveUpdateDestroyAPIView):
    name = 'doctor-timetable-detail'