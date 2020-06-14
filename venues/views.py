from django.shortcuts import render

def venue(request):
    return render(request, 'venue/venue01.html')
