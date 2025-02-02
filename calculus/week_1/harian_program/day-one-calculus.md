# Rencana Pembelajaran: Hari Pertama

## Pengenalan Limit dan Setup Environment

### A. Persiapan (15 menit)

#### Setup Environment Python

1. Instalasi software yang diperlukan:

   - Python (versi 3.8 atau lebih baru)
   - PyCharm atau VSCode sebagai IDE
   - Git untuk version control
2. Instalasi library yang diperlukan:

   ```bash
   pip install numpy matplotlib scipy jupyter
   ```

### B. Sesi Teori (45 menit)

#### 1. Konsep Limit (20 menit)

- Tonton video 3Blue1Brown "Essence of Calculus" Episode 1
- Poin-poin kunci yang perlu diperhatikan:
  - Definisi informal limit
  - Pendekatan dari kiri dan kanan
  - Kasus-kasus ketika limit tidak ada

#### 2. Pembacaan Stewart Calculus Bab 1 (15 menit)

- Fokus pada bagian:
  - Definisi formal limit
  - Teorema-teorema dasar limit
  - Contoh-contoh perhitungan limit

#### 3. Aplikasi dalam Gerak (10 menit)

- Hubungan limit dengan:
  - Kecepatan sesaat
  - Percepatan
  - Rate of change

### C. Sesi Praktik (45 menit)

#### 1. Setup Project (10 menit)

```python
# limit_calculator.py
import numpy as np
import matplotlib.pyplot as plt

class LimitCalculator:
    def __init__(self):
        self.x_range = np.linspace(-10, 10, 1000)
  
    def plot_function(self, func, point, epsilon=0.1):
        """
        Plot fungsi dan visualisasi limit di sekitar titik tertentu
    
        Args:
            func: fungsi yang akan diplot
            point: titik x dimana limit akan dievaluasi
            epsilon: jarak dari titik untuk visualisasi pendekatan
        """
        y_values = [func(x) for x in self.x_range if x != point]
        x_values = [x for x in self.x_range if x != point]
    
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, 'b-', label='f(x)')
        plt.axvline(x=point, color='r', linestyle='--', label=f'x={point}')
        plt.grid(True)
        plt.legend()
        plt.title(f'Limit Analysis at x={point}')
        plt.show()
```

#### 2. Implementasi Fungsi Limit (20 menit)

- Buat fungsi untuk menghitung limit numerik
- Implementasi visualisasi pendekatan limit
- Eksperimen dengan berbagai fungsi

#### 3. Visualisasi dan Eksperimen (15 menit)

- Buat visualisasi untuk beberapa fungsi dasar
- Eksperimen dengan kasus-kasus khusus
- Dokumentasikan hasil pengamatan

### D. Sesi Review (30 menit)

#### 1. Dokumentasi (15 menit)

- Buat catatan tentang:
  - Konsep kunci yang dipelajari
  - Tantangan yang ditemui
  - Solusi yang ditemukan
  - Pertanyaan yang muncul

#### 2. Hubungan dengan Machine Learning (15 menit)

- Catat hubungan limit dengan:
  - Gradient descent
  - Optimization
  - Error analysis

### E. Tugas untuk Dikerjakan

1. Implementasi Dasar:

   ```python
   # Implementasikan fungsi berikut
   def calculate_numerical_limit(f, point, delta=0.0001):
       """
       Menghitung limit numerik fungsi f ketika x mendekati point
       """
       pass

   def analyze_limit_existence(f, point):
       """
       Menganalisis keberadaan limit dengan memeriksa
       pendekatan dari kiri dan kanan
       """
       pass
   ```
2. Latihan:

   - Hitung limit untuk fungsi-fungsi berikut:
     - f(x) = (x² - 1)/(x - 1) saat x → 1
     - f(x) = sin(x)/x saat x → 0
     - f(x) = (1 + 1/x)^x saat x → ∞

### F. Checklist Akhir Hari

- [X] Environment Python terinstal dan berfungsi
- [X] Memahami konsep dasar limit
- [X] Dapat mengimplementasikan perhitungan limit numerik
- [X] Dapat membuat visualisasi fungsi dan limit
- [ ] Dokumentasi pembelajaran tersimpan
- [X] Minimal satu latihan terselesaikan

### G. Referensi Tambahan

1. Video:

   - 3Blue1Brown: https://www.3blue1brown.com/topics/calculus
   - Khan Academy: Limits Introduction
2. Dokumentasi Python:

   - NumPy: https://numpy.org/doc/
   - Matplotlib: https://matplotlib.org/stable/tutorials/
3. Bacaan:

   - Stewart Calculus Chapter 1
   - Python for Data Analysis (untuk visualisasi)
