from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Shaxar nomi")
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shaxar nomi"
        verbose_name_plural = "Shaxarlar nomlari"


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Dasturlash tili")
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dasturlash tili"
        verbose_name_plural = "Dasturlash tilllari"


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name="Vakansiya nomi")
    company = models.CharField(max_length=250, verbose_name="Kompaniya")
    description = models.TextField(verbose_name="Vakansiya tasnifi")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Shaxar")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Dasturlash tili")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vakansiya"
        verbose_name_plural = "Vakansiyalar"
        ordering = ['-timestamp']


class Error(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return str(self.timestamp)

    class Meta:
        verbose_name = "Xato"
        verbose_name_plural = "Xatolar"