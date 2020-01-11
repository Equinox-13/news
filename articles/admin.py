from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.StackedInline):
	# replace StackdInline to TabularInline for single line display in admin page
	model = Comment


class ArticleAdmin(admin.ModelAdmin):
	inlines = [CommentInline,]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
