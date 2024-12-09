from django.shortcuts import render

# Create your views here.


def ifcondition(request):
    d={'name':'Sreerag','age':25}
    return render(request,'ifcondition.html',context=d)

def ifelse(request):
    d={'name':'Sreerag','age':16}
    return render(request,'ifelse.html',context=d)

def ifelif(request):
    d={'name':'Sreerag','age':25}
    return render(request,'ifelif.html',context=d)

def nested(request):
    d={'name':'Sreerag','age':60}
    return render(request,'nestedif.html',context=d)

def forloop(request):
    d={'name':'Sreerag','age':25}
    return render(request,'forloop.html',context=d)














