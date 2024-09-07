from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from ..serializers import LoginSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class SignupView(APIView):
    def post(self, request):
        data = request.data
        password = data.get('userpwd')  # 클라이언트가 'userpwd' 필드로 비밀번호를 전송한다고 가정

        # 비밀번호가 제공되지 않으면 에러 반환
        if not password:
            return Response(
                {"status": "fail", "message": "비밀번호가 제공되지 않았습니다."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 비밀번호 해시화
        hashed_password = make_password(password)
        data['userpwd'] = hashed_password

        # 시리얼라이저로 데이터 검증 및 저장 시도
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "회원가입이 성공적으로 완료되었습니다.",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        # 실패한 경우, 시리얼라이저의 오류를 반환
        return Response(
            {
                "status": "fail",
                "message": "회원가입에 실패했습니다.",
                "errors": serializer.errors  # 시리얼라이저의 상세 오류 메시지 포함
            },
            status=status.HTTP_400_BAD_REQUEST
        )

@method_decorator(csrf_exempt, name='dispatch')
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            # authenticate 함수를 사용하여 사용자 인증
            user = authenticate(
                request=request,
                login_id=serializer.validated_data['login_id'],
                password=serializer.validated_data['userpwd']
            )

            if user is not None:
                # 인증 성공
                refresh = RefreshToken.for_user(user)
                return Response({
                    'status': 'success',
                    'message': '로그인 성공',
                    'login_id': user.login_id,
                    'token': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                }, status=status.HTTP_200_OK)

            # 인증 실패 시 메시지 반환
            return Response({
                'status': 'fail',
                'message': '로그인 정보가 잘못되었습니다.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        # 시리얼라이저 오류 반환
        return Response({
            'status': 'fail',
            'message': '유효하지 않은 요청입니다.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)