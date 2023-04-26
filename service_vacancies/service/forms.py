from django import forms
from service.models import City, Language


class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        to_field_name="slug",
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Shaxar")
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        to_field_name="slug",
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Yo'nalish")
