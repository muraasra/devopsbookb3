from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet


router = DefaultRouter()
router.register(r"author", AuthorViewSet)
router.register(r'books', BookViewSet)


urlpatterns = [
    path('',include(router.urls))
    # path('hello/', index, name='index'),
    # path('book_list/', book_list, name='book_list'),
]
