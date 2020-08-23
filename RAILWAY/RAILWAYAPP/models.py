from django.db import models
class TCData(models.Model):
	fullname=models.CharField(max_length=50)
	emailid=models.CharField(max_length=100)
	password=models.CharField(max_length=30)
	confirm=models.CharField(max_length=30)
	doj=models.CharField(max_length=30)
	gender=models.CharField(max_length=30)
class AddtrainData(models.Model):
	trainno=models.CharField(max_length=6)
	trainname=models.CharField(max_length=50)
	ac2tier=models.CharField(max_length=30)
	ac3tier=models.CharField(max_length=30)
	sleeper=models.CharField(max_length=30)
class TrainrouteData(models.Model):
	trainno=models.CharField(max_length=6)
	trainfrom=models.CharField(max_length=50)
	trainto=models.CharField(max_length=30)
	route=models.CharField(max_length=30)
	departuretime=models.CharField(max_length=30)
	arrivaltime=models.CharField(max_length=30)
class PassengerData(models.Model):
	name=models.CharField(max_length=50)
	age=models.CharField(max_length=50)
	gender=models.CharField(max_length=30)
	concession=models.CharField(max_length=30)
