from django.shortcuts import render
from .models import user_message
# Create your views here.
def message(request):
	if request.method == "POST":
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		address = request.POST.get('address','')
		message = request.POST.get('message','')
		user_message = message()
		user_message.name = name
		user_message.email = email
		user_message.address = address
		user_message.message = message
		user_message.save()


	return render(request,'liuyanban.html')