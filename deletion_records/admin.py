from django.contrib import admin

from deletion_records.models import DeletedRecord


@admin.site.register(DeletedRecord)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("table_name", "object_id", "deleted_at")
