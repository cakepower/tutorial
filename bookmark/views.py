from typing import NewType
from django.db.models.lookups import EndsWith
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .models import Bookmark
from .forms import BookmarkForm

# Create your views here.
def list(request):
    list = Bookmark.objects.all()

    return render(request, 'bookmark/list.html', {
        'list': list,
    })

def new(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = Bookmark()
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            return redirect('bookmark:list')
    else:
        form = BookmarkForm()
    return render(request, 'bookmark/new.html', {
        'form': form,
    })

def edit(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)

    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance = bookmark)
        if form.is_valid():
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            return redirect('bookmark:list')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'bookmark/edit.html', {
        'bookmark': bookmark,
        'form': form,
    }) 

def delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)

    if request.method == 'POST':
        bookmark.delete()
        return redirect('bookmark:list')

