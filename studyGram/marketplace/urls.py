from django.urls import path,include
from rest_framework import routers
from . import views
from .views import product_photoViewSet, photo_productsViewSet, \
    subjectViewSet, topicViewSet, subject_topicViewSet, \
    level_subject_topic_productViewSet, raiting_productsViewSet, \
    raitings_to_productViewSet, ProductViewSet, levelViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'photo_products', photo_productsViewSet)
router.register(r'product_photo', product_photoViewSet)
router.register(r'level', levelViewSet)
router.register(r'subject', subjectViewSet)
router.register(r'topic', topicViewSet)
router.register(r'subject_topic', subject_topicViewSet)
router.register(r'level_subject_topic', level_subject_topic_productViewSet)
router.register(r'raiting_products', raiting_productsViewSet)
router.register(r'raitings_to_product', raitings_to_productViewSet)

urlpatterns = [

    # path('', views.start, name='start'),
    path('api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))

]
