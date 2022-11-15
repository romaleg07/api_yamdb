import uuid

from api.permissions import IsAuthenticatedOrAdmin
from api.serializers import (TokenSerializer, UserEditSerializer,
                             UserListSerializer, UserSerializer)
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class SignupViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        email = serializer.validated_data.get('email')
        confirmation_code = uuid.uuid4().hex
        serializer.save(confirmation_code=confirmation_code)

        send_mail(
            'Code for get token',
            confirmation_code,
            'bestTeam@ever.com',
            [email],
            fail_silently=False,
        )
        return Response('serializer.data', status=status.HTTP_200_OK)


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.initial_data.get('username')
            user = get_object_or_404(User, username=username)
            confirmation_code = serializer.initial_data.get(
                'confirmation_code'
            )

            if user.confirmation_code != confirmation_code:
                return Response(
                    {"token": "incorrect"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({"token": f"{access_token}"})
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UsersViewSet(viewsets.ModelViewSet):
    lookup_field = "username"
    queryset = User.objects.all()
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticatedOrAdmin,)
    serializer_class = UserListSerializer
    filter_backends = (filters.OrderingFilter,)


@action(detail=False, methods=['get'])
class MeViewSet(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserEditSerializer
    pagination_class = None

    def get_object(self):
        username = self.request.user.username
        return get_object_or_404(User, username=username)

    def perform_update(self, serializer):
        serializer.save()
