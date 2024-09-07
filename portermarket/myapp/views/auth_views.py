from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from ..models import User
from ..serializers import UserSerializer

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
