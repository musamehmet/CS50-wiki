from django.shortcuts import render
import random
import markdown
from . import util


def md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, title):
    content_html = md_to_html(title)
    if content_html == None:
        return render(
            request, "encyclopedia/error.html", {"msg": "This entry does not exist."}
        )
    else:
        return render(
            request,
            "encyclopedia/entry.html",
            {"title": title, "content": content_html},
        )


def search(request):
    if request.method == "POST":
        search_entry = request.POST["q"]
        content_html = md_to_html(search_entry)
        if content_html is not None:
            return render(
                request,
                "encyclopedia/entry.html",
                {"title": search_entry, "content": content_html},
            )
        else:
            entries = util.list_entries()
            recommendation = []
            for entry in entries:
                if search_entry.lower() in entry.lower():
                    recommendation.append(entry)
        return render(
            request, "encyclopedia/search.html", {"recommendation": recommendation}
        )


def add_content(request):
    if request.method == "GET":
        return render(request, "encyclopedia/add.html")
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(
                request,
                "encyclopedia/error.html",
                {"msg": "Your entry has already exists."},
            )
        else:
            util.save_entry(title, content)
            content_html = md_to_html(title)
            return render(
                request,
                "encyclopedia/entry.html",
                {"title": title, "content": content_html},
            )


def edit_content(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = util.get_entry(title)
        return render(
            request, "encyclopedia/edit.html", {"title": title, "content": content}
        )


def save_content(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        content_html = md_to_html(title)
        return render(
            request,
            "encyclopedia/entry.html",
            {"title": title, "content": content_html},
        )


def random_content(request):
    allEntries = util.list_entries()
    random_entry = random.choice(allEntries)
    content_html = md_to_html(random_entry)
    return render(
        request,
        "encyclopedia/entry.html",
        {"title": random_entry, "content": content_html},
    )
