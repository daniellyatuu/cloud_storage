from rest_framework import serializers
from app.main.models import Customer


class CreatePostSerializer(serializers.ModelSerializer):
    # filename = serializers.ListField(
    #     child=serializers.ImageField(allow_empty_file=False))

    class Meta:
        model = Customer
        fields = ['name', 'age', 'profile_picture']

    # def create(self, validated_data):
    #     bussiness = self.validated_data['bussiness']
    #     caption = self.validated_data['caption']
    #     filename = validated_data.pop('filename')

    #     # save post
    #     windowshoppi_post = BussinessPost.objects.create(
    #         bussiness=bussiness,
    #         caption=caption,
    #     )

    #     # save post images
    #     # image_list = []
    #     # for image in filename:
    #     #     # resizedImage = self.compress(image)
    #     #     image_list.append(
    #     #         PostImage(post=windowshoppi_post, filename=image))
    #     # PostImage.objects.bulk_create(image_list)

    #     for image in filename:
    #         PostImage.objects.create(post=windowshoppi_post, filename=image)

    #     return windowshoppi_post
