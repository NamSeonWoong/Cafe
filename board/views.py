from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import P,C
from .forms import PForm,CForm
# Create your views here.
@login_required
def index(request):
    ps = P.objects.all()
    context={
        'ps':ps
    }
    return render(request,'board/index.html',context)
    
def search(request):
    ps = P.objects.all()
    search = request.GET.get('search')
    context={
        'search':search,
        'ps':ps
    }
    return render(request,'board/search.html',context)

@login_required
def create(request):
    if request.method == "POST":
        form = PForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.author = request.user
            p.save()
            return redirect('board:index')
    
    else:
        form = PForm()
    context= {
        'form':form
    }
    return render(request,'board/form.html',context)

@login_required
def detail(request, id):
    p = get_object_or_404(P,id=id)
    cform = CForm()
    context={
        'p':p,
        'cform':cform
    }
    return render(request,'board/detail.html',context)

@login_required
def update(request, id):
    p = get_object_or_404(P, id= id)
    if request.user == p.author:
        if request.method =="POST":
            form = PForm(request.POST, instance=p)
            if form.is_valid():
                form.save()
                return redirect('board:detail', id)
        else:
            form = PForm(instance=p)
        context={
            'form':form
        }
        return render(request,'board/form.html', context)
    return redirect('board:detail', id)

@login_required
def delete(request, id):
    p = get_object_or_404(P, id= id)
    if request.user == p.author:
        p.delete()
    return redirect('board:index') 

@login_required
def create_c(request, id):
    if request.method =="POST":
        cform = CForm(request.POST)
        if cform.is_valid():
            c = cform.save(commit=False)
            c.author = request.user
            c.p = get_object_or_404(P, id=id)
            c.save()
            return redirect('board:detail',id)

    return redirect('board:detail',id)

@login_required
def delete_c(request, p_id, c_id):
    c = get_object_or_404(C, id=c_id)
    if c.author == request.user:
        c.delete()
    return redirect('board:detail', p_id) 

@login_required
def like(request,id):
    p = get_object_or_404(P,id=id)
    user = request.user
    if user in p.like_users.all():
        p.like_users.remove(user)
    else:
        p.like_users.add(user)

    return redirect('board:detail',id)

@login_required
def like_c(request, p_id, c_id):
    c = get_object_or_404(C,id=c_id)
    user = request.user
    if user in c.like_users_c.all():
        c.like_users_c.remove(user)
    else:
        c.like_users_c.add(user)

    return redirect('board:detail', p_id)


