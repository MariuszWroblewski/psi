from django.urls import path
from . import views


urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('turnieje', views.TurniejList.as_view(), name=views.TurniejList.name),
    path('turnieje/<int:pk>', views.TurniejDetail.as_view(), name=views.TurniejDetail.name),
    path('rozgrywki', views.RozgrywkaList.as_view(), name=views.RozgrywkaList.name),
    path('rozgrywki/<int:pk>', views.RozgrywkaDetail.as_view(), name=views.RozgrywkaDetail.name),
    path('uczestnicy', views.UczestnikList.as_view(), name=views.UczestnikList.name),
    path('uczestnicy/<int:pk>', views.UczestnikDetail.as_view(), name=views.UczestnikDetail.name),
    path('sedziowie', views.SedziaList.as_view(), name=views.SedziaList.name),
    path('sedziowie/<int:pk>', views.SedziaDetail.as_view(), name=views.SedziaDetail.name),
]
