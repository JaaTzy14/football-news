from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406405563',
        'name': 'Mirza Radithya Ramadhana',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
# Create your views here.
