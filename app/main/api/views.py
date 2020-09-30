from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from app.main.api.serializers import CreatePostSerializer


class CreatePostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):

        feedback = {}
        data = self.request.data

        images = dict((request.data))['profile_picture']

        while("" in images):
            images.remove("")

        if len(images) == 0:
            feedback['error'] = 'image file is required'
            return Response(data=feedback, status=status.HTTP_400_BAD_REQUEST)

        if len(images) > 1:
            feedback['error'] = 'maximum file to upload is 1'
            return Response(data=feedback, status=status.HTTP_400_BAD_REQUEST)

        serializer = CreatePostSerializer(data=data)

        if serializer.is_valid():
            windowshoppi_post = serializer.save()
            feedback = 'success'
            return Response(feedback, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
