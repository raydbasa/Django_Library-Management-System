from django.contrib import admin

from usermanagement.models import UserProfile, User, Role, Faculty, City, Semester, Gender

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(Faculty)
admin.site.register(City)
admin.site.register(Gender)
admin.site.register(Semester)

