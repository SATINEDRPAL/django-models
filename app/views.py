from django.shortcuts import render
from.forms import employeeform
# Create your views here.
def contact(request):
    form=employeeform(request.POST)
    if form.is_valid():
        form.save()
    return render(request,"contact.html")