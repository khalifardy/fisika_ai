# Gradient Descent dalam Optimasi

Gradient Descent adalah salah satu algoritma optimasi yang paling populer digunakan dalam berbagai bidang, terutama dalam pembelajaran mesin dan statistik. Algoritma ini digunakan untuk menemukan nilai minimum (atau maksimum) dari suatu fungsi dengan mengikuti arah negatif gradien fungsi tersebut.

## Daftar Isi

1. [Pendahuluan](#pendahuluan)
2. [Apa itu Gradient Descent?](#apa-itu-gradient-descent)
3. [Formulasi Matematis](#formulasi-matematis)
4. [Jenis-Jenis Gradient Descent](#jenis-jenis-gradient-descent)
   - [Batch Gradient Descent](#batch-gradient-descent)
   - [Stochastic Gradient Descent (SGD)](#stochastic-gradient-descent-sgd)
   - [Mini-Batch Gradient Descent](#mini-batch-gradient-descent)
5. [Algoritma Gradient Descent](#algoritma-gradient-descent)
6. [Kriteria Konvergensi](#kriteria-konvergensi)
7. [Tingkat Pembelajaran (Learning Rate) dan Pentingnya](#tingkat-pembelajaran-learning-rate-dan-pentingnya)
8. [Contoh Penerapan](#contoh-penerapan)
9. [Aplikasi Gradient Descent](#aplikasi-gradient-descent)
10. [Kelebihan dan Kekurangan](#kelebihan-dan-kekurangan)
11. [Varian Gradient Descent](#varian-gradient-descent)
    - [Momentum](#momentum)
    - [AdaGrad](#adagrad)
    - [RMSProp](#rmsprop)
    - [Adam](#adam)
12. [Referensi](#referensi)

---

## Pendahuluan

Optimasi adalah proses mencari nilai terbaik (maksimum atau minimum) dari suatu fungsi. Dalam banyak aplikasi, terutama dalam pembelajaran mesin, kita sering kali perlu meminimalkan fungsi kerugian (loss function) untuk menemukan model yang paling sesuai dengan data.

Gradient Descent adalah metode iteratif yang digunakan untuk menemukan nilai minimum dari fungsi yang dapat di-diferensiasikan. Algoritma ini sangat efisien dan mudah diimplementasikan, membuatnya menjadi pilihan utama dalam berbagai aplikasi optimasi.

## Apa itu Gradient Descent?

Gradient Descent adalah algoritma optimasi yang digunakan untuk meminimalkan fungsi dengan bergerak ke arah negatif gradien fungsi tersebut. Gradien menunjukkan arah tercepat peningkatan fungsi, sehingga bergerak ke arah negatif gradien berarti kita bergerak ke arah tercepat penurunan fungsi.

## Formulasi Matematis

Misalkan kita memiliki fungsi yang ingin diminimalkan, \( f(\theta) \), di mana \( \theta \) adalah vektor parameter. Gradient Descent melakukan update parameter \( \theta \) dengan rumus:

$$
\theta := \theta - \alpha \nabla f(\theta)
$$

Di mana:

- \( \alpha \) adalah tingkat pembelajaran (learning rate), sebuah bilangan positif yang menentukan ukuran langkah yang diambil.
- \( \nabla f(\theta) \) adalah gradien dari fungsi \( f \) di titik \( \theta \).

### Proses Iteratif

Proses iteratif dari Gradient Descent dapat dituliskan sebagai:

$$
\theta^{(k+1)} = \theta^{(k)} - \alpha \nabla f(\theta^{(k)})
$$

Di mana \( k \) menunjukkan iterasi ke-\( k \).

## Jenis-Jenis Gradient Descent

### Batch Gradient Descent

Batch Gradient Descent menggunakan seluruh dataset untuk menghitung gradien pada setiap iterasi. Metode ini stabil dan konvergen menuju minimum global (untuk fungsi convex).

**Kelebihan:**

- Konvergensi stabil.
- Akurat dalam perhitungan gradien.

**Kekurangan:**

- Lambat pada dataset besar karena harus memproses seluruh data setiap iterasi.

### Stochastic Gradient Descent (SGD)

Stochastic Gradient Descent menghitung gradien menggunakan satu sampel data acak pada setiap iterasi. Metode ini lebih cepat pada dataset besar dan dapat melewati minimum lokal.

**Kelebihan:**

- Lebih cepat pada dataset besar.
- Dapat keluar dari minimum lokal.

**Kekurangan:**

- Update gradien yang lebih bising, sehingga konvergensi kurang stabil.

### Mini-Batch Gradient Descent

Mini-Batch Gradient Descent adalah kompromi antara Batch dan Stochastic Gradient Descent. Metode ini menggunakan subset kecil (mini-batch) dari dataset untuk menghitung gradien pada setiap iterasi.

**Kelebihan:**

- Lebih cepat daripada Batch Gradient Descent.
- Lebih stabil daripada SGD.
- Memanfaatkan komputasi vektor dan paralelisasi.

**Kekurangan:**

- Memerlukan pemilihan ukuran mini-batch yang tepat.

## Algoritma Gradient Descent

Berikut adalah langkah-langkah umum dari algoritma Gradient Descent:

1. **Inisialisasi Parameter:**

   - Pilih nilai awal untuk parameter \( \theta \).
2. **Iterasi:**

   - Hitung gradien \( \nabla f(\theta) \).
   - Update parameter:
     $$
     \theta := \theta - \alpha \nabla f(\theta)
     $$
3. **Konvergensi:**

   - Ulangi langkah iterasi hingga perubahan pada fungsi kerugian atau parameter berada di bawah ambang batas tertentu.

### Pseudocode

```pseudo
initialize θ
repeat until convergence:
    calculate gradient ∇f(θ)
    update θ = θ - α * ∇f(θ)
end repeat
```
