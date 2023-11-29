from django.urls import path
from . import views

app_name = 'majanmania'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),

    path('yaku/',views.YakubutuView.as_view(),name='yaku'),

    path('yakubutuform/',views.YakuFormView.as_view(),name='yakuform'),

    path('yaku_done/', views.YakuSuccessView.as_view(), name='yaku_done'),

    path('rule/', views.RuleView.as_view(), name='rule'),

    path('contact/', views.ContactView.as_view(), name='contact'),

    
]