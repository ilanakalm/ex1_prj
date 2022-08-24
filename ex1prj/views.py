from django.shortcuts import render
def home(request):
    return render(request,"home.html")

def reverse(request):
    get_text=request.GET['message']
    reverse_text=get_text[::-1]



    return render(request,"reverse.html",{'reversetext':reverse_text,'gettext':get_text})