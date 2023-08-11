
from django.urls import path,include

from .views import DepartmanView,PersonelView

from rest_framework import routers

router =routers.DefaultRouter()
router.register('departman',DepartmanView )
router.register('personel',PersonelView)

urlpatterns = [
    path("",include(router.urls))
 
]
