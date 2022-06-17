from django.contrib import admin
from .models import Education, Sector,companyType,Experience, Position, profileModel,RecruiterProfile,AgencyProfile, userLanguage, userSkill
# Register your models here.

admin.site.register(profileModel)
admin.site.register(RecruiterProfile)
admin.site.register(AgencyProfile)
admin.site.register(Position)
admin.site.register(userSkill)
admin.site.register(Experience)
admin.site.register(companyType)
admin.site.register(Sector)
admin.site.register(Education)
admin.site.register(userLanguage)








