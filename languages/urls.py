from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages',views.LanguageView)
router.register('parading',views.ParadignView)
router.register('programer',views.ProgramerView)

urlpatterns = [
    path('',include(router.urls))
]
