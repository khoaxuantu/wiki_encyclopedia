from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from . import util, forms
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
                that contain the entry:<br>"
            })

    else:
        return index(request)


""" Create a new page """
def create_page(request):
    if request.method == "POST":
        text = forms.MarkdownForm(request.POST)
        # print(text.cleaned_data)

        if text.is_valid():
            title = text.cleaned_data["title"]

            if util.get_entry(title) is not None:
                messages.error(request, "The \'"+title+"\' title exists, please choose another title.")
                return render(request, "encyclopedia/newpage.html", {
                    "form": text
                })

            content = text.cleaned_data["content"]
            util.save_entry(title, content)
            return redirect("wiki/"+title)
        else:
            return render(request, "encyclopedia/newpage.html", {
                "form": text
            })
        
    return render(request, "encyclopedia/newpage.html", {
        "form": forms.MarkdownForm()
    })


""" Edit a page """
def edit_page(request, entry):
    initial_dict = {}
    initial_dict["content"] = util.get_entry(entry)

    if request.method == "POST":
        text = forms.EditForm(request.POST)

        if text.is_valid():
            content = text.cleaned_data["content"]
            util.save_entry(entry, content)
            return redirect("../wiki/"+entry)
        else:
            return render(request, "encyclopedia/editpage.html", {
                "form": text
            })

    return render(request, "encyclopedia/editpage.html", {
        "form": forms.EditForm(initial=initial_dict),
        "title": entry
    })