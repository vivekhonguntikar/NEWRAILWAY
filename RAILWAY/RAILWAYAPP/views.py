from django.shortcuts import render
from RAILWAYAPP.models import TCData,AddtrainData,TrainrouteData,PassengerData
def TCSave(request):
	if request.method=="POST":
		t=TCData()
		t.fullname=request.POST.get("txtfullname","")
		t.emailid=request.POST.get("emailid","")
		t.mobile=request.POST.get("mobile","")
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
	try:
		if request.method=="POST":
			pid=request.POST.get("tcid","");
			data=TCData.objects.get(id=pid)	
			data.delete()
			newdata=TCData.objects.all()
			return render(request,"RAILWAYAPP/tcregisterdisplay.html",{"data":newdata,"msg":"Record Deleted"})
		else:
			data=TCData.objects.all()
			return render(request,"RAILWAYAPP/tcregisterdisplay.html",{"data":data})
	except Exception as e:
		raise
		
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
		p.idproof=request.POST.get("idproof","")
		p.doj=request.POST.get("doj","")
		p.trainid=request.POST.get("trainnumber","")
		p.source=request.POST.get("source","")
		p.destination=request.POST.get("destination","")
		p.seatnumber=request.POST.get("txtseatnumber","")
		p.seatstatus=request.POST.get("seatstatus","")
		p.statusnumber=request.POST.get("txtstatusnumber","")
		p.ticketkey=request.POST.get("txtkey","")
		p.ttapproval="1"
		p.pnrnumber=request.POST.get("pnrnumber","")
		p.save()
		return render(request,"RAILWAYAPP/passengerlist.html",{"msg":"Passenger list added"})
	else:
		return render(request,"RAILWAYAPP/passengerlist.html")

def passengerlistdisplay(request):
	if request.method=="POST":
		pid=request.POST.get("pid","");
		data=PassengerData.objects.get(id=pid)	
		data.delete()
		newdata=PassengerData.objects.all()
		return render(request,"RAILWAYAPP/passengerlistdisplay.html",{"data":newdata})
	else:
		data=PassengerData.objects.all()
		return render(request,"RAILWAYAPP/passengerlistdisplay.html",{"data":data})

def tcpassengerlistdisplay(request):
	if request.method=="POST":
		pid=request.POST.get("pid","");
		data=PassengerData.objects.get(id=pid)	
		data.delete()
		newdata=PassengerData.objects.all()
		return render(request,"RAILWAYAPP/tcpassengerlistdisplay.html",{"data":newdata})
	else:
		data=PassengerData.objects.all()
		return render(request,"RAILWAYAPP/tcpassengerlistdisplay.html",{"data":data})

def loginpage(request):
	try:
		if request.method=="POST":
			username=request.POST.get("mobilenumber","")
			password=request.POST.get("password","")
			if(username=="9876543210" and password=="9876543210"):
				return render(request,"RAILWAYAPP/adminhome.html")
			else:
				data=TCData.objects.get(mobile=username,password=password)
				if(data.mobile==username and data.password==password):
					return render(request,"RAILWAYAPP/tchome.html")
				else:
					return render(request,"RAILWAYAPP/login.html")
		else:	
			return render(request,"RAILWAYAPP/login.html")
	except Exception as e:
			return render(request,"RAILWAYAPP/login.html",{"msg":"Invalid Mobile Number or Password"})
def adminhome(request):
	return render(request,"RAILWAYAPP/adminhome.html")
def tchome(request):
	if request.method=="POST":
		submit=request.POST.get("btnsubmit","");
		pid=request.POST.get("pid","");
		key=request.POST.get("ticketkey","");
		if submit=="Occupied":
			data=PassengerData.objects.get(id=pid)
			data.ttapproval=100
			data.save()
			data=PassengerData.objects.all()
			return render(request,"RAILWAYAPP/tchome.html",{"data":data,"msg":"Ticket Approved"})
		else:
			canceldata=PassengerData.objects.get(id=pid)
			cseatnumber=0
			ccoachtype=""
			if canceldata:
				cseatnumber=canceldata.seatnumber
				ccoachtype=canceldata.coachtype
				canceldata.seatstatus="CNCL"
				canceldata.seatnumber=cseatnumber
				canceldata.ttapproval="100"
				canceldata.save()
			pdata=PassengerData.objects.all()
			for pp in pdata:
				if(pp.statusnumber=="1" and pp.seatstatus=="RAC"):
					pp.seatstatus="CNF"
					pp.seatnumber=cseatnumber
					pp.coachtype=ccoachtype
					pp.statusnumber="1"
				elif(pp.statusnumber=="2" and pp.seatstatus=="RAC"):
					pp.seatstatus="CNF"
					pp.statusnumber="1"			
				else:
					i=1
					pp.statusnumber=i
					i=i+1
				pp.save()
			data=PassengerData.objects.all()
			return render(request,"RAILWAYAPP/tchome.html",{"data":data,"msg":"Ticket Cancelled & Reassigned"})
	else:
		data=PassengerData.objects.all()
		return render(request,"RAILWAYAPP/tchome.html",{"data":data})
