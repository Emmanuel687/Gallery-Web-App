from django.shortcuts import render
from django.http import Http404
from .models import Location,Category,Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def welcome(request):
    images = Image.all_images()
    return render (request,'index.html',{"images":images})

def search(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,"search.html",{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request,"search.html",{"message":message})

def image(request,image_id):
    try:
        image = Image.get_image_by_id(image_id)

    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html",{"image":image})

def location(request):
    if 'location' in request.GET and request.GET["location"]:
        location = request.GET.get("location")
        searched_images = Image.filter_by_location(location)
        message = f"{location}"
        return render(request,"search.html",{"message":message,"images":searched_images})

    else:
        message = "select location to filter"
        return render(request,"search.html",{"message":message})