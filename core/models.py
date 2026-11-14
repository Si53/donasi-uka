from django.db import models
from django.utils.text import slugify


class ActivityPost(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name="Judul Kegiatan",
        help_text="Contoh: Penyaluran Bantuan Pendidikan Semester Genap Adik Asuh Sukabumi"
    )
    slug = models.SlugField(
        max_length=220, 
        unique=True, 
        blank=True,
        verbose_name="Slug URL",
        help_text="Akan terisi otomatis dari judul jika dikosongkan."
    )
    thumbnail = models.ImageField(
        upload_to='activities/', 
        verbose_name="Foto Dokumentasi",
        blank=True, 
        null=True,
        help_text="Format foto yang dianjurkan: JPG/PNG/WebP resolusi baik."
    )
    content = models.TextField(
        verbose_name="Isi Berita / Dokumentasi",
        help_text="Tuliskan laporan ringkas kegiatan, nama daerah, jumlah bantuan, dan kesan kegiatan."
    )
    activity_date = models.DateField(
        verbose_name="Tanggal Kegiatan",
        help_text="Tanggal saat kegiatan penyaluran berlangsung."
    )
    is_published = models.BooleanField(
        default=True, 
        verbose_name="Tampilkan di Website",
        help_text="Centang agar dokumentasi ini muncul pada landing page website."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Waktu Dibuat"
    )

    class Meta:
        verbose_name = "Dokumentasi Kegiatan"
        verbose_name_plural = "Daftar Dokumentasi Kegiatan"
        ordering = ['-activity_date', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.activity_date.strftime('%d/%m/%Y')})"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "kegiatan"
            slug = base_slug
            counter = 1
            while ActivityPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def excerpt(self):
        """Returns first 140 chars for card display."""
        if len(self.content) > 140:
            return self.content[:137] + "..."
        return self.content

