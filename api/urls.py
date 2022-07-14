from django.contrib import admin
from django.urls import path
from .views import CaseList, CaseDetail

urlpatterns = [
    path('case', CaseList.as_view(), name='listcreate'),
    path('case/<int:pk>', CaseDetail.as_view(), name='detailcreate')
]
