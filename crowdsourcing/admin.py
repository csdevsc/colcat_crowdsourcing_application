from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from crowdsourcing.models import Task, OCRTranscription, OCRVerification, CrowdsourceVerification
from crowdsourcing.models import NamingTranscription1, NamingTranscription2

# RESOURCES

class OCRTranscriptionResource(resources.ModelResource):
    class Meta:
        model = OCRTranscription

class OCRVerificationResource(resources.ModelResource):
    class Meta:
        model = OCRVerification

class CrowdsourceVerificationResource(resources.ModelResource):
    class Meta:
        model = CrowdsourceVerification

class NamingTranscription1VerificationResource(resources.ModelResource):
    class Meta:
        model = NamingTranscription1

class NamingTranscription2VerificationResource(resources.ModelResource):
    class Meta:
        model = NamingTranscription2

# ADMINS
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('task_id', 'name', 'responses', 'task_type')

class OCRTranscriptionAdmin(ImportExportModelAdmin):
    resource_class = OCRTranscriptionResource
    pass

class OCRVerificationAdmin(ImportExportModelAdmin):
    resource_class = OCRVerificationResource
    pass

class CrowdsourceVerificationAdmin(ImportExportModelAdmin):
    resource_class = CrowdsourceVerificationResource
    pass

class NamingTranscription1Admin(ImportExportModelAdmin):
    resource_class = NamingTranscription1VerificationResource
    pass

class NamingTranscription2Admin(ImportExportModelAdmin):
    resource_class = NamingTranscription2VerificationResource
    pass


admin.site.register(Task, TaskAdmin)
admin.site.register(OCRTranscription, OCRTranscriptionAdmin)
admin.site.register(OCRVerification, OCRVerificationAdmin)
admin.site.register(CrowdsourceVerification, CrowdsourceVerificationAdmin)
admin.site.register(NamingTranscription1, NamingTranscription1Admin)
admin.site.register(NamingTranscription2, NamingTranscription2Admin)
