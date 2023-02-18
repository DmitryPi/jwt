from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(["GET"])
def get_routes(request):
    routes = [
        request.build_absolute_uri(reverse("token_obtain_pair")),
        request.build_absolute_uri(reverse("token_refresh")),
        request.build_absolute_uri(reverse("token_verify")),
    ]
    return Response(routes)
