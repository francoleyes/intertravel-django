from rest_framework.routers import DefaultRouter
from form.api.views import FormApiViewSet

router_form = DefaultRouter()

router_form.register(
    prefix='form', basename='form', viewset=FormApiViewSet
)