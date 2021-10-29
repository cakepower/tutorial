from django.contrib import admin

# Register your models here.
from .models import Blog, HelloWorld, Hello, World, Condition

class HelloAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'text2']

class WorldAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'contents']

class ConditionAdmin(admin.ModelAdmin):
    list_display = ['id', 'upcond', 'downcond', 'discond', 'transcond', 'field']

class HelloWorldAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']    

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'theme2', 'theme3', 'body']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Hello, HelloAdmin)
admin.site.register(HelloWorld, HelloWorldAdmin)
admin.site.register(World, WorldAdmin)
admin.site.register(Condition, ConditionAdmin)
