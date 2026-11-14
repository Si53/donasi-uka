# PRODUCT REQUIREMENTS DOCUMENT (PRD)
**Nama Proyek:** Website Informasi & Donasi Layanan Kakak Asuh Vihara Vimala Dharma (VVD) Bandung  
**Versi Dokumen:** 1.0  
**Pengembang (Developer):** Internal (Solo Developer)  
**Target Peluncuran:** Secepatnya (MVP / Minimum Viable Product)  

---

## 1. Latar Belakang & Tujuan Proyek (Project Overview)
**Layanan Kakak Asuh Vihara Vimala Dharma Bandung** adalah divisi khusus yang mengelola penyaluran bantuan biaya pendidikan dari para donatur kepada adik asuh Buddhis, sekaligus melakukan monitoring perkembangan mereka.

Website ini dibangun sebagai pusat informasi resmi dan jembatan penghubung untuk menarik **Donatur** dari seluruh kalangan agar turut berpartisipasi memberikan bantuan materi (baik sebagai **Donatur Tetap** maupun **Donatur Sekali Jalan**).

### 1.1 Terminologi Penting
* **Kakak Asuh:** Divisi/tim pengurus di Vihara Vimala Dharma yang mengelola dana bantuan, memonitor adik asuh, mengelola website (1 orang admin), serta mengirimkan laporan kepada donatur.
* **Donatur Tetap:** Pemberi bantuan dana secara rutin setiap bulan (laporan perkembangan adik asuh dikirimkan langsung via WhatsApp oleh Kakak Asuh, dan pengingat bulanan dikirimkan oleh adik asuh melalui WhatsApp).
* **Donatur Sekali Jalan:** Pemberi bantuan dana secara insidental/tidak terikat waktu (melihat transparansi melalui dokumentasi kegiatan penyaluran bantuan dan testimoni wisuda di website).
* **Adik Asuh:** Pelajar/mahasiswa Buddhis penerima manfaat bantuan biaya pendidikan.

### 1.2 Tujuan & Metrik Keberhasilan (Success Metrics)
1. **Penyebaran Informasi:** Menjadi rujukan utama yang menjelaskan profil, alur penyaluran, dan kredibilitas Layanan Kakak Asuh VVD kepada masyarakat luas.
2. **Konversi Donatur:** Meningkatkan jumlah pendaftar **Donatur Tetap** baru (diukur dari jumlah klik tombol pendaftaran WhatsApp) dan meningkatkan total nominal **Donasi Sekali Jalan**.
3. **Kemudahan Pengelolaan:** Admin (1 orang Kakak Asuh) dapat memperbarui konten dokumentasi kegiatan/berita dengan mudah melalui tabel admin tanpa perlu mengubah kode program.

---

## 2. Target Pengguna (User Personas)
1. **Calon Donatur / Donatur Umum (Seluruh Kalangan):**
   * **Kebutuhan:** Ingin mengetahui kejelasan program, melihat bukti nyata penyaluran bantuan dan lulusan adik asuh, serta mendapatkan cara berdonasi yang cepat, jelas, dan praktis (via QRIS, Transfer Bank, atau informasi Stand Minggu Pagi).
2. **Admin Website (1 Orang Pengurus Kakak Asuh):**
   * **Kebutuhan:** Membutuhkan halaman *backoffice* (tabel admin) yang sederhana untuk menambah, mengubah, dan menghapus artikel kegiatan/dokumentasi penyaluran bantuan.

---

## 3. Ruang Lingkup Fitur & Kebutuhan Fungsional (Functional Requirements)

### 3.1 Sisi Pengunjung / Donatur (Public Front-End)
Pengunjung **tidak perlu melakukan Login/Registrasi akun** di website. Seluruh interaksi konfirmasi dan pendaftaran diarahkan langsung ke WhatsApp resmi Layanan Kakak Asuh.

| Kode | Bagian / Halaman | Deskripsi Kebutuhan Fitur | Prioritas |
| :--- | :--- | :--- | :--- |
| **FR-01** | **Hero Section (Beranda)** | Menampilkan pesan utama yang menggugah empati, pengenalan singkat Layanan Kakak Asuh VVD, serta tombol Call-to-Action (CTA) utama: **"Donasi Sekarang"** dan **"Jadi Donatur Tetap"**. | Wajib (P0) |
| **FR-02** | **Tentang Kami & Statistik Adik Asuh** | Menampilkan profil Layanan Kakak Asuh VVD, alur pengelolaan dana menyeluruh oleh Kakak Asuh, serta **data statis** (diatur di awal dalam kode):<br>- Total keseluruhan jumlah Adik Asuh.<br>- Sebaran daerah tempat Adik Asuh berada. | Wajib (P0) |
| **FR-03** | **Pilihan Skema Donasi** | Menjelaskan 3 cara berdonasi secara jelas:<br>1. **Donatur Tetap (Rutin Bulanan):** Dilengkapi tombol CTA yang langsung mengarahkan ke *chat* WhatsApp Kakak Asuh dengan *pre-filled text* pendaftaran.<br>2. **Donasi Sekali Jalan:** Menampilkan gambar **QRIS Resmi** (bisa diunduh/diperbesar) dan **Nomor Rekening Bank** Layanan Kakak Asuh (dilengkapi tombol *Copy Nomor Rekening*), serta tombol **Unggah/Kirim Bukti Transfer via WhatsApp Admin**.<br>3. **Donasi Langsung (Offline):** Informasi jadwal dan lokasi Stand Kakak Asuh di Vihara Vimala Dharma setiap kebaktian Minggu pagi. | Wajib (P0) |
| **FR-04** | **Kegiatan Adik Asuh & Dokumentasi Penyaluran** | Menampilkan daftar berita/dokumentasi kegiatan penyaluran bantuan dan aktivitas adik asuh (sebagai wujud transparansi untuk Donatur Sekali Jalan). Data ini bersifat **dinamis** (diambil dari database yang dikelola Admin). | Wajib (P0) |
| **FR-05** | **Testimoni & Kesan Pesan (Adik Asuh Wisuda & Donatur)** | Menampilkan kutipan kesan, pesan, dan cerita sukses dari beberapa Adik Asuh yang telah lulus/wisuda serta testimoni donatur. (Data statis diatur di awal). | Wajib (P0) |
| **FR-06** | **FAQ (Tanya Jawab)** | Menampilkan daftar pertanyaan umum beserta jawabannya dalam format *accordion* (buka-tutup), seperti perbedaan Kakak Asuh vs Donatur, Donatur Tetap vs Sekali Jalan, cara konfirmasi donasi, dan mekanisme penyaluran dana. | Wajib (P0) |
| **FR-07** | **Floating WhatsApp Button** | Tombol melayang di pojok kanan bawah layar agar calon donatur bisa langsung menghubungi WhatsApp Layanan Kakak Asuh kapan saja. | Wajib (P0) |

### 3.2 Sisi Pengelola / Kakak Asuh (Admin Panel / Backoffice)
Menggunakan **Django Built-in Admin Panel** yang dikustomisasi agar ramah pengguna bagi 1 orang Admin Kakak Asuh.

| Kode | Fitur Admin | Deskripsi Kebutuhan Fitur | Prioritas |
| :--- | :--- | :--- | :--- |
| **ADM-01** | **Autentikasi Admin** | Halaman Login khusus untuk 1 orang pengurus Kakak Asuh menggunakan *username* dan *password*. | Wajib (P0) |
| **ADM-02** | **Manajemen Berita / Kegiatan (CRUD)** | Tabel pengelolaan informasi kegiatan yang memungkinkan Admin untuk:<br>- **Menambah (Create):** Judul kegiatan, tanggal kegiatan, foto dokumentasi, dan isi deskripsi/artikel.<br>- **Mengubah (Update):** Mengedit tulisan atau mengganti foto.<br>- **Menghapus (Delete):** Menghapus berita kegiatan dari website. | Wajib (P0) |

---

## 4. Alur Pengguna Utama (User Flows)

### 4.1 Alur Pendaftaran Donatur Tetap
1. Pengunjung membuka Website Layanan Kakak Asuh VVD.
2. Membaca informasi pada bagian **Pilihan Skema Donasi (Donatur Tetap)**.
3. Mengklik tombol **"Daftar Jadi Donatur Tetap"**.
4. Sistem mengarahkan otomatis ke aplikasi WhatsApp menuju nomor resmi Kakak Asuh dengan teks pembuka otomatis.
5. Pengurus Kakak Asuh membalas pesan dan mendata donatur (proses pengingat bulanan oleh adik asuh dan pengiriman laporan perkembangan selanjutnya berjalan via WhatsApp).

### 4.2 Alur Donasi Sekali Jalan (Transfer Bank / QRIS)
1. Pengunjung membuka Website dan mengklik **"Donasi Sekarang"**.
2. Pengunjung memindai (*scan*) gambar **QRIS** atau menyalin **Nomor Rekening Bank** Layanan Kakak Asuh VVD.
3. Pengunjung melakukan transfer melalui aplikasi *mobile banking* atau *e-wallet* masing-masing.
4. Pengunjung mengklik tombol **"Kirim Bukti Transfer via WhatsApp"**.
5. Pengunjung mengirimkan foto/tangkapan layar bukti transfer ke WhatsApp Admin Kakak Asuh.

### 4.3 Alur Update Berita Kegiatan oleh Admin Kakak Asuh
1. Admin membuka halaman `/admin` dan masuk menggunakan akun pengurus.
2. Memilih menu tabel **"Kegiatan & Dokumentasi"**.
3. Mengklik **"Tambah Kegiatan"** untuk mengunggah foto dan artikel baru, atau memilih data yang ada untuk diubah/dihapus.
4. Mengklik **"Simpan"**, dan perubahan langsung tampil secara otomatis di halaman depan website.

---

## 5. Spesifikasi Teknis (Technical Specifications)

### 5.1 Arsitektur & Tech Stack
* **Backend Framework:** Python **Django** (memanfaatkan fitur *Built-in Admin Panel* untuk CRUD berita dan ORM).
* **Frontend Styling:** **HTML5 + Tailwind CSS** (memudahkan kustomisasi warna dan tata letak sesuai referensi Dribbble).
* **Frontend Interactivity:** **Vanilla JavaScript** (untuk fitur salin nomor rekening, *modal* perbesar QRIS, navigasi *mobile*, dan *accordion* FAQ).
* **Database:** **SQLite** (untuk pengembangan awal/MVP) atau **PostgreSQL** (untuk *production*).

### 5.2 Skema Database (`models.py`)
Karena data statistik jumlah adik asuh, daerah, dan testimoni wisuda diatur secara statis di awal pada kode *template*, database hanya memerlukan satu tabel utama di samping tabel bawaan autentikasi Django:

**Model: `ActivityPost` (Dokumentasi Kegiatan & Penyaluran)**
* `id`: `AutoField` (Primary Key)
* `title`: `CharField(max_length=200)` — Judul kegiatan penyaluran atau acara adik asuh
* `slug`: `SlugField(unique=True)` — URL ramah SEO otomatis dari judul
* `thumbnail`: `ImageField(upload_to='activities/')` — Foto dokumentasi kegiatan
* `content`: `TextField()` — Deskripsi lengkap kegiatan
* `activity_date`: `DateField()` — Tanggal kegiatan berlangsung
* `is_published`: `BooleanField(default=True)` — Status tayang di halaman publik
* `created_at`: `DateTimeField(auto_now_add=True)` — Waktu pembuatan data

### 5.3 Kebutuhan Non-Fungsional (Non-Functional Requirements)
1. **Desain Responsif (Mobile-First):** Tampilan wajib optimal di layar ponsel pintar karena mayoritas pengguna akan langsung berinteraksi dengan aplikasi WhatsApp dan *mobile banking*.
2. **Optimasi Media:** Gambar QRIS harus tajam dan mudah dipindai, sementara foto dokumentasi kegiatan harus terkompresi dengan baik agar waktu muat halaman (*page load*) tetap cepat.
3. **Keamanan:** Menggunakan proteksi bawaan Django (CSRF, XSS protection, dan amankan *endpoint* `/admin`).

---

## 6. Batasan Proyek (Out of Scope - Fase 1 / MVP)
1. Tidak menggunakan integrasi *Payment Gateway* otomatis (konfirmasi dilakukan manual via WhatsApp).
2. Tidak ada sistem registrasi atau *login dashboard* untuk Donatur di dalam website.
3. Tidak ada pengiriman pengingat atau laporan otomatis dari sistem website (dilakukan via WhatsApp).
4. Tidak menampilkan data pribadi detail per individu Adik Asuh secara terbuka.