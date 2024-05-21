from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from markdownx.models import MarkdownxField
from markdownx.widgets import AdminMarkdownxWidget
from .models import rules

class rules_admin(admin.ModelAdmin):
  verbose_name='Rules'
  plural_name='Rule'
  formfield_overrides = {
      MarkdownxField: {'widget': AdminMarkdownxWidget}
  }


admin.site.register(rules, MarkdownxModelAdmin)