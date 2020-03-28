from django.http import Http404, HttpResponseRedirect

from django.urls import reverse

from django.shortcuts import render
from .models import Article

def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:5]
	return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})



def blog(request, article_id):
	try:
		a=Article.objects.get (id = article_id)
	except:
		raise Http404(" Статься не найдена!")
	latest_comments_list = a.comment_set.order_by('-id')[:10]

	latest_articles_list = Article.objects.order_by('-pub_date')[:3]	

	return render(request, 'articles/blog.html', {'article':a, 'latest_comments_list':latest_comments_list, 'latest_articles_list': latest_articles_list})	


def leave_comment(request, article_id):
	try:
		a=Article.objects.get (id = article_id)
	except:
		raise Http404(" Статься не найдена!")
	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect(reverse('articles:blog', args = (a.id,)))