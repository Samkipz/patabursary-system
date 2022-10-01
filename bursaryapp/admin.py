from django.contrib import admin
from .models import Bursary,BursaryParameter,Application



class Bursary_ParametersAdmin(admin.StackedInline):
    model = BursaryParameter
    # we are using StackedInline class to edit “BursaryParameter” model inside “Bursary” model.

@admin.register(Bursary)
class BursaryAdmin(admin.ModelAdmin):
    inlines = [Bursary_ParametersAdmin]

    class Meta:
        model = Bursary

@admin.register(BursaryParameter)
class Bursary_ParametersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Application)
# admin.site.register(BursaryParameter)