from django.contrib import admin

from .models import SamlProvider, PEMCertificate


@admin.register(PEMCertificate)
class PEMCertificateAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ("id",)
    search_fields = ("name",)


@admin.register(SamlProvider)
class SamlProviderAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    autocomplete_fields = (
        "idp_x509_signing_certificates",
        "idp_x509_encryption_certificates",
    )
