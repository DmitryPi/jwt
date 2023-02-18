from django.urls import resolve, reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_routes(request):
    routes = [
        request.build_absolute_uri(reverse("token_obtain_pair")),
        request.build_absolute_uri(reverse("token_refresh")),
        request.build_absolute_uri(reverse("token_verify")),
    ]
    return Response(routes)
