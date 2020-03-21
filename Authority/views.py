from django.shortcuts import render
from Candidate.models import Candidate


def sorted_list_3(request):
    candidates = Candidate.objects.all()
    candidates = list(candidates)
    candidates.sort(key=lambda c: c.experiences_skills_combined_score, reverse=True)

    return render(request, "Authority/sorted_list.html", {'candidates': candidates})


def sorted_list_2(request):
    candidates = Candidate.objects.all()
    candidates = list(candidates)
    candidates.sort(key=lambda c: c.skills_score, reverse=True)

    return render(request, "Authority/sorted_list.html", {'candidates': candidates})


def sorted_list_1(request):
    candidates = Candidate.objects.all()
    candidates = list(candidates)
    candidates.sort(key=lambda c: c.total_experiences, reverse=True)

    return render(request, "Authority/sorted_list.html", {'candidates': candidates})


def home(request):
    return render(request, "Authority/sorted_list.html", {})
