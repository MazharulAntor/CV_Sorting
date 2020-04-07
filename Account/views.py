from django.shortcuts import render, redirect

from Authority.models import Authority
from Authority.views import home
from Candidate.views import handleResume


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        authority = Authority.objects.all().filter(username=username, password=password)
        for auth in authority:
            request.session['username'] = auth.username
        if authority:
            return redirect(handleResume)
    return render(request, "Account/login.html", {})


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect(login)
