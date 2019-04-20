from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Video, Actress, Genre


class ActressInline(admin.TabularInline):
    model = Video.actress.through
    # ordering = ('dvd_id',)

    # extra = 0
    # max_num = 0
    # fields = ['dvd_id']
    # readonly_fields = ['dvd_id']

    # fields = ['dvd_id', 'video_title', 'my']
    # readonly_fields = ['dvd_id', 'video_title', 'my']
    # can_delete = False

    # def dvd_id(self, instance):
    #     return instance.video.dvd_id

    # def dvd_id(self, obj):
    #     return obj.dvd_id
    #
    # def video_title(self, instance):
    #     return instance.video.title
    #
    # def my(self, instance):
    #     url = reverse("admin:my_av_video_change", args=(instance.video.id,))
    #     return mark_safe('<a href={url}>{url}</a>'.format(url=url))
    # return mark_safe('<a href="http://127.0.0.1:8000/admin/my_av/actress/{}/change/">Visit our HTML tutorial</a>'.format(instance.video.id))

    # my.allow_tags = True
    # video_title.short_description = 'aaaaaaaaaaaaa'


class GenreInline(admin.TabularInline):
    model = Video.genre.through


class VideoAdmin(admin.ModelAdmin):
    list_display = ['dvd_id', 'title', 'get_actress']

    def get_actress(self, obj):
        return ", ".join([p.name for p in obj.actress.all()])

    get_actress.admin_order_field = 'actress__name'


class ActressAdmin(admin.ModelAdmin):
    inlines = [ActressInline]


class GenreAdmin(admin.ModelAdmin):
    inlines = [GenreInline]


admin.site.register(Video, VideoAdmin)
admin.site.register(Actress, ActressAdmin)
admin.site.register(Genre, GenreAdmin)