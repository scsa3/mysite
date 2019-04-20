from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from .models import Movie, Genre
from .forms import MovieChangeListForm


class MovieChangeList(ChangeList):
    def __init__(self,
                 request,
                 model,
                 list_display,
                 list_display_links,
                 list_filter,
                 date_hierarchy,
                 search_fields,
                 list_select_related,
                 list_per_page,
                 list_max_show_all,
                 list_editable,
                 model_admin, sortable_by):
        super().__init__(request,
                         model,
                         list_display,
                         list_display_links,
                         list_filter,
                         date_hierarchy,
                         search_fields,
                         list_select_related,
                         list_per_page,
                         list_max_show_all,
                         list_editable,
                         model_admin, sortable_by)

        # these need to be defined here, and not in MovieAdmin
        self.list_display = ['action_checkbox', 'name', 'genre']
        self.list_display_links = ['name']
        self.list_editable = ['genre']


class MovieAdmin(admin.ModelAdmin):

    def get_changelist(self, request, **kwargs):
        return MovieChangeList

    def get_changelist_form(self, request, **kwargs):
        return MovieChangeListForm


# admin.site.register(Movie, MovieAdmin)
# admin.site.register(Genre)
