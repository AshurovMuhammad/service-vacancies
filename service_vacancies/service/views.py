from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm


def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        obj = {}
        if city:
            obj['city__slug'] = city
        if language:
            obj['language__slug'] = language
        qs = Vacancy.objects.filter(**obj)
    context = {
        "city": city,
        "language": language,
        "form": form,
        "object_list": qs
    }
    return render(request, 'service/home.html', context)
