
from django. contrib import admin
from models import Country, Departament, City, User 
# Register your models here.
'''
admin.site.register(Country)
admin.site.register(Departament)
admin.site.register(City)
admin.site.register (User)
'''
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    display_data = ('name', 'abreviation', 'get_status')

    def get_status (self, obj):
        return "Active" if obj. status else "Inactive"
    get_status.short_description = 'Status' #Table label
