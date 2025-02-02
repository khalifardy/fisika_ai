# Hubungan Limit dengan Optimisasi

## Pendahuluan
Konsep limit merupakan salah satu fondasi penting dalam analisis matematika dan memiliki peran krusial dalam teori optimisasi. Dokumen ini akan mengeksplorasi bagaimana limit berperan dalam berbagai aspek optimisasi, dari definisi dasar hingga aplikasi praktis.

## Dasar Teori Limit dalam Optimisasi

### Definisi Formal
Dalam konteks optimisasi, limit sering muncul dalam bentuk:

$$ \lim_{x \to a} f(x) = L $$

dimana $f(x)$ adalah fungsi objektif yang ingin kita optimasi, dan $L$ adalah nilai limit yang kita cari. Dalam optimisasi, kita seringkali mencari nilai $x$ dimana fungsi mencapai nilai ekstremum (maksimum atau minimum).

### Kontinuitas dan Diferensiabilitas
Limit membantu kita memahami sifat-sifat penting fungsi untuk optimisasi:

1. Kontinuitas:
$$ \lim_{h \to 0} f(x + h) = f(x) $$

2. Diferensiabilitas:
$$ f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} $$

## Peran Limit dalam Metode Optimisasi

### 1. Necessary Conditions untuk Optimum
Kondisi perlu untuk titik optimal melibatkan limit dalam bentuk turunan:

$$ \frac{d}{dx}f(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = 0 $$

### 2. Sufficient Conditions
Kondisi cukup melibatkan turunan kedua:

$$ \frac{d^2}{dx^2}f(x) = \lim_{h \to 0} \frac{f''(x + h) - f''(x)}{h} > 0 \text{ (minimum)} $$
$$ \frac{d^2}{dx^2}f(x) = \lim_{h \to 0} \frac{f''(x + h) - f''(x)}{h} < 0 \text{ (maximum)} $$

### 3. Convergence Analysis
Dalam analisis konvergensi algoritma optimisasi:

$$ \lim_{n \to \infty} \|x_{n+1} - x_n\| = 0 $$

## Aplikasi dalam Metode Numerik

### 1. Gradient Descent
Limit berperan dalam menentukan arah penurunan:

$$ x_{k+1} = x_k - \alpha \lim_{h \to 0} \frac{f(x_k + h) - f(x_k)}{h} $$

### 2. Newton's Method
Metode Newton menggunakan aproksimasi linear melalui limit:

$$ x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)} $$

### 3. Sequence Limits dalam Iterative Methods
$$ \lim_{k \to \infty} x_k = x^* $$

dimana $x^*$ adalah solusi optimal.

## Optimisasi dengan Constraints

### 1. KKT Conditions
Kondisi Karush-Kuhn-Tucker melibatkan limit dalam bentuk:

$$ \nabla f(x^*) + \sum_{i=1}^m \lambda_i \nabla g_i(x^*) = 0 $$

### 2. Barrier Methods
Metode barrier menggunakan sequence dari masalah unconstrained:

$$ \lim_{t \to \infty} \min_x \{f(x) + \frac{1}{t}\phi(x)\} $$

dimana $\phi(x)$ adalah fungsi barrier.

## Aplikasi Praktis

### 1. Machine Learning
Dalam deep learning, limit muncul dalam:
$$ \lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n L(y_i, f(x_i; \theta)) $$

### 2. Control Theory
Dalam kontrol optimal:
$$ J = \lim_{T \to \infty} \int_0^T L(x(t), u(t))dt $$

## Convergence Rate Analysis

### 1. Linear Convergence
$$ \lim_{k \to \infty} \frac{\|x_{k+1} - x^*\|}{\|x_k - x^*\|} = r < 1 $$

### 2. Quadratic Convergence
$$ \lim_{k \to \infty} \frac{\|x_{k+1} - x^*\|}{\|x_k - x^*\|^2} = M < \infty $$

## Kesimpulan
Pemahaman mendalam tentang limit sangat penting dalam:
1. Memahami sifat-sifat fungsi yang dioptimasi
2. Menganalisis konvergensi algoritma optimisasi
3. Mengembangkan metode optimisasi baru
4. Mengevaluasi performa algoritma optimisasi

## Referensi
* Optimization Theory and Methods (Wenyu Sun, Ya-Xiang Yuan)
* Convex Optimization (Boyd & Vandenberghe)
* Numerical Optimization (Nocedal & Wright)
