from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
# from .views import RegistrationView

from . import views
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
#router.register(prefix='list', viewset=RegistrationView, base_name='Registration')
router.register(r'classlevel', views.ClassLevelViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'program', views.ProgramViewSet)

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]