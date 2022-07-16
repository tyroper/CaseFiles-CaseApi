from django.contrib import admin
from django.urls import path
from .views import CaseList, CaseDetail, BanList, BanDetail, ModeratorDetail, ModeratorList, VoteList, VoteDetail

urlpatterns = [
    path('case', CaseList.as_view(), name='caselistcreate'),
    path('case/<int:pk>', CaseDetail.as_view(), name='casedetaildestroy'),
    path('ban', BanList.as_view(), name='banlistcreate'),
    path('ban/<int:pk>', BanDetail.as_view(), name='bandetaildestroy'),
    path('moderator', ModeratorList.as_view(), name='moderatorlistcreate'),
    path('moderator/<int:pk>', ModeratorDetail.as_view(),
         name='moderatordetaildestroy'),
    path('vote', VoteList.as_view(), name='votelistcreate'),
    path('vote/<int:pk>', VoteDetail.as_view(), name='votedetaildestroy')
]
