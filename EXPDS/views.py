from django.shortcuts import render

def index(request):
    context={
        'banner':'Compare shipping costs and track delivery status across multiple courier services.'
    }
    return render(request,'index.html',context)