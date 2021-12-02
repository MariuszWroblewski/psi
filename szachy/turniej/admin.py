from django.contrib import admin
from .models import Sedzia, Uczestnik, Turniej, Rozgrywka

# Register your models here.

admin.site.register(Sedzia)
admin.site.register(Uczestnik)
admin.site.register(Turniej)
admin.site.register(Rozgrywka)
