import datetime
from django.core.management.base import BaseCommand
from core.models import ActivityPost


class Command(BaseCommand):
    help = 'Populate sample activity posts for Layanan Kakak Asuh VVD'

    def handle(self, *args, **options):
        posts_data = [
            {
                "title": "Penyaluran Bantuan SPP & Perlengkapan Belajar Semester Gasal Adik Asuh Pati & Jepara",
                "slug": "penyaluran-bantuan-spp-perlengkapan-belajar-pati-jepara",
                "activity_date": datetime.date(2026, 9, 15),
                "is_published": True,
                "content": (
                    "Pada pertengahan September 2026, tim Layanan Kakak Asuh Vihara Vimala Dharma Bandung telah "
                    "berhasil menyalurkan dana bantuan pendidikan periode semester gasal untuk 24 Adik Asuh di wilayah Pati dan Jepara, Jawa Tengah.\n\n"
                    "Bantuan ini mencakup pembayaran SPP sekolah, seragam baru, sepatu, dan buku modul pelajaran. "
                    "Para pengurus lokal di Vihara mitra mendampingi penyerahan langsung kepada wali adik asuh dengan penuh sukacita.\n\n"
                    "Kami mengucapkan terima kasih yang sebesar-besarnya kepada seluruh Donatur Tetap dan Donatur Sekali Jalan atas cinta kasih dan kepedulian yang terus mengalir bagi masa depan pendidikan anak-anak Buddhis ini. Semoga kebajikan ini senantiasa melimpahkan berkah kebahagiaan dan kedamaian bagi para donatur sekeluarga."
                )
            },
            {
                "title": "Monitoring Rapor Semester & Paket Nutrisi Adik Asuh Sukabumi & Ampel",
                "slug": "monitoring-rapor-semester-paket-nutrisi-sukabumi-ampel",
                "activity_date": datetime.date(2026, 8, 20),
                "is_published": True,
                "content": (
                    "Tim Kakak Asuh VVD mengadakan kegiatan monitoring perkembangan belajar dan kesehatan untuk 18 Adik Asuh di wilayah Sukabumi dan Ampel.\n\n"
                    "Hasil evaluasi rapor menunjukkan rata-rata adik asuh mempertahankan peringkat 10 besar di kelas masing-masing. "
                    "Selain pemantauan prestasi akademik, Kakak Asuh juga membagikan paket suplemen nutrisi, susu, dan alat tulis penunjang ujian tengah semester.\n\n"
                    "Laporan nilai dan foto perkembangan masing-masing adik asuh telah kami distribusikan langsung kepada para Donatur Tetap melalui pesan resmi WhatsApp Kakak Asuh. Transparansi dan akuntabilitas adalah komitmen utama kami."
                )
            },
            {
                "title": "Apresiasi Kelulusan & Beasiswa Lanjutan Siswa Berprestasi Wonosobo",
                "slug": "apresiasi-kelulusan-beasiswa-lanjutan-wonosobo",
                "activity_date": datetime.date(2026, 7, 10),
                "is_published": True,
                "content": (
                    "Kabar membanggakan datang dari lereng pegunungan Wonosobo! Dua orang Adik Asuh binaan Layanan Kakak Asuh VVD "
                    "berhasil menyelesaikan pendidikan jenjang SMK dengan predikat sangat memuaskan, serta 1 orang adik asuh meraih beasiswa jalur prestasi ke perguruan tinggi negeri.\n\n"
                    "Kakak Asuh VVD memberikan dana apresiasi kelulusan dan serah terima bantuan biaya pendaftaran kuliah perdana. "
                    "Keberhasilan ini menjadi bukti nyata bahwa gotong royong dan uluran tangan para donatur telah mengubah garis hidup generasi muda Buddhis menuju masa depan yang cerah dan mandiri."
                )
            }
        ]

        created_count = 0
        for item in posts_data:
            obj, created = ActivityPost.objects.get_or_create(
                slug=item["slug"],
                defaults={
                    "title": item["title"],
                    "activity_date": item["activity_date"],
                    "is_published": item["is_published"],
                    "content": item["content"],
                }
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"[OK] Berhasil membuat: {obj.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"[-] Sudah ada: {obj.title}"))

        self.stdout.write(self.style.SUCCESS(f"\nSelesai! {created_count} data contoh berhasil ditambahkan."))

