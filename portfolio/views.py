from django.shortcuts import render
from . import data


def index(request):
    context = {
        "profile": data.PROFILE,
        "experience": data.EXPERIENCE,
        "skills": data.SKILLS,
        "certifications": data.CERTIFICATIONS,
        "education": data.EDUCATION,
        "mentoring": data.MENTORING,
        "speaking": data.SPEAKING,
    }
    return render(request, "portfolio/index.html", context)
