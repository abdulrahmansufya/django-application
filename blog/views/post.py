   
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..ai_content.service.summarize import summarize_post
from ..serializers import PostSerializer
from ..models import Post



#class PostViewSet(viewsets.ModelViewSet):
 #   queryset = Post.objects.all()
  #  serializer_class = PostSerializer


@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_posts(request):
    try:
        page = int(request.query_params.get('page', 1))
        limit = int(request.query_params.get('limit', 10))
        start = (page - 1) * limit
        end = start + limit

        posts = Post.objects.all()[start:end]
        serializer = PostSerializer(posts, many=True)
        return Response(
            {'posts': serializer.data, 'page': page, 'limit': limit}
        )
    except Exception:
        return Response(
            {"error":"An unexpected error occured."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

