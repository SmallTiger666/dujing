from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth import authenticate,login
# Create your views here.
# 
from django.contrib.auth.backends import ModelBackend
#
from .models import UserProfile
#
class CustomBackend(ModelBackend):
	def authenticate(self,username=None,password=None,**kwargs):
		try:
			user=UserProfile.objects.get(username=username)
			if user.check_password(password):
				return user
		except Exception as e:
			return None



def user_login(request):


	if request.method == "POST":
		user_name = request.POST.get("username","")
		pass_word = request.POST.get("password","")
		user = authenticate(username=user_name,password=pass_word)
		if user is not None:
			login(request,user)
			return render(request,"index.html")

		else:
			return render(request,"login.html",{})


	elif request.method == "GET":
		return render(request,"login.html",{})
