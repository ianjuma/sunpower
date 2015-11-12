from django.contrib import admin
from utils.models import Country, Currency

admin.register(Country, admin.ModelAdmin)
admin.register(Currency, admin.ModelAdmin)
