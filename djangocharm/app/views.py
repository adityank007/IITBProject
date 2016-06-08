from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserInfoForm
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import addtheme, addsubject
from .queries import *
from app.leaderboard import *
from app.objects import *
from django.core.paginator import Paginator
from django.http import Http404


# Create your views here.
def base(request):
	if 'login' in request.POST:
		print(request.POST.dict)
		return user_login(request)
	else:
		print(request)
		return register(request)
def register(request):
	print("Entered register")
	print(request.POST.dict)
	print(request.GET.dict)
	context = RequestContext(request)
	if request.method == 'POST':
		print(request.POST.dict)
		user_form = UserForm(data=request.POST)
		profile_form=UserInfoForm(data=request.POST)

		if user_form.is_valid()*profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

		else:
			print(user_form.errors,profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserInfoForm()

	return render_to_response('home.html',{'user_form':user_form,'profile_form':profile_form, },context)


def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST.get("username","")
		password = request.POST.get("password","")
		print(username,password)
		user = authenticate(username = username ,password = password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponse("You are logged in")
			else:
				return HttpResponse(" Your account is disabled")
		else:
			print("Invalid login details : {0},{1} ".format(username,password))
			return HttpResponse("Invalid login details supplied")
	else:
		return render_to_response('home.html',{},context)


def themelist(request):

    #Fetch all projects from database and load in context
    context = {
        'theme_list' : addtheme.objects.all(),
    }

    return render(request, 'list.html', context)

def subjectlist(request):

    #Fetch all projects from database and load in context
    context = {
        'subject_list' : addsubject.objects.all(),
    }

    return render(request, 'list2.html', context)


def profile(request):
	list = get_dynamic_details('adi')
	context = {'list':list}
	return render(request,'profile.html',context)

def leaderboard_redirect(request):
	return redirect('/app/leaderboard/1')


def leaderboard(request,page_no):
	#generate leaderboard for all

	search_text = 'Input Text'
	context = {}
	start_time = datetime.datetime(1, 1, 1, 1, 1, 1, 1)
	end_time = datetime.datetime.now()
	generate_leaderboard(start_time, end_time, DynamicRecord.objects)
	users_list = LeaderBoard.sorted_objects()	
	if request.method == 'POST':
		search_text = request.POST.get('search_text')
		print search_text
		users_list = LeaderBoard.filter(users_list,search_text)
		print 'filtered'
	
	# 	for p in users_list:
	# 	    print p


	# for p in users_list:
	# 	print p

	p = Paginator(users_list,10)
	if p.num_pages > page_no:
		raise Http404('Out of Bounds')
	context = {'users': p.page(page_no).object_list}
	context['search_text']=search_text	
	return render(request,'LEADERBOARD.html',context)



