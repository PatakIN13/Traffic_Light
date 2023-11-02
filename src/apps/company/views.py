from django.shortcuts import render
from apps.company.load_tree import generate_tree_department


def index(request):

    return render(request, "index.html", context={"data": generate_tree_department()})
