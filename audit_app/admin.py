from django.contrib import admin

from audit_app.models import Audit


# Register your models here.
class AuditAdmin(admin.ModelAdmin):
    model = Audit
    list_display = ('id','audited_user', 'description', 'creation_date')
    search_fields =

admin.site.register(Audit, AuditAdmin)
