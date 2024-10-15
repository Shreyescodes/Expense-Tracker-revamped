# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, World!")

from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("Hello, World!")

def api_hello(request):
    return JsonResponse({"message": "Hello from API!"})