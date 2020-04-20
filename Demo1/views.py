from django.shortcuts import render
from .models import Demo
from Demo1 import form




# Create your views here.

def Fin(request):

    dt=Demo.objects.all()
    msg={'dt':dt}
    return render(request,"/Users/Huzefa/PycharmProjects/django proj/templates/index.html",context={'dt':dt})

def Register(request):

    form_data= form.Reg(request.POST or None)

    if form_data.is_valid():
        st=Demo()
        st.first_name=form_data.cleaned_data['first_name']
        st.last_name = form_data.cleaned_data['last_name']
        st.address = form_data.cleaned_data['address']
        st.save()

    context={'form_reg':form_data}
    return render(request,"/Users/Huzefa/PycharmProjects/django proj/templates/base.html",context)
