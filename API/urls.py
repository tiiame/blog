from django.urls import path
from.views import *


urlpatterns = [
    path("profile/", ProfileData.as_view()),
    path("service/", get_service_data),
    path("about/", AboutData.as_view()),
    path("skill/", SkillsAPIView.as_view()),
    path("category/",CategoryListAPIView.as_view()),
    path("post/",PostListAPIView.as_view()),
    path("portfolio/", PortfolioListAPIView.as_view()),
    path("blog-create/", BlogCreateAPIView.as_view()),
    path("blog/<int:pk>/", BlogUpdateAPIView.as_view()),
    path("blogs/", BlogListAPIView.as_view()),
    path("about/", AboutAPIView.as_view()),
    path("category/", CategoryListAPIView.as_view()),
    path("portfolio/", ListCreateAPIView.as_view()),
    
]