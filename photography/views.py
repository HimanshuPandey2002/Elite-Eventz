from django.shortcuts import render

def photo(request):
    return render(request, 'photography/photo.html')

