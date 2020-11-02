from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
#views.py에 페이지를 항상 연동시킬 것.