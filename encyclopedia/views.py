from cProfile import label
from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
from django.contrib import messages
  

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def page(request, title):

    markdowner = Markdown()
    entry = util.get_entry(title)

    if entry:
        entry = markdowner.convert(entry)
        return render(request, 'encyclopedia/page.html', {'title': title, 'entry': entry })  
    
    return redirect('not_found')

def not_found(request):
    return render(request, 'encyclopedia/not-found.html')


def search(request):
    q = request.POST.get('q').lower()
    entries = util.list_entries()

    matches = []

    for entry in entries:
        if q == entry.lower():
            return redirect('page', q)
        if q in entry.lower():
            matches.append(entry)

    return render(request, 'encyclopedia/search.html', {'matches': matches})

def new_page(request):

    if request.method == "POST":
        title = request.POST.get('page-title')
        content = request.POST.get('content')
        entries_lower_case = [entry.lower() for entry in util.list_entries()]

        if title.lower() in entries_lower_case:
            messages.error(request, "That entry already exists")
            return render(request, 'encyclopedia/new-page.html')

        util.save_entry(title, content)

        return redirect('page', title)

    return render(request, 'encyclopedia/new-page.html')

def edit_page(request, title):

    if request.method == "POST":
        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect('page', title)

    entry = util.get_entry(title)

    if entry:
        return render(request, 'encyclopedia/edit-page.html', {'title': title, 'entry': entry })  
    
    return redirect('not_found')


