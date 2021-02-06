from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    context_dict = {'boldmessage':"Crunchy,creamy,cookie,candy,cupcake!"}
    return render(request,'rango/index.html', context=context_dict)
    return HttpResponse("Rango says hey there partner! <br/> < a href='/rango/about/ '>About</ a>")
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)
def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Jianhua Hua.'}
    return render(request,'rango/about.html', context=context_dict)
    return HttpResponse("Rango says here is the about page！< a href='/rango/>Index</ a>")
def show_category(request, category_name_slug):
    context_dict = {}
    category = Category.objects.get(slug=category_name_slug)
    pages = Page.objects.filter(category=category)
    context_dict['pages'] = pages
    context_dict['category'] = category
    return render(request, 'rango/category.html', context=context_dict)
