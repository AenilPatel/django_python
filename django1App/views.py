from django.shortcuts import render
from .models import student
from .forms import regForm,logForm
from django.http import *

# Create your views here.
def reg_page(request):
	c1=regForm()
	data={'form':c1}
	return render(request,"django1App/register.html",data)

def log_page(request):
	c2=logForm()
	data={'form':c2}
	return render(request,"django1App/login.html",data)

def reg(request):
	name1=request.POST.get("name")
	pass1=request.POST.get("password")

	obj=student(name=name1,password=pass1)
	obj.save()

	c2=logForm()
	data={'form':c2}
	return render(request,"django1App/login.html",data)

def log(request):
	name1=request.POST.get("name")
	pass1=request.POST.get("password")

	list1=student.objects.all()

	for i in list1:
		if(i.name==name1 and i.password==pass1):
			context={'name':name1,'db':list1}
			return render(request,"django1App/home.html",context)

def delete(request):
	name1=request.GET.get("name")

	list1=student.objects.all()

	for i in list1:
		if(name1==i.name):
			l1=student.objects.filter(name=name1)
			l1.delete()
			return HttpResponse("Row Deleted")

def update(request):
	name1=request.GET.get("name")

	list1=student.objects.all()

	for i in list1:
		if(i.name==name1):
			context={'name':i.name,'password':i.password}
			return render(request,"django1App/update.html",context)

def updateNew(request):
	name1=request.POST.get("name")
	pass1=request.POST.get("password")

	list1=student.objects.all()

	for i in list1:
		if(i.name==name1):
			l1=student.objects.get(name=name1)
			l1.name=name1
			l1.password=pass1
			l1.save()
			return HttpResponse("Rows Updated")