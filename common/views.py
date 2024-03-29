from django.shortcuts import render

# from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.


# def index(requests):
#     members = Member.objects.all()




def index(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    abouts =  About.objects.all()
    services = Service.objects.all()
    posts = Post.objects.all()
    portfolios = Portfolio.objects.all()
    categories = Category.objects.all()
    print(abouts)
    context = {"profile":profile,
               "skills":skills ,
                "abouts":abouts,
                "services":services,
                "posts":posts,
                "portfolios":portfolios,
                "categories":categories,
                 }
    return  render(request, "index.html", context)

def about(request):
    return render(request, "about-us.html")


def blog(request):
    posts = Post.objects.all()

    if request.method == "POST":
        search = request.POST.get("search")
        if search:
            posts = posts.filter(title__icontains=search)

    context = {"posts":posts}
    return render(request, "blog.html", context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, id=pk)

    return render(request, "single-blog.html", {"post":post})
    
    

   

def portfolio(request):
    return render(request, "portfolio.html")