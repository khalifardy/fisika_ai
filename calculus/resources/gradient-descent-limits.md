# Hubungan Antara Limit dan Gradient Descent

## Pendahuluan
Dalam matematika optimisasi dan machine learning, gradient descent dan konsep limit memiliki hubungan yang mendalam dan saling terkait. Dokumen ini akan menjelaskan bagaimana kedua konsep ini berinteraksi dan saling melengkapi.

## Definisi Dasar

### Gradient Descent
Gradient descent adalah algoritma optimisasi iteratif yang bertujuan untuk menemukan minimum dari suatu fungsi. Algoritma ini bekerja dengan mengikuti gradien negatif dari fungsi target untuk mencapai nilai minimum.

Rumus update parameter dalam gradient descent adalah:

$$ \theta_{new} = \theta_{current} - \alpha \nabla J(\theta) $$

dimana:
- $\theta$ adalah parameter yang kita optimalkan
- $\alpha$ adalah learning rate
- $\nabla J(\theta)$ adalah gradien dari fungsi biaya $J(\theta)$

### Konsep Limit dalam Turunan
Gradien itu sendiri didefinisikan menggunakan konsep limit:

$$ \nabla J(\theta) = \lim_{h \to 0} \frac{J(\theta + h) - J(\theta)}{h} $$

## Hubungan Mendalam

### 1. Konvergensi dan Limit
Ketika gradient descent konvergen, kita sebenarnya sedang mengamati suatu limit:

$$ \lim_{n \to \infty} \theta_n = \theta_{optimal} $$

dimana $n$ adalah jumlah iterasi.

### 2. Learning Rate dan Epsilon
Konsep $\epsilon$ dalam limit mirip dengan peran learning rate ($\alpha$) dalam gradient descent:
- Dalam limit: Kita mencari nilai yang cukup dekat dalam radius $\epsilon$
- Dalam gradient descent: Learning rate menentukan seberapa besar langkah menuju minimum

$$ |\theta_{n+1} - \theta_n| < \epsilon $$

### 3. Analisis Konvergensi
Untuk fungsi konveks yang diferensiabel dengan gradient Lipschitz continu $L$, kita memiliki:

$$ J(\theta_k) - J(\theta^*) \leq \frac{\|\theta_0 - \theta^*\|^2}{2\alpha k} $$

dimana:
- $\theta^*$ adalah nilai optimal
- $k$ adalah jumlah iterasi
- $\alpha$ adalah learning rate yang memenuhi $\alpha \leq \frac{1}{L}$

## Contoh Praktis
Misalkan kita memiliki fungsi kuadrat sederhana:

$$ J(\theta) = \theta^2 $$

Gradiennya adalah:

$$ \nabla J(\theta) = 2\theta $$

Update gradient descent menjadi:

$$ \theta_{k+1} = \theta_k - 2\alpha\theta_k = (1-2\alpha)\theta_k $$

Untuk konvergensi, kita memerlukan $|1-2\alpha| < 1$, yang memberikan batasan pada learning rate:

$$ 0 < \alpha < 1 $$

## Kesimpulan
Pemahaman tentang limit sangat penting dalam:
1. Mendefinisikan gradien yang digunakan dalam algoritma
2. Menganalisis konvergensi algoritma
3. Memilih parameter learning rate yang tepat
4. Memahami perilaku algoritma saat mendekati nilai optimal

## Referensi Lebih Lanjut
* Calculus: A Complete Course (Adams & Essex)
* Optimization Methods in Machine Learning (Nocedal & Wright)
* Deep Learning (Goodfellow, Bengio, & Courville)
