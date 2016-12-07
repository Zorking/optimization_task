from django.shortcuts import render
# from .rnd_opt import rnd_opt
# Create your views here.
def home(request):
    # if request.method == 'POST':
        # output = rnd_opt()
    return render(request, 'home.html', {})