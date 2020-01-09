from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(LoginRequiredMixin,ListView):
	model = Article
	template_name = 'article_list.html'
	login_url = 'login'


class ArticleDetailView(LoginRequiredMixin,DetailView):
	model = Article
	template_name = 'article_detail.html'
	login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin,UpdateView):
	model = Article
	fields = ('title','body',)
	template_name = 'article_edit.html'
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs):
		"""
		checks wheather the updation is done 
		by the same user who has created it
		"""
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
	model = Article
	template_name = 'article_delete.html'
	success_url = reverse_lazy('article_list')
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs):
		"""
		checks wheather the deletion is done 
		by the same user who has created it
		"""
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin,CreateView):
	model = Article
	fields = ('title','body',)
	template_name = 'article_new.html'
	login_url = 'login' # redirects to login page if user not signed in

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)