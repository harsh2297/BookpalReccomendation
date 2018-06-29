# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from predictBook import getTopReccomendation
import json

def index(request):

	if request.method == 'GET':
		uid = int(request.GET['id'])
		reccomendations = {}
		try:
			topReccomendations = getTopReccomendation(uid)
		except Exception as e:
			print(str(e))
			return HttpResponseBadRequest("Invalid BookID")
		reccomendations['similar_books'] = topReccomendations
	else:
		return HttpResponseBadRequest('Invalid parameters, refer the README.md for acceptable parameters')
	
	return JsonResponse(reccomendations)


def home(request):

	return HttpResponse("Book reccomendation system is running")