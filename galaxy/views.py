from django.shortcuts import render


def index(request, id):
    return render(request, "galaxy/galaxy-s23-ultra.html")
