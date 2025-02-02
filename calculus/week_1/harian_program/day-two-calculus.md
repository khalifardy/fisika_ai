# Rencana Pembelajaran: Hari Kedua

## Memahami Konsep Turunan dan Interpretasi Geometrisnya

### A. Refleksi Awal (15 menit)

Mulailah hari ini dengan mengulas konsep limit yang dipelajari kemarin. Perhatikan bagaimana limit akan menjadi fondasi untuk memahami turunan. Tuliskan pemahaman Anda tentang:

- Bagaimana limit menggambarkan perubahan yang sangat kecil
- Mengapa limit penting dalam matematika
- Hubungan limit dengan rate of change

### B. Sesi Teori (45 menit)

#### 1. Definisi Turunan (20 menit)

Pelajari dari Stewart Calculus dengan fokus pada:

- Definisi formal turunan sebagai limit
- Notasi Leibniz (dy/dx) dan notasi Newton (f'(x))
- Interpretasi turunan sebagai rate of change

Mari memahami turunan melalui contoh konkret:
Bayangkan Anda mengendarai sepeda. Speedometer menunjukkan kecepatan saat ini, yang sebenarnya adalah turunan dari posisi terhadap waktu. Setiap perubahan kecepatan adalah turunan kedua, yang kita rasakan sebagai percepatan atau perlambatan.

#### 2. Interpretasi Geometris (15 menit)

Tonton video Khan Academy tentang interpretasi geometris dengan memperhatikan:

- Garis singgung sebagai representasi turunan
- Hubungan antara kemiringan garis singgung dan nilai turunan
- Kasus-kasus khusus (horizontal tangent, vertical tangent)

#### 3. Konsep Diferensiabilitas (10 menit)

Pahami kapan suatu fungsi memiliki turunan:

- Syarat kontinuitas
- Keberadaan limit kiri dan kanan
- Contoh fungsi yang tidak terdiferensiasi

### C. Sesi Praktik (45 menit)

#### 1. Implementasi Turunan Numerik

```python
# derivative_calculator.py
import numpy as np
import matplotlib.pyplot as plt

class DerivativeCalculator:
    def __init__(self):
        """
        Inisialisasi calculator dengan tools untuk visualisasi
        dan perhitungan turunan numerik
        """
        self.x_range = np.linspace(-10, 10, 1000)
  
    def numerical_derivative(self, f, x, h=0.0001):
        """
        Menghitung turunan numerik menggunakan definisi limit
    
        Args:
            f: fungsi yang akan dihitung turunannya
            x: titik dimana turunan dihitung
            h: delta x yang sangat kecil
        
        Returns:
            Nilai turunan di titik x
        """
        return (f(x + h) - f(x)) / h
  
    def plot_function_and_derivative(self, f, x_point):
        """
        Memvisualisasikan fungsi dan garis singgungnya
        di titik tertentu
    
        Args:
            f: fungsi yang akan divisualisasikan
            x_point: titik dimana garis singgung akan digambar
        """
        # Hitung nilai fungsi
        y_values = [f(x) for x in self.x_range]
    
        # Hitung turunan di titik yang dipilih
        derivative_at_point = self.numerical_derivative(f, x_point)
    
        # Persamaan garis singgung
        tangent_line = lambda x: f(x_point) + derivative_at_point * (x - x_point)
    
        # Plot
        plt.figure(figsize=(12, 8))
        plt.plot(self.x_range, y_values, 'b-', label='f(x)')
    
        # Plot garis singgung
        x_tangent = np.linspace(x_point - 2, x_point + 2, 100)
        y_tangent = [tangent_line(x) for x in x_tangent]
        plt.plot(x_tangent, y_tangent, 'r--', 
                label=f'Tangent line (slope = {derivative_at_point:.2f})')
    
        plt.grid(True)
        plt.legend()
        plt.title('Function and Its Derivative Visualization')
        plt.show()
```

#### 2. Eksperimen dengan Berbagai Fungsi (25 menit)

Mari mengimplementasikan dan memahami turunan untuk fungsi-fungsi berikut:

- Fungsi linear: f(x) = 2x + 1
- Fungsi kuadrat: f(x) = x²
- Fungsi trigonometri: f(x) = sin(x)

#### 3. Visualisasi Interaktif (20 menit)

Buat visualisasi yang menunjukkan:

- Perubahan garis singgung di berbagai titik
- Hubungan antara kemiringan kurva dan nilai turunan
- Kasus-kasus khusus seperti titik stasioner

### D. Sesi Review (30 menit)

#### 1. Dokumentasi Pembelajaran

Catat pemahaman Anda tentang:

- Bagaimana turunan menggambarkan rate of change
- Interpretasi geometris turunan
- Hubungan antara limit dan turunan
- Kasus-kasus khusus yang menarik

#### 2. Aplikasi dalam Machine Learning

Pahami bagaimana turunan digunakan dalam:

- Gradient descent untuk optimasi
- Backpropagation dalam neural networks
- Error minimization

### E. Latihan untuk Dikerjakan

1. Implementasi Lanjutan:

```python
def analyze_derivative_behavior(f, interval):
    """
    Menganalisis perilaku turunan dalam suatu interval
  
    Args:
        f: fungsi yang dianalisis
        interval: tuple (a, b) batas interval
    
    Returns:
        Dictionary berisi informasi tentang:
        - Titik-titik stasioner
        - Interval naik/turun
        - Nilai maksimum/minimum lokal
    """
    pass

def find_critical_points(f, interval):
    """
    Menemukan titik-titik kritis dalam interval
    (titik dimana f'(x) = 0 atau f'(x) tidak ada)
    """
    pass
```

2. Soal Analisis:

- Tentukan dimana f'(x) = 0 untuk f(x) = x³ - 3x² + 2
- Analisis perilaku turunan f(x) = |x| di x = 0
- Visualisasikan turunan f(x) = sin(x) dan jelaskan mengapa f'(x) = cos(x)

### F. Checklist Akhir Hari

- [X] Memahami definisi formal turunan
- [X] Dapat menghitung turunan numerik
- [X] Memahami interpretasi geometris turunan
- [X] Dapat membuat visualisasi fungsi dan turunannya
- [X] Mengimplementasikan minimal satu fungsi analisis
- [X] Menyelesaikan minimal satu soal analisis

### G. Persiapan untuk Hari Berikutnya

1. Review materi tentang:

- Aturan-aturan turunan dasar
- Chain rule
- Product rule

2. Siapkan pertanyaan tentang:

- Konsep yang masih membingungkan
- Implementasi yang challenging
- Aplikasi dalam dunia nyata

### H. Catatan Pengingat

Ingatlah bahwa turunan adalah konsep fundamental yang akan kita gunakan terus menerus dalam pembelajaran berikutnya. Pastikan Anda benar-benar memahami:

- Definisi dasar turunan
- Interpretasi geometrisnya
- Cara menghitungnya secara numerik
- Aplikasinya dalam masalah nyata
