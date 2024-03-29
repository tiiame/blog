from django.shortcuts import render

# Create your views here.
from common.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView , ListCreateAPIView,CreateAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . import permission

#function based
@api_view(['GET', 'POST'])
def get_profile_date(requests):

    if requests.method == 'POST':
        print(requests.data)
        print(type(requests.data))

    profile = Profile.objects.first()
    data = {
        'image':str(profile.image),
        'full_name': profile.full_name,
        'bio': profile.bio,
    }
    return Response(data=data,status=200)





#class based
class ProfileData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,format=None):
        profile = Profile.objects.first()
        data = {
            'image':str(profile.image),
            'full_name': profile.full_name,
            'bio': profile.bio,
        }
        return Response(data=data,status=200)
    
    
    def post(self, request,format=None):
        print(request.data)
        return Response(status=200)
    

@api_view(['GET','POST'])
def get_service_data(request):

    if request.method == 'POST':
        print(request.data)
        print(type(request.data))

    service = Service.objects.first()
    data = {
        'title': service.title,
        'icon': service.icon,
        'description': service.description
    }
    return Response(data=data,status=200)   

class ServiceData(APIView):
    permission_classes = [IsAuthenticated,]
    

    def get(self, request,format=None):
        service = Service.objects.first()
        data = {
            'title': service.title,
            'icon': service.icon,
            'description': service.description
        }
        return Response(data=data,status=200)
    
    def post(self, request,format=None):
        print(request.data)
        return Response(status=200)



class AboutData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,format=None):
        about = About.objects.first()
        data = {
            'experience': about.experience,
            'total_projects': about.total_projects,
            'total_users': about.total_users,
          'salary': about.salary,
        }
        return Response(data=data,status=200)
    
    def post(self, request,format=None):
        print(request.data)
        return Response(status=200)


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = ('title', 'percentage')

class PortfolioListCreateAPIView(ListCreateAPIView):
    class Meta:
        model = Portfolio
        fields = ('title', 'description', 'image', 'link', 'used_tools', 'category', 'complated_at')

@api_view()
def get_skills(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(instance=skills, many=True)
    return Response(serializer.data)
    

class SkillsAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(instance=skills, many=True)
        return Response(serializer.data)
#*******************************************************************
    


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   

    def post(self, request, format=None):
        print(request.data)
        return Response(status=200)
    

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'image', 'description', 'title', 'count_views','id',)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, format=None):
        print(request.data)
        return Response(status=200)



class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('title', 'description', 'image','link','used_tools','category','complated_at')


class PortfolioListAPIView(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def post(self, request, format=None):
        print(request.data)
        return Response(status=200)

#---------------------------------------------------
from .serializers import SkillSerializer


class SkillListAPIView(ListAPIView):
    
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class BlogCreateAPIView(APIView):
    queryset = Blog.objects.all()

    def post(self, request):
        serializer = BlogCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(data=serializer.data, status=201)
    
      
    
class BlogUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer
    lookup_field_name = 'pk'


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ('title')
    permission_classes = [IsAdminUser]
    filterset_fields = ('category', )

    serializer_class = BlogListSerializer


    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)
    
    
class AboutAPIView(APIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        about = About.objects.first()
        data = {
            'experience': about.experience,
            'total_projects': about.total_projects,
            'total_users': about.total_users,
         'salary': about.salary,
        }
        return Response(data=data,status=200)
    
class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permission.CustomPermission]    
    

# class PortfolioListCreateAPIView(ListCreateAPIView):
#     serializer_class = PortfolioSerializer
#     queryset = Portfolio.objects.all()
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         portfolio = Portfolio.objects.first()
#         data = {
#             'title': portfolio.description,
#             'description': portfolio.description,
#             'image': portfolio.image,
#             'link': portfolio.link,
#             'used_tools': portfolio.used_tools,
#             'category': portfolio.category,
#             'complated_at': portfolio.complated_at,
#         }
#         return Response(data=data,status=200)



# class PortfolioListCreateAPIView(ListCreateAPIView):
#     permission_classes = [IsAuthenticated,]

#     def get(self,request):
#         profile = Profile.objects.first()
#         data = {
#             'title': profile.full_name,
#             'description': profile.bio,
#             'image': str(profile.image),
#             'link': profile.link,
#             'used_tools': [skill.title for skill in profile.used_tools.all()],
#             'category': profile.category.name,
#             'complated_at': profile.complated_at
#         }
#         return Response(data=data,status=200)
    



# class PortfolioDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Portfolio.objects.all()
#     serializer_class = PortfolioSerializer
#     permission_classes = [IsAuthenticated]








































