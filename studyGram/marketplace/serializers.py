from rest_framework import serializers

from .models import product, photo_products, product_photo, level, subject, topic, subject_topic, \
    level_subject_topic_product, raiting_products, raitings_to_product


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['product_id', 'title', 'thumbnail', 'description', 'price', 'profile_id', 'tags']


class photo_productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = photo_products
        fields = [
            'id_photo',
            'photo_file',
            'name'
        ]


class product_photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_photo
        fields = [
            'id_product_photo',
            'id_product',
            'id_photo'

        ]


class levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = level
        fields = ['id_level',
                  'name',
                  'slug']


class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = ['id_subject',
                  'name',
                  'slug']


class topicSerializer(serializers.ModelSerializer):
    class Meta:
        model = topic
        fields = [
            'id_topic',
            'slug',
            'name'
        ]


class subject_topicSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject_topic
        fields = [
            'id_subject_topic',
            'id_topic',
            'id_subject'
        ]


class level_subject_topic_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = level_subject_topic_product
        fields = [
            'id_level_subject_product',
            'id_level',
            'id_subject_topic',
            'id_product'
        ]


class raiting_productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = raiting_products
        fields = [
            'id_raiting',
            'value_text',
            'value_number',
            'id_user'
        ]


class raitings_to_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = raitings_to_product
        fields = [
            'raiting_product',
            'id_product'
            'id_raiting'
        ]
