from django.contrib import admin
from django.utils.html import format_html
from .models import ActivityPost

# Customizing Django Admin Header and Title
admin.site.site_header = "Admin Layanan Kakak Asuh VVD Bandung"
admin.site.site_title = "Admin Layanan Kakak Asuh VVD Bandung"
admin.site.index_title = "Panel Kontrol Layanan Kakak Asuh PVVD"


@admin.register(ActivityPost)
class ActivityPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'activity_date', 'is_published', 'thumbnail_preview', 'created_at')
    list_filter = ('is_published', 'activity_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'activity_date'
    list_editable = ('is_published',)
    ordering = ('-activity_date', '-created_at')
    readonly_fields = ('created_at', 'thumbnail_large_preview')

    fieldsets = (
        ("Informasi Utama", {
            'fields': ('title', 'slug', 'activity_date', 'is_published')
        }),
        ("Foto Dokumentasi", {
            'fields': ('thumbnail', 'thumbnail_large_preview')
        }),
        ("Konten & Narasi", {
            'fields': ('content',)
        }),
        ("Metadata", {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="{}" style="width: 54px; height: 38px; object-fit: cover; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.12);" />',
                obj.thumbnail.url
            )
        return format_html('<span style="color: #94a3b8; font-size: 12px;">(Tanpa Foto)</span>')
    thumbnail_preview.short_description = "Pratinjau Foto"

    def thumbnail_large_preview(self, obj):
        if obj.thumbnail:
            return format_html(
                '<div style="margin-top: 6px;"><img src="{}" style="max-width: 320px; max-height: 200px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" /><p style="font-size: 12px; color: #64748b; margin-top: 4px;">Foto yang sedang digunakan</p></div>',
                obj.thumbnail.url
            )
        return format_html('<span style="color: #94a3b8;">Belum ada foto yang diunggah. Foto default akan digunakan di landing page.</span>')
    thumbnail_large_preview.short_description = "Tampilan Foto Saat Ini"

