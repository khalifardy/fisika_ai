
# Analisis Penyelesaian Soal Limit Matematika

## Soal 1: Limit \((1 + 1/x)^x\)

Pada penyelesaian pertama, terdapat kesalahan dalam menentukan nilai limit:

$$
\lim_{x \to \infty} \bigl(1 + \tfrac{1}{x}\bigr)^x = 1
$$

**(Salah ❌)**

Nilai yang benar adalah:

$$
\lim_{x \to \infty} \bigl(1 + \tfrac{1}{x}\bigr)^x = e \approx 2.71828\dots
$$

**(Benar ✓)**

Ini merupakan salah satu limit paling penting dalam kalkulus karena mendefinisikan bilangan \(e\) (bilangan Euler). Bilangan \(e\) memiliki peran sangat penting dalam matematika, terutama dalam:

- Perhitungan bunga majemuk
- Pertumbuhan eksponensial
- Fungsi logaritma natural
- Turunan dan integral

---

## Soal 2: Limit \(\sin x / x\)

Penyelesaian untuk limit kedua sudah tepat:

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$

**(Benar ✓)**

Pembuktian menggunakan *teorema apit* (*squeeze theorem*) sangat baik dengan langkah-langkah:

1. Dimulai dari ketidaksamaan dasar trigonometri: \(-1 \le \sin x \le 1\)
2. Membagi ketidaksamaan dengan \(x\) (mempertimbangkan tanda saat \(x\) positif/negatif):

   \(-1 \le \frac{\sin x}{x} \le 1\)
3. Karena limit kiri dan kanan sama dengan 1, maka berdasarkan teorema apit:

   $$
   \lim_{x \to 0} \frac{\sin x}{x} = 1
   $$

---

## Soal 3: Limit Bentuk Tak Tentu

Penyelesaian untuk limit ketiga juga sudah benar:

$$
\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = 2
$$

**(Benar ✓)**

Ini merupakan contoh limit **bentuk tak tentu** \(\frac{0}{0}\) yang bisa diselesaikan dengan faktorisasi:

1. Faktorkan pembilang: \((x + 1)(x - 1)\)
2. Sederhanakan dengan pembagi \((x - 1)\)
3. Hasil limitnya menjadi:

   $$
   \lim_{x \to 1} (x + 1) = 2
   $$

Limit ini sebenarnya merupakan definisi turunan dari fungsi \(f(x) = x^2\) di titik \(x = 1\).

---

## Rekomendasi Perbaikan

1. Untuk limit pertama, perbaiki jawaban dari 1 menjadi \(e\).
2. Untuk limit kedua, penyelesaian sudah sempurna dan bisa dijadikan contoh penggunaan teorema apit yang baik.
3. Untuk limit ketiga, meskipun jawaban benar, akan lebih baik jika ditambahkan langkah-langkah faktorisasi secara eksplisit.

---

## Catatan Penting

Dalam menyelesaikan soal limit:

1. Perhatikan bentuk-bentuk limit khusus seperti \(\bigl(1 + \tfrac{1}{x}\bigr)^x\) yang menuju \(e\).
2. Gunakan *teorema apit* untuk limit fungsi trigonometri.
3. Untuk bentuk tak tentu, coba selesaikan dengan faktorisasi terlebih dahulu.
4. Selalu periksa apakah hasil akhir masuk akal dengan mensubstitusi nilai-nilai di sekitar titik limit.

---
