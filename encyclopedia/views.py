from http.client import HTTPResponse
from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util




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