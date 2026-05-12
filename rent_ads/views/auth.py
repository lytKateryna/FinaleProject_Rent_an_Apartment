from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.exceptions import TokenError
from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken

from rent_ads.serializers.auth import RegisterSerializer, LoginSerializer
from rent_ads.utils import set_jwt_cookies, REFRESH_COOKIE_NAME, clear_jwt_cookies





@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @extend_schema(request=RegisterSerializer, responses={201: RegisterSerializer})
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response = Response(
                {
                    'user': {
                        'username': user.username,
                        'email': user.email
                    }
                },
                status=status.HTTP_201_CREATED
            )
            set_jwt_cookies(response, user)
            return response
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


@method_decorator(csrf_exempt, name='dispatch')
class UserLoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @extend_schema(request=LoginSerializer, responses={200: None})
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        response = Response(
            {"message": "Login successful"},
            status=status.HTTP_200_OK
        )
        try:
            set_jwt_cookies(response=response, user=user)
            return response

        except Exception as e:
            return Response(
                data={
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=None, responses={200: None})
    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            refresh_token = request.COOKIES.get(REFRESH_COOKIE_NAME)
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

        except TokenError:
            pass

        except Exception as e:
            return Response(
                data={
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        response = Response(
            {"message": "Logout successful"},
            status=status.HTTP_200_OK
        )
        clear_jwt_cookies(response=response)
        return response

