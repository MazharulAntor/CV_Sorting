from django.shortcuts import render
from Candidate.models import Candidate


def sorted_list(request):
    candidates = Candidate.objects.all()
    candidates = list(candidates)
    candidates.sort(key=lambda c: c.experiences_skills_combined_score, reverse=True)

    return render(request, "Authority/sorted_list.html", {'candidates': candidates})
