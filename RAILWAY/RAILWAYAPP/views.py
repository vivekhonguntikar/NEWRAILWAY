from django.shortcuts import render
from RAILWAYAPP.models import TCData,AddtrainData,TrainrouteData,PassengerData
def TCSave(request):
	if request.method=="POST":
		t=TCData()
		t.fullname=request.POST.get("txtfullname","")
		t.emailid=request.POST.get("emailid","")
		t.password=request.POST.get("password","")
		t.confirm=request.POST.get("password","")
		t.doj=request.POST.get("dob","")
		t.gender=request.POST.get("gender","")
		t.save()
		return render(request,"RAILWAYAPP/tcregister.html",{"msg":"TC Register"})
	else:
		return render(request,"RAILWAYAPP/tcregister.html")


# Create your views here.
def registerdisplay(request):
	data=TCData.objects.all()
	return render(request,"RAILWAYAPP/tcregisterdisplay.html",{"data":data})

def AddtrainSave(request):
	if request.method=="POST":
		a=AddtrainData()
		a.trainno=request.POST.get("trainnumber","")
		a.trainname=request.POST.get("name","")
		a.ac2tier=request.POST.get("ac2tiernumber","")
		a.ac3tier=request.POST.get("ac2tiernumber","")
		a.sleeper=request.POST.get("sleepnumber","")
		a.save()
		return render(request,"RAILWAYAPP/addtrain.html",{"msg":"Train details added"})
	else:
		return render(request,"RAILWAYAPP/addtrain.html")

def addtraindisplay(request):
	data=AddtrainData.objects.all()
	return render(request,"RAILWAYAPP/addtraindisplay.html",{"data":data})
	
def TrainrouteSave(request):
	if request.method=="POST":
		r=TrainrouteData()
		r.trainno=request.POST.get("trainnumber","")
		r.trainfrom=request.POST.get("cityname","")
		r.trainto=request.POST.get("city","")
		r.route=request.POST.get("address","")
		r.departuretime=request.POST.get("departuretime","")
		r.arrivaltime=request.POST.get("arrivaltime","")
		r.save()
		return render(request,"RAILWAYAPP/trainroute.html",{"msg":"Train route details added"})
	else:
		return render(request,"RAILWAYAPP/trainroute.html")

def trainroutedisplay(request):
	data=TrainrouteData.objects.all()
	return render(request,"RAILWAYAPP/trainroutedisplay.html",{"data":data})
	
def PassengerSave(request):
	if request.method=="POST":
		p=PassengerData()
		p.name=request.POST.get("passengername","")
		p.age=request.POST.get("passengerage","")
		p.gender=request.POST.get("gender","")
		p.concession=request.POST.get("concession","")
		p.save()
		return render(request,"RAILWAYAPP/passengerlist.html",{"msg":"Passenger list added"})
	else:
		return render(request,"RAILWAYAPP/passengerlist.html")

def passengerlistdisplay(request):
	data=PassengerData.objects.all()
	return render(request,"RAILWAYAPP/passengerlistdisplay.html",{"data":data})
