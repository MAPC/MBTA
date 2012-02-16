from django.contrib import admin

from budgetcalc.models import Category, Optiongroup, Option, Submission


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'cat_type', 'order',)
    list_editable = ('title', 'cat_type', 'order',)


class OptiongroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_editable = ('title',)


class OptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'amount', 'ridership', 'category', 'optiongroup', 'order',)
    list_editable = ('title', 'amount', 'ridership', 'category', 'optiongroup', 'order',)

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('email', 'budget', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Optiongroup, OptiongroupAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Submission, SubmissionAdmin)