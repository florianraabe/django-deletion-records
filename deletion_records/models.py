from django.db import models
from django.utils.translation import gettext_lazy as _


class DeletedRecord(models.Model):
    data = models.JSONField(_("data"))
    table_name = models.CharField(_("table name"), max_length=128)
    object_id = models.BigIntegerField(_("object id"))
    deleted_at = models.DateTimeField(_("deleted at"))

    class Meta:
        verbose_name = _("deleted record")
        verbose_name_plural = _("deleted records")

        db_table = "django_deletion_record"
        managed = False

    def __str__(self) -> str:
        return "(%s, %s)" % (self.table_name, self.object_id)
