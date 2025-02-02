# Dokumentasi Pembelajaran (day 2)

## Memahami Konsep Turunan dan Interpretasi Geometrisnya

### 1. Bagaimana turunan menggambarkan rate of change ?

#### 1.1. Penjelasan Konseptual

Turunan merupakan konsep fundamental dalam kalkulus yang menggambarkan bagaimana suatu fungsi berubah terhadap variabel bebasnya. Dalam konteks matematika, turunan memberikan kita cara yang presisi untuk mengukur seberapa cepat perubahan terjadi pada suatu titik tertentu.

#### 1.2. Definisi Matematis

Secara matematis, turunan suatu fungsi $f(x)$ didefinisikan sebagai:

$f'(x) = \lim\limits_{h \to 0} \frac{f(x+h) - f(x)}{h}$

Definisi ini memiliki interpretasi geometris yang mendalam: turunan pada suatu titik merupakan kemiringan garis singgung kurva pada titik tersebut. Kemiringan ini dapat dituliskan sebagai:

$m = \lim\limits_{x_1 \to x_0} \frac{f(x_1) - f(x_0)}{x_1 - x_0}$

#### 1.3. Rate of Change dalam Konteks Nyata

##### 1.3.1. Kecepatan sebagai Rate of Change

Misalkan $s(t)$ adalah fungsi posisi terhadap waktu. Kecepatan, yang merupakan turunan dari posisi terhadap waktu, dapat ditulis sebagai:

$v(t) = s'(t) = \lim\limits_{h \to 0} \frac{s(t+h) - s(t)}{h}$

##### Contoh Numerik

Misalkan sebuah bola jatuh dengan fungsi posisi:

$s(t) = -4.9t^2 + 10t + 2$

Untuk mencari kecepatan pada waktu tertentu:

$v(t) = s'(t) = -9.8t + 10$

#### 1.4. Perbedaan Rate of Change

##### 1.4.1. Average Rate of Change

Rate of change rata-rata dihitung menggunakan interval waktu yang tetap:

$\frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$

##### 1.4.2. Instantaneous Rate of Change

Rate of change sesaat (turunan) adalah limit dari rate of change rata-rata saat interval mendekati nol:

$\frac{dy}{dx} = \lim\limits_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$

#### 1.5. Aturan-aturan Turunan Dasar

1. Aturan Power Rule:
   $\frac{d}{dx}(x^n) = nx^{n-1}$
2. Aturan Product Rule:
   $\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$
3. Aturan Chain Rule:
   $\frac{d}{dx}[f(g(x))] = f'(g(x))g'(x)$
4. Aturan Quotient Rule:
   $\frac{d}{dx}[\frac{f(x)}{g(x)}] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$

#### 1.6. Aplikasi dalam Berbagai Bidang

##### 1.6.1. Fisika

- Kecepatan: $v(t) = \frac{ds}{dt}$
- Percepatan: $a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2}$
- Daya: $P = \frac{dE}{dt}$

##### 1.6.2. Ekonomi

- Marginal cost: $MC = \frac{dTC}{dq}$
- Marginal revenue: $MR = \frac{dTR}{dq}$

##### 1.6.3. Biologi

Laju pertumbuhan populasi:
$\frac{dP}{dt} = rP(1-\frac{P}{K})$

#### 1.7. Kesimpulan

Turunan memberikan cara yang tepat untuk mengukur rate of change secara instan pada titik tertentu. Pemahaman yang mendalam tentang hubungan antara turunan dan rate of change memungkinkan kita untuk:

1. Menganalisis perubahan secara kuantitatif
2. Membuat prediksi tentang perilaku sistem
3. Mengoptimalkan proses dalam berbagai bidang aplikasi

#### 1.8. Catatan Tambahan

Untuk pemahaman yang lebih mendalam, penting untuk memperhatikan:

- Interpretasi geometris turunan sebagai kemiringan garis singgung
- Hubungan antara rata-rata dan nilai sesaat
- Aplikasi dalam pemecahan masalah dunia nyata

#### Referensi

- Stewart, J. (2020). Calculus: Early Transcendentals
- Thomas' Calculus
- Anton, H. Calculus with Analytic Geometry

### 2. Interpretasi geometris turunan

bahwa turunan merepresentasikan kemiringan (gradien) garis singgung pada titik tertentu pada sebuah fungsi.

Turunan secara geometris diinterpretasikan sebagai kemiringan (gradien) garis singgung pada kurva di setiap titik tertentu. Hal ini berlaku tidak hanya untuk fungsi kuadrat, tetapi untuk semua fungsi yang dapat diturunkan (differentiable). Berikut penjelasan yang lebih rinci:

#### 2.1. Key Components

1. Turunan f'(x) pada titik x₀ sama dengan kemiringan garis singgung pada kurva y = f(x) di titik (x₀, f(x₀)).
2. Kemiringan ini merepresentasikan laju perubahan sesaat dari fungsi tersebut di titik yang dimaksud..
3. Garis singgung adalah garis yang “menyentuh” kurva di tepat satu titik dan memiliki arah (kemiringan) yang sama dengan kurva di titik itu.

#### 2.2. Mathematical Expression

Jika kita memiliki fungsi  f(x),  maka kemiringan garis singgung pada titik x₀ diberikan oleh:

$ f'(x_0) = \lim\limits_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} $

#### 2.3. Catatan Penting

- Interpretasi ini berlaku untuk semua fungsi yang dapat diturunkan, bukan hanya fungsi kuadrat.
- Nilai turunan dapat positif (kemiringan ke atas), negatif (kemiringan ke bawah), atau nol (garis singgung mendatar).
- Pada titik-titik di mana turunan tidak ada, bisa jadi terdapat:
  - Sudut tajam (sudut yang tidak mulus).
  - Garis singgung vertikal.
  - Ketakselanjaran (diskontinuitas).

#### 2.4. Pemahaman Visual

Turunan pada titik mana pun menggambarkan:

- Derajat (tingkat) kemiringan kurva di titik tersebut.
- Laju perubahan sesaat.
- Arah pergerakan kurva (apakah sedang naik atau turun).

Interpretasi geometris ini sangat mendasar dalam kalkulus dan membantu memvisualisasikan konsep laju perubahan di berbagai bidang, mulai dari fisika hingga ekonomi.

### 3. Hubungan antara limit dan turunan

Limit dan turunan saling terkait erat. Definisi formal dari turunan adalah limit dari perubahan suatu fungsi terhadap perubahan variabel bebasnya, di mana perubahan variabel bebas tersebut mendekati nol.

### 4. Kasus-kasus khusus yang menarik

Berikut adalah beberapa **kasus-kasus khusus yang menarik pada turunan** dalam kalkulus beserta penjelasan dan contohnya:

#### 4.1. Turunan Fungsi Potongan (Piecewise Function)

**Penjelasan:**
Fungsi potongan adalah fungsi yang didefinisikan berbeda pada interval yang berbeda. Menentukan turunan fungsi potongan memerlukan pemeriksaan batas di titik potong untuk memastikan apakah turunan ada atau tidak.

**Contoh:**

$$
f(x) =
\begin{cases}
x^2 & \text{jika } x < 1 \\
2x + 1 & \text{jika } x \geq 1
\end{cases}
$$

Untuk menentukan turunan di \( x = 1 \), kita perlu memastikan bahwa nilai turunan dari kedua sisi sama. Jika tidak, turunan tidak ada di titik tersebut.

#### 4.2. Turunan Implisit

**Penjelasan:**
Ketika suatu fungsi didefinisikan secara implisit oleh sebuah persamaan yang melibatkan kedua variabel, kita menggunakan diferensiasi implisit untuk menemukan turunan.

**Contoh:**

Misalkan diberikan persamaan lingkaran:

$$
x^2 + y^2 = r^2
$$

Untuk menemukan \( \frac{dy}{dx} \), kita diferensiasikan kedua sisi terhadap \( x \):

$$
2x + 2y\frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{x}{y}
$$

#### 4.3. Turunan dari Fungsi Absolut (Absolute Value Function)

**Penjelasan:**
Fungsi nilai mutlak memiliki sudut tajam di titik tertentu, yang menyebabkan turunan tidak terdefinisi di titik tersebut.

**Contoh:**

$$
f(x) = |x|
$$

Turunan dari \( f(x) \) adalah:

$$
f'(x) =
\begin{cases}
1 & \text{jika } x > 0 \\
-1 & \text{jika } x < 0
\end{cases}
$$

Di \( x = 0 \), turunan tidak terdefinisi karena adanya perubahan tiba-tiba dari -1 ke 1.

#### 4.4. Turunan Logaritmik (Logarithmic Differentiation)

**Penjelasan:**
Teknik ini digunakan untuk mendiferensiasikan fungsi yang merupakan hasil perkalian, pembagian, atau perpangkatan dari beberapa fungsi, dengan mengambil logaritma terlebih dahulu.

**Contoh:**

Misalkan $( y = x^x )$. Mengambil logaritma:

$$
\ln y = x \ln x
$$

Diferensiasi kedua sisi:

$$
\frac{1}{y} \frac{dy}{dx} = \ln x + 1 \implies \frac{dy}{dx} = y (\ln x + 1) = x^x (\ln x + 1)
$$

#### 4.5. Turunan Parametrik

**Penjelasan:**
Ketika fungsi didefinisikan dalam bentuk parametrik, yaitu \( x(t) \) dan \( y(t) \), turunan \( \frac{dy}{dx} \) diperoleh dengan membagi \( \frac{dy}{dt} \) dengan \( \frac{dx}{dt} \).

**Contoh:**

Misalkan:

$$
x(t) = t^2, \quad y(t) = t^3
$$

Maka:

$$
\frac{dx}{dt} = 2t, \quad \frac{dy}{dt} = 3t^2
$$

Sehingga:

$$
\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} = \frac{3t^2}{2t} = \frac{3t}{2}
$$

#### 4.6. Turunan Tingkat Tinggi (Higher-Order Derivatives)

**Penjelasan:**
Turunan tingkat tinggi adalah turunan dari turunan sebelumnya. Misalnya, turunan kedua $( \frac{d^2y}{dx^2} )$ memberikan informasi tentang kelengkungan grafik fungsi.

**Contoh:**

Misalkan $( f(x) = x^3 )$.

$$
f'(x) = 3x^2
$$

$$
f''(x) = 6x
$$

$$
f'''(x) = 6
$$

#### 4.7. Derivatif di Titik Diskontinuitas atau Sudut Tajam

**Penjelasan:**
Di titik di mana fungsi tidak kontinu atau memiliki sudut tajam (seperti pada \( f(x) = |x| \) di \( x = 0 \)), turunan tidak terdefinisi.

**Contoh:**

Fungsi \( f(x) = |x| \) memiliki sudut tajam di \( x = 0 \), sehingga turunan tidak ada di titik tersebut.

#### 4.8. Turunan Fungsi Kompleks

**Penjelasan:**
Dalam analisis kompleks, turunan fungsi kompleks memiliki kondisi tambahan yang harus dipenuhi, seperti fungsi harus holomorfik (diferensiabel secara kompleks di seluruh domainnya).

**Contoh:**

Fungsi $( f(z) = z^2 )$, di mana $( z )$ adalah bilangan kompleks, memiliki turunan:

$$
f'(z) = 2z
$$

yang berlaku di seluruh bidang kompleks.

#### 4.9. Turunan Fungsi dengan Basis Variabel

**Penjelasan:**
Fungsi eksponensial atau logaritma dengan basis yang merupakan fungsi variabel memerlukan aplikasi aturan rantai.

**Contoh:**

Misalkan $( f(x) = a(x)^{b(x)} )$, misalnya $( f(x) = x^{\sin x} )$.

Menggunakan diferensiasi logaritmik:

$$
\ln f(x) = \sin x \cdot \ln x
$$

Diferensiasi:

$$
\frac{f'(x)}{f(x)} = \cos x \cdot \ln x + \frac{\sin x}{x}
$$

Sehingga:

$$
f'(x) = x^{\sin x} \left( \cos x \cdot \ln x + \frac{\sin x}{x} \right)
$$

#### 4.10. Derivatif Tak Terbatas (Unbounded Derivatives)

**Penjelasan:**
Beberapa fungsi memiliki turunan yang tidak terbatas di titik tertentu, meskipun fungsi tersebut tetap kontinu.

**Contoh:**

Fungsi $( f(x) = \sqrt{x} )$ memiliki turunan:

$$
f'(x) = \frac{1}{2\sqrt{x}}
$$

Di \( x = 0 \), \( f'(x) \) mendekati tak hingga, sehingga turunan tidak terbatas di titik tersebut.

#### 4.11. Keteraturan Turunan (Regularity of Derivatives)

**Penjelasan:**
Beberapa fungsi memiliki turunan yang ada hampir di semua titik, tetapi tidak kontinu, atau memiliki sifat keteraturan tertentu.

**Contoh:**

Fungsi Weierstrass adalah contoh klasik fungsi yang kontinu di semua titik tetapi tidak memiliki turunan di mana pun.

#### 4.12. Derivatif Parsial dalam Fungsi Multivariabel

**Penjelasan:**
Untuk fungsi yang memiliki lebih dari satu variabel, kita dapat mengambil turunan parsial terhadap masing-masing variabel.

**Contoh:**

Misalkan $( f(x, y) = x^2 y + \sin(xy) )$.

$$
\frac{\partial f}{\partial x} = 2xy + y \cos(xy)
$$

$$
\frac{\partial f}{\partial y} = x^2 + x \cos(xy)
$$

---

Kasus-kasus khusus ini menunjukkan kompleksitas dan keanekaragaman dalam konsep turunan. Memahami berbagai situasi ini sangat penting untuk mengaplikasikan kalkulus secara efektif dalam berbagai bidang matematika dan sains.
