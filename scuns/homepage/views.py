from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from homepage.models import User
from datetime import datetime
from .forms import UserForm

def homepage(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        

    context = {
        'form': form
    }
    
    return render(request, "homepage/homepage.html", context)

def fix_query_set(request):
    profiles = User.objects.values_list('profile')
    context = {'my_objects': profiles}
    return render(request, 'homepage.html', context)

def scuns_list(request):
    sort_by = request.GET.get('sort', 'surname')
    allowed_sorts = ['surname', 'name', 'name2', 'avg_oge_score', "avg_score", "avg_score_of_exam"]
    if sort_by not in allowed_sorts:
        sort_by = 'surname'
    users = User.objects.order_by(sort_by)
    paginator = Paginator(users, 5)

    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)

    context = {
    'page_obj': page_obj, 
    'current_sort': sort_by,
    'allowed_sorts': allowed_sorts,
    }
    return render(request, 'homepage/scuns_list.html', context)

def delete_user(request, pk):
    # Получаем объект модели или выбрасываем 404 ошибку.
    instance = get_object_or_404(User, pk=pk)
    # В форму передаём только объект модели;
    # передавать в форму параметры запроса не нужно.
    form = UserForm(instance=instance)
    context = {'form': form}
    # Если был получен POST-запрос...
    if request.method == 'POST':
        # ...удаляем объект:
        instance.delete()
        # ...и переадресовываем пользователя на страницу со списком записей.
        return redirect('homepage:list')
    # Если был получен GET-запрос — отображаем форму.
    return render(request, 'homepage/homepage.html', context)