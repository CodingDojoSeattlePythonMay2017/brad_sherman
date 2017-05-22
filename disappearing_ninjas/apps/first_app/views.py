from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def ninja(request):
    return render(request, 'first_app/ninja.html')

def color(request, color):
    print (color)
    if color == "blue":
        turtle = "leonardo"
    elif color == "purple":
        turtle = "donatello"
    elif color == "orange":
        turtle = "michelangelo"
    elif color == "red":
        turtle = "raphael"
    else:
        turtle = "notapril"
    print (turtle)
    context = {
        "color": turtle
    }
    print (context)
    return render(request, 'first_app/color.html', context)
