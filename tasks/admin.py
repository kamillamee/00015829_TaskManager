"""
Admin panel configuration for Task Manager.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Project, Tag, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'task_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description', 'owner__username']
    ordering = ['-created_at']
    raw_id_fields = ['owner']

    @admin.display(description='Tasks')
    def task_count(self, obj):
        return obj.tasks.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'task_count']
    search_fields = ['name']
    ordering = ['name']

    @admin.display(description='Tasks')
    def task_count(self, obj):
        return obj.tasks.count()


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'owner', 'status', 'tags_list', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'description', 'project__name']
    filter_horizontal = ['tags']
    ordering = ['-created_at']
    raw_id_fields = ['project']
    date_hierarchy = 'created_at'

    @admin.display(description='Owner')
    def owner(self, obj):
        return obj.project.owner.username

    @admin.display(description='Tags')
    def tags_list(self, obj):
        return ', '.join(t.name for t in obj.tags.all()) or '-'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('project', 'project__owner').prefetch_related('tags')


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0
    show_change_link = True
    fields = ['name', 'description', 'created_at']


admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'project_count', 'is_staff', 'is_active', 'date_joined', 'last_login']
    list_filter = ['is_staff', 'is_active', 'is_superuser', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-date_joined']
    inlines = [ProjectInline]

    @admin.display(description='Projects')
    def project_count(self, obj):
        return obj.projects.count()
