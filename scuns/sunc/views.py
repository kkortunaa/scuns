from django.shortcuts import render


def sunc(request):
    return render(request, 'sunc/index.html')
