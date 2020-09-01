from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.urls import reverse_lazy

def home_view(request):
    return redirect('posts:main_post_view')


