from django.urls import path
# from .views import CourseList,CourseDetail,CourseDelete
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet


router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
    # path('courses/',CourseList.as_view(),name='courses'),
    # path('course-detail/<int:pk>/',CourseDetail.as_view(),name='course-detail'),
    # path('course-delete/<int:pk>/',CourseDelete.as_view(),name='course-delete'),
    # path('course/<int:pk>/',CourseUpdateAPIView.as_view(),name='course'),
    # path('course-delete/<int:pk>/',CourseDeleteAPIView.as_view(),name='delete'),
# ]