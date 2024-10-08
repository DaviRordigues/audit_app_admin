from django.contrib import admin
from rangefilter.filters import (
    DateRangeQuickSelectListFilterBuilder,
)

from audit_app.models import Audit


# Register your models here.
class AuditAdmin(admin.ModelAdmin):
    model = Audit
    list_display = ('id', 'audited_user', 'description', 'creation_date', 'action')
    search_fields = ('audited_user', 'description')
    list_filter = (
        ("creation_date", DateRangeQuickSelectListFilterBuilder()), ('action'),  # Range + QuickSelect Filter
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(source_app='SISAQUA')


admin.site.register(Audit, AuditAdmin)
