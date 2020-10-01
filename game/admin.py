from django.contrib import admin

from .models import blogpost

admin.site.register(blogpost)

# class ChoiceInline(admin.TabularInline):  # StackedInline, TabularInline
#     model = Choice
#     extra = 3


# class blogpostAdmin(admin.ModelAdmin):
#     # fields = ['pub_date', 'question_text']
#     fieldsets = [
#         (None,               {'fields': ['post_title']}),
#         ('Date information', {'fields': [
#          'pub_date'], 'classes': ['collapse']}),
#     ]
#     # inlines = [ChoiceInline]

#     # displaying columns in the questions list
#     list_display = ('post_title', 'pub_date')

#     # additional features
#     # list_filter = ['pub_date']
#     search_fields = ['post_title']


# admin.site.register(blogpost, blogpostAdmin)
