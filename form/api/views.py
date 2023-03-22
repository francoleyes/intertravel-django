from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from form.models import Form
from form.api.serializers import FormSerializer

class FormApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = FormSerializer
    queryset = Form.objects.all()