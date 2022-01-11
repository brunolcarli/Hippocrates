from django.shortcuts import render
from django.conf import settings

def index(request):
	"""Homepage"""
	host = settings.BACKEND['host']
	port = settings.BACKEND['port']
	env_ref = settings.ENV_REF
	return render(request, 'pages/index.html')