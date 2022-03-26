from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Category, Location, Image


# Create your views here.
def welcome(request):
    try:
        category = Category.objects.all()
        location = Location.objects.all()
        images = Image.objects.all()
    except:
        raise Http404()

    return render(request, 'index.html', {"location": location,"category":category,"images":images})

def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_name = Image.search_by_name(search_term)
        message = f"{search_term}"
        print(searched_name)

        return render(request, 'search.html', {"message": message, "image": searched_name})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})



