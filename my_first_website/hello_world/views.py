from django.shortcuts import render

# Create your views here.

# Renders file when page is loaded
def hello_world(request):
    return render(request, "hello_world.html", {})