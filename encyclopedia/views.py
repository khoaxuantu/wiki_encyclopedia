from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import util
import markdown2


""" The index page """
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "h1tag": "All Pages"
    })


""" Display the entry page """
def generate_entry(request, entry):
    content = util.get_entry(entry)
    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "md": markdown2.markdown(content)
    })


""" Render the searched entry """
def entry(request):
    if request.method == "POST":
        entry = request.POST["q"]
        content = util.get_entry(entry)

        if content is not None:
            return redirect("wiki/"+entry)
        else:
            render_list = []
            entries_list = util.list_entries()
            for s in entries_list:
                # print(util.substr_contained(s, entry))
                if util.substr_contained(s, entry):
                    render_list.append(s)
            print(render_list)

            if len(render_list) == 0:
                return render(request, "encyclopedia/entry.html", {
                    "md": "<h1>Entry Not Found!</h1>"
                })

            return render(request, "encyclopedia/index.html", {
                "entries": render_list,
                "h1tag": "\'"+entry+"\' is not found. Here are the list of keywords\
                that contain the entry:"
            })

    else:
        return index(request)