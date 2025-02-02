# Dokumentasi Kasus Khusus dalam Limit

## A. Kasus-Kasus Khusus dalam Limit

### 1. Limit yang Tidak Ada (DNE - Does Not Exist)

#### 1.1 Limit Tak Hingga
$$ \lim_{x \to 1} \frac{1}{x-1} = \infty $$

Karakteristik:
- Fungsi mendekati tak hingga positif atau negatif
- Grafik memiliki asimtot vertikal
- Biasanya terjadi pada pembagian dengan nol

#### 1.2 Limit Osilasi
$$ \lim_{x \to 0} \sin(\frac{1}{x}) \text{ DNE} $$

Karakteristik:
- Fungsi berosilasi tanpa batas
- Tidak memiliki nilai limit tunggal
- Frekuensi osilasi meningkat mendekati titik limit

#### 1.3 Limit Jump Discontinuity
$$ f(x) = \begin{cases} 
1 & x < 0 \\
2 & x > 0
\end{cases} $$

Karakteristik:
- Nilai limit kiri dan kanan berbeda
- Terdapat lompatan nilai pada titik diskontinuitas
- Limit tidak ada pada titik diskontinuitas

### 2. Indeterminate Forms

#### 2.1 Bentuk 0/0
$$ \lim_{x \to 0} \frac{\sin x}{x} = 1 $$

Karakteristik:
- Memerlukan manipulasi aljabar atau L'Hopital
- Sering muncul dalam aplikasi trigonometri
- Dapat menghasilkan nilai finite

#### 2.2 Bentuk ∞/∞
$$ \lim_{x \to \infty} \frac{x^2+1}{x^2-1} = 1 $$

Karakteristik:
- Memerlukan pembagian dengan pangkat tertinggi
- Sering muncul dalam fungsi rasional
- Hasil bisa konvergen ke nilai tertentu

#### 2.3 Bentuk 0·∞
$$ \lim_{x \to \infty} x\cdot e^{-x} = 0 $$

Karakteristik:
- Dapat diubah ke bentuk lain (0/0 atau ∞/∞)
- Memerlukan manipulasi aljabar
- Sering muncul dalam aplikasi eksponensial

## B. Template Hasil Pengamatan

### Eksperimen #[Nomor]

**Fungsi yang Diamati:**
$$ f(x) = [masukkan fungsi] $$

**Jenis Kasus Khusus:**
[Identifikasi jenis kasus khusus yang terjadi]

**Karakteristik Visual:**
1. Perilaku grafik:
   - [Deskripsi perilaku]
   - [Pola yang teramati]
   - [Keunikan visual]

2. Titik-titik kritis:
   - [Identifikasi titik discontinuity]
   - [Perilaku di sekitar titik kritis]
   - [Nilai-nilai penting]

**Analisis Matematis:**
1. Pendekatan dari kiri:
   $$ \lim_{x \to a^-} f(x) = [nilai] $$

2. Pendekatan dari kanan:
   $$ \lim_{x \to a^+} f(x) = [nilai] $$

3. Metode penyelesaian:
   - [Langkah-langkah penyelesaian]
   - [Teknik yang digunakan]
   - [Justifikasi metode]

**Kesimpulan:**
[Ringkasan temuan dan implikasi]

**Catatan Tambahan:**
[Observasi khusus atau insight menarik]

### Contoh Pengisian Template

**Fungsi yang Diamati:**
$$ f(x) = \frac{\sin x}{x} $$

**Jenis Kasus Khusus:**
Indeterminate Form 0/0

**Karakteristik Visual:**
1. Perilaku grafik:
   - Fungsi kontinu di semua titik kecuali x = 0
   - Grafik mendekati garis y = 1 saat x mendekati 0
   - Osilasi teredam saat x menjauh dari 0

2. Titik-titik kritis:
   - x = 0 adalah titik yang perlu investigasi khusus
   - Fungsi terdefinisi untuk semua x ≠ 0
   - Memiliki simetri terhadap sumbu y

[Lanjutkan dengan bagian lain sesuai kebutuhan...]

## C. Tips Dokumentasi

1. Selalu sertakan visualisasi grafik jika memungkinkan
2. Dokumentasikan langkah-langkah penyelesaian secara detail
3. Catat pola-pola menarik yang ditemukan
4. Hubungkan dengan aplikasi praktis jika ada
5. Bandingkan dengan kasus-kasus serupa

## Referensi
* Calculus (Stewart)
* Advanced Calculus (Fitzpatrick)
* Real Analysis (Rudin)
