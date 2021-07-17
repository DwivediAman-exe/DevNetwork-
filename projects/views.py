from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
	return HttpResponse('here is the project page')

def project(request, pk):
	return HttpResponse('single project' + ' ' + pk)