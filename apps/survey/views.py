from django.shortcuts import render, redirect

def index(request):
	request.session['count']=request.session.get('count',1)
	return render(request, "survey/index.html")

def process(request):
	request.session['full_name']=request.POST['name']
	request.session['location']=request.POST['location']
	request.session['language']=request.POST['language']
	request.session['comments']=request.POST['comment']
	request.session['count']+=1
	return redirect('/result')

def success(request):
	return render(request, "survey/success.html")

def reset(request):
	return redirect('/')
