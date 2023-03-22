from rest_framework.serializers import ModelSerializer
from form.models import Form

class FormSerializer(ModelSerializer):
    class Meta:
        model = Form
        fields = ['full_name', 'email', 'mobile']