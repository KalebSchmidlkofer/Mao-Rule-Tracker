from django.contrib import admin
from .models import rules

class rules_admin(admin.ModelAdmin):
  verbose_name='Rules'
  plural_name='Rule'


admin.site.register(rules, rules_admin)