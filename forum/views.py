from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse
from .models import *
from .forms import *

class IndexView(generic.ListView):
	template_name = 'forum/index.html'
	context_object_name = 'threads'

	def get_queryset(self):
		return Thread.objects.all()

def newThread(request):
	if request.method == 'POST':
		form = NewThreadForm(request.POST)
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			thread = Thread()
			thread.title = form.cleaned_data["title"]
			thread.authorUserName = form.cleaned_data["user"]
			thread.save()

			return HttpResponseRedirect(reverse("forum:thread", args=[thread.pk]))

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NewThreadForm()

	return render(request, 'forum/newThread.html', {'form': form})

def newPost(request):
	if request.method == 'POST':
		thread = Thread.objects.get(pk=request.POST['threadID'])
		post = Post()
		post.thread = thread
		post.userName = request.POST['user']
		post.content = request.POST['reply']
		post.save()

	return HttpResponseRedirect(reverse("forum:thread", args=[thread.pk]))

@csrf_exempt
@require_http_methods(["POST"])
def likePost(request):
	if request.method == "POST":
		post = Post.objects.get(pk=request.POST['postid'])
		post.likes += 1
		post.save()
		return HttpResponse(200)


class ThreadView(generic.DetailView):
	model = Thread
	template_name = "forum/thread.html"

class ThreadViewSecure(generic.DetailView):
	model = Thread
	template_name = "forum/threadS.html"
