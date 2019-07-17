from rest_framework import viewsets # 요거는 아직~!
from .models import Post
from .serializer import PostSerializer

# serializer에서 정의한 ModelSerializer를 바탕으로 ViewSet 완성하기
# queryset, serializer_class만 적어주면 됨
# 직접 코드 볼 것 권장

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer