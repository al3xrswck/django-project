from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Street)
admin.site.register(City)
admin.site.register(Product)