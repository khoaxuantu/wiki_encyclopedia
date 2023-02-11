from django.shortcuts import render
from django.http import HttpResponse

from . import util
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

""" Display the entry page """
def entry(request):
    if request.method == "POST":
        entry = request.POST["q"]
        content = util.get_entry(entry)

        if content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry,
                "md": markdown2.markdown(content)
            })
        else:
            return HttpResponse("404 Not Found!")
            
    else:
        return index(request)