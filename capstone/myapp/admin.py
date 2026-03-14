from django.contrib import admin
from .models import Seed, DonorProfile, Donor, Use, Feedback

# Register your models here.
class SeedAdmin(admin.ModelAdmin):
    #readonly_fields = ('slug',)
    prepopulated_fields = {"slug": ('name',)}
    list_filter = ('donors', 'use')
    list_display = ('name', 'botanical')
    search_fields = ('name', 'donors')

admin.site.register(Seed, SeedAdmin)
admin.site.register(Use)
admin.site.register(Donor)
admin.site.register(DonorProfile)
admin.site.register(Feedback)