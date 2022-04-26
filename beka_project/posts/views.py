from django.shortcuts import render, redirect
from .forms import PostCreate
from django.http import HttpResponse
from .models import*
from posts.models import Posts,RegUser
from .forms import CreateUser
# Create your views here.
def createuser(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('create_user')
            except:
                form.add_error(None, 'Failed attempt to create user')
    else:
        form = CreateUser()
    return render(request, 'posts/registration.html', {'form': form})
def discount(request):
    return render(request, 'posts/discount.html',{})
def services(request):
    return render(request, 'posts/services.html',{})
def firstPage(request):
    return render(request, 'posts/firstPage.html',{})
def places(request):
    return render(request, 'posts/places.html',{})
def index2(request):
    table= Table.objects.all()
    actor= Actor.objects.all()
    return render(request, 'posts/index2.html',{'title':'index2',
                                                'actor':actor,
                                                'table':table})
def Dimash(request):
    actor= Actor.objects.all()
    table= Table.objects.all()
    return render(request, 'posts/Dimash.html',{'title':'Dimash',
                                                'actor':actor,
                                                'table':table})
def index(request):
    all_posts=Posts.objects.all()
    actor= Actor.objects.all()
    return render(request, 'posts/index.html',{'posts':all_posts,'actor':actor})
def upload(request):
    upload = PostCreate()
    if request.method == 'POST':
        upload = PostCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""Error, reload on <a href = "{{url : 'index'}}">reload</a>""")
    else:
        return render(request, 'posts/upload_form.html',{'upload_form':upload})
def update_post(request, posts_id):
    post_id = int(post_id)
    try:
        post_sel = Posts.objects.get(id = post_id)
    except Posts.DoesNotExist:
        return redirect('index')
    post_form = PostCreate(request.POST or None, instance = post_sel)
    if post_form.is_valid():
        post_form.save()
        return redirect('index')
    return render(request, 'posts/upload_form.html',{'upload_form':post_form})
def delete_post(request, post_id):
    post_id=int(post_id)
    try:
        post_sel = Posts.objects.get(id = post_id)
    except Posts.DoesNotExist:
        return redirect('index')
    post_sel.delete()
    return redirect('index')                                         

