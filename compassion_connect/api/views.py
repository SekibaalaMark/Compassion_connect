from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from rest_framework.permissions import IsAuthenticated


class RegionalDirectorRegisterView(APIView):
    def post(self, request):
        serializer = RegionalDirectorRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Regional Director registered successfully.",
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "role":user.role
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class CountryDirectorRegisterView(APIView):
    def post(self, request):
        serializer = CountryDirectorRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Country Director registered successfully.",
                "user_id": user.id,
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PFRegisterView(APIView):
    def post(self, request):
        serializer = PFRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "PF registered successfully.",
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "role":user.role
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PDRegistrationAPIView(GenericAPIView):
    serializer_class = PDRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Project Director registered successfully.",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "project_code":user.project_code,
                    "cluster":user.cluster
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SDRRegisterView(APIView):
    def post(self, request):
        serializer = SDRRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "CDO SDR registered successfully.",
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "role":user.role
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class HealthRegisterView(APIView):
    def post(self, request):
        serializer = HealthRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "CDO HEALTH registered successfully.",
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "role":user.role
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class EmailVerifyAPIView(APIView):
    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # Generate JWT tokens for the authenticated user
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                "message": "successful.",
                "user_id": user.id,
                "username": user.username,
                "role": user.role,
                "email": user.email,
                "access": access_token,
                "refresh": refresh_token,
                "success": True,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PostCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreatePostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # author is set inside serializer's create()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CommentCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateCommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            comment = serializer.save()  # author set in serializer
            return Response({
                "id": comment.id,
                "post": comment.post.id,
                "author": comment.author.username,
                "content": comment.content,
                "created_at": comment.created_at
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class PostCommentsListAPIView(APIView):
    def get(self, request, post_id, format=None):
        comments = Comment.objects.filter(post_id=post_id).order_by('-created_at')
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






class PostListByRoleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        posts = Post.objects.filter(author__role=user.role).order_by('-created_at')
        serializer = PostWithCommentsSerializer(posts, many=True)
        return Response(serializer.data)





class LikePostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        user = request.user
        try:
            post = Post.objects.get(id=post_id)
            Like.objects.get_or_create(post=post, user=user)
            return Response({'message': 'Liked'}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)


class UnlikePostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        user = request.user
        try:
            post = Post.objects.get(id=post_id)
            like = Like.objects.filter(post=post, user=user)
            if like.exists():
                like.delete()
                return Response({'message': 'Unliked'}, status=status.HTTP_200_OK)
            return Response({'error': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)




from rest_framework.exceptions import NotFound, PermissionDenied

class PostDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound("Post not found.")

        # Only allow the author to delete
        if post.author != request.user:
            raise PermissionDenied("You can only delete your own posts.")

        post.delete()
        return Response({"message": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
