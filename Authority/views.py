from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

from Authority.models import TopCandidates
from Candidate.models import Candidate


def sorted_list_3(request):
    if 'username' not in request.session:
        return render(request, "Account/login.html", {})
    candidates = Candidate.objects.all()
    candidates = list(candidates)
    candidates.sort(key=lambda c: c.experiences_skills_combined_score, reverse=True)
    return render(request, "Authority/sorted_list.html", {'candidates': candidates})


def sorted_list_2(request):
    if 'username' not in request.session:
        return render(request, "Account/login.html", {})
    candidates = Candidate.objects.all()
    candidates = list(candidates)
    candidates.sort(key=lambda c: c.skills_score, reverse=True)

    return render(request, "Authority/sorted_list.html", {'candidates': candidates})


def sorted_list_1(request):
    if 'username' not in request.session:
        return render(request, "Account/login.html", {})
    candidates = Candidate.objects.all()
    candidates = list(candidates)
    candidates.sort(key=lambda c: c.total_experiences, reverse=True)

    return render(request, "Authority/sorted_list.html", {'candidates': candidates})


def home(request):
    if 'username' not in request.session:
        return render(request, "Account/login.html", {})

    return render(request, "Authority/sorted_list.html", {})

def sendEmail1(request):

    if 'username' not in request.session:
        return render(request, "Account/login.html", {})
    top_candidates = TopCandidates.objects.all()
    candidates = Candidate.objects.all()
    candidates = list(candidates)
    candidates.sort(key=lambda c: c.total_experiences, reverse=True)
    mailPart(top_candidates, candidates)
    return render(request, "Authority/sorted_list.html", {'candidates': candidates})


def sendEmail2(request):
    if 'username' not in request.session:
        return render(request, "Account/login.html", {})
    top_candidates = TopCandidates.objects.all()
    candidates = Candidate.objects.all()
    candidates = list(candidates)
    candidates.sort(key=lambda c: c.skills_score, reverse=True)
    mailPart(top_candidates, candidates)
    return render(request, "Authority/sorted_list.html", {'candidates': candidates})


def sendEmail3(request):
    top_candidates = TopCandidates.objects.all()
    candidates = Candidate.objects.all()
    candidates = list(candidates)
    candidates.sort(key=lambda c: c.experiences_skills_combined_score, reverse=True)
    mailPart(top_candidates, candidates)
    return render(request, "Authority/sorted_list.html", {'candidates': candidates})


def mailPart(top_candidates, candidates):
    count = 1
    for max_can in top_candidates:
        max_candidates = max_can.number_of_selection
        date = max_can.date
        print(max_candidates)
    for can in candidates:
        if count <= max_candidates:
            send_mail(
                'Django Developer Interview',
                'You submitted your CV to Antor Productions. You are cordially invited for the interview. Your score: ' +
                str(can.experiences_skills_combined_score) + '. Position: ' + str(count) + '. Interview Date: ' + str(
                    date) + '.',
                settings.EMAIL_HOST_USER,
                [can.email],
                fail_silently=False,
            )
            count = count + 1
