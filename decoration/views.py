from django.shortcuts import render

def dec(request):
    return render(request, 'decoration/decoration.html')
