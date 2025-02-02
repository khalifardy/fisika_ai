# Backpropagation dalam Neural Network

Backpropagation adalah algoritma kunci dalam pelatihan jaringan saraf (neural networks). Algoritma ini memungkinkan jaringan untuk belajar dari data dengan mengoptimalkan bobot (weights) melalui perhitungan gradien fungsi loss. Backpropagation sangat penting dalam mencapai performa tinggi pada berbagai aplikasi seperti pengenalan gambar, pemrosesan bahasa alami, dan banyak lagi.

## Daftar Isi

1. [Pendahuluan](#pendahuluan)
2. [Apa itu Backpropagation?](#apa-itu-backpropagation)
3. [Formulasi Matematis](#formulasi-matematis)
4. [Langkah-Langkah Backpropagation](#langkah-langkah-backpropagation)
   - [Forward Pass](#forward-pass)
   - [Backward Pass](#backward-pass)
5. [Fungsi Aktivasi](#fungsi-aktivasi)
6. [Algoritma Backpropagation](#algoritma-backpropagation)
7. [Optimasi dengan Backpropagation](#optimasi-dengan-backpropagation)
8. [Contoh Penerapan](#contoh-penerapan)
9. [Aplikasi Backpropagation](#aplikasi-backpropagation)
10. [Kelebihan dan Kekurangan](#kelebihan-dan-kekurangan)
11. [Varian Backpropagation](#varian-backpropagation)
    - [Momentum](#momentum)
    - [AdaGrad](#adagrad)
    - [RMSProp](#rmsprop)
    - [Adam](#adam)
12. [Referensi](#referensi)

---

## Pendahuluan

Neural networks adalah model komputasi yang terinspirasi oleh struktur dan fungsi otak manusia. Mereka terdiri dari lapisan-lapisan neuron yang saling terhubung, di mana setiap koneksi memiliki bobot yang menentukan kekuatan hubungan antar neuron. Tujuan utama pelatihan jaringan saraf adalah menemukan bobot yang optimal sehingga jaringan dapat membuat prediksi yang akurat.

Backpropagation adalah algoritma yang digunakan untuk melatih jaringan saraf dengan menyesuaikan bobot berdasarkan kesalahan prediksi. Algoritma ini bekerja dengan menghitung gradien dari fungsi loss terhadap setiap bobot dalam jaringan, memungkinkan optimasi yang efisien.

## Apa itu Backpropagation?

**Backpropagation** adalah singkatan dari "backward propagation of errors". Ini adalah metode untuk menganalisis dan memperbarui bobot jaringan saraf berdasarkan kesalahan yang dihasilkan selama forward pass. Dengan menghitung gradien fungsi loss relatif terhadap setiap bobot, backpropagation memungkinkan jaringan untuk belajar dari kesalahan dan meningkatkan akurasi prediksi.

Backpropagation terdiri dari dua fase utama:

1. **Forward Pass**: Menghitung output jaringan dan fungsi loss.
2. **Backward Pass**: Menghitung gradien dan memperbarui bobot.

## Formulasi Matematis

Misalkan kita memiliki jaringan saraf feedforward dengan satu atau lebih lapisan tersembunyi. Fungsi loss $( L )$ mengukur kesalahan antara prediksi jaringan $( \hat{y} )$ dan nilai aktual $( y )$. Tujuan backpropagation adalah menemukan gradien $( \frac{\partial L}{\partial w} )$ untuk setiap bobot \( w \) dalam jaringan, sehingga kita dapat mengupdate bobot menggunakan aturan pembaruan seperti Gradient Descent.

### Fungsi Loss

Contoh fungsi loss yang umum digunakan adalah **Mean Squared Error (MSE)**:

$$
L = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Di mana:

- $( n )$ adalah jumlah sampel.
- $( y_i )$ adalah nilai aktual.
- $( \hat{y}_i )$ adalah nilai prediksi oleh jaringan.

### Update Bobot

Pembaruan bobot dilakukan menggunakan rumus:

$$
w := w - \alpha \frac{\partial L}{\partial w}
$$

Di mana:

- $( \alpha )$ adalah **learning rate**.
- $( \frac{\partial L}{\partial w} )$ adalah gradien fungsi loss terhadap bobot \( w \).

## Langkah-Langkah Backpropagation

### Forward Pass

1. **Input Layer**: Menerima input data.
2. **Hidden Layers**: Menghitung aktivasi setiap neuron berdasarkan bobot dan fungsi aktivasi.
3. **Output Layer**: Menghasilkan prediksi \( \hat{y} \).
4. **Fungsi Loss**: Menghitung nilai loss \( L \) berdasarkan prediksi dan nilai aktual.

### Backward Pass

1. **Hitung Gradien Loss**: Menghitung turunan fungsi loss terhadap output jaringan.
2. **Propagasi Gradien Mundur**: Menghitung gradien untuk setiap bobot dari lapisan output hingga lapisan input menggunakan aturan rantai.
3. **Update Bobot**: Menyesuaikan bobot menggunakan gradien yang telah dihitung.

## Fungsi Aktivasi

Fungsi aktivasi menentukan output neuron berdasarkan input yang diterima. Fungsi ini memperkenalkan non-linearitas ke dalam jaringan, memungkinkan jaringan untuk mempelajari hubungan kompleks dalam data.

Beberapa fungsi aktivasi yang umum digunakan:

- **Sigmoid**:
  $$
  \sigma(x) = \frac{1}{1 + e^{-x}}
  $$
- **ReLU (Rectified Linear Unit)**:
  $$
  \text{ReLU}(x) = \max(0, x)
  $$
- **Tanh (Hyperbolic Tangent)**:
  $$
  \tanh(x) = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}
  $$

## Algoritma Backpropagation

Berikut adalah langkah-langkah umum dari algoritma Backpropagation:

1. **Inisialisasi Bobot**:

   - Bobot diinisialisasi secara acak, sering kali dengan distribusi kecil untuk memulai proses pembelajaran.
2. **Forward Pass**:

   - Hitung output setiap neuron di semua lapisan.
   - Hitung fungsi loss $( L )$.
3. **Backward Pass**:

   - Hitung turunan fungsi loss terhadap output (gradien awal).
   - Propagasi gradien dari lapisan output ke lapisan input.
   - Hitung gradien untuk setiap bobot menggunakan aturan rantai.
4. **Update Bobot**:

   - Sesuaikan bobot berdasarkan gradien yang telah dihitung dan learning rate $( \alpha )$.
5. **Iterasi**:

   - Ulangi proses forward dan backward pass hingga konvergensi (nilai loss tidak berkurang secara signifikan) atau hingga mencapai jumlah iterasi maksimum.

### Pseudocode

```pseudo
initialize weights randomly
repeat until convergence:
    for each training example:
        # Forward Pass
        output = forward_pass(input, weights)
    
        # Compute Loss
        loss = compute_loss(output, target)
    
        # Backward Pass
        gradients = backward_pass(loss, weights)
    
        # Update Weights
        weights = weights - learning_rate * gradients
    end for
end repeat
```
