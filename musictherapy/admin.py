from django.contrib import admin

import models
# Register your models here.

admin.site.register(models.Domains)
admin.site.register(models.Goals)
admin.site.register(models.DomainMeasurables)
admin.site.register(models.GoalsMeasurables)
admin.site.register(models.UserGoals)
admin.site.register(models.UserMeasurables)
admin.site.register(models.UserGoalMeasurables)
admin.site.register(models.UserDomainNoteMeasurables)
admin.site.register(models.UserGoalNoteMeasurable)


# admin.site.register(UserInfo)
# admin.site.register(MusicalPreference)
# admin.site.register(CommunicationGoals)
# admin.site.register(CommunicationAssessment)