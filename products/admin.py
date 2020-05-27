from django.contrib import admin
from .models import Cakes
from .models import Base
from .models import Offer


class CakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size')


class BaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingrediants')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


# Register your models here.
admin.site.register(Cakes, CakesAdmin)
admin.site.register(Base, BaseAdmin)
admin.site.register(Offer, OfferAdmin)
