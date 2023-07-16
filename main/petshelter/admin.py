from django.contrib import admin
from .models import Pupil, News, Interactive


class PupilAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'telegram_publication_flag_completed',)


class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'telegram_publication_flag_completed',)


class InteractiveAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'telegram_publication_flag_completed',)


admin.site.register(Pupil, PupilAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Interactive, InteractiveAdmin)
