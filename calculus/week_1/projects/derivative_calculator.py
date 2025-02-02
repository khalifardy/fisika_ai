# derivative_calculator.py
import numpy as np
import matplotlib.pyplot as plt

class DerivativeCalculator:
    def __init__(self,func,h=0.0001):
        """
        Inisialisasi calculator dengan tools untuk visualisasi
        dan perhitungan turunan numerik
        """
        self.x_range = np.linspace(-10, 10, 1000)
        self.h = h
        self.func = func
    
    def numerical_derivative(self,x):
        """
        Menghitung turunan numerik menggunakan definisi limit
        
        Args:
            f: fungsi yang akan dihitung turunannya
            x: titik dimana turunan dihitung
            h: delta x yang sangat kecil
            
        Returns:
            Nilai turunan di titik x
        """
        return (self.func(x + self.h) - self.func(x)) / self.h
    
    def plot_function_and_derivative(self,x_point):
        """
        Memvisualisasikan fungsi dan garis singgungnya
        di titik tertentu
        
        Args:
            f: fungsi yang akan divisualisasikan
            x_point: titik dimana garis singgung akan digambar
        """
        # Hitung nilai fungsi
        y_values = [self.func(x) for x in self.x_range]
        
        # Hitung turunan di titik yang dipilih
        derivative_at_point = self.numerical_derivative(x_point)
        
        # Persamaan garis singgung
        tangent_line = lambda x: self.func(x_point) + derivative_at_point * (x - x_point)
        
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
    
    def analyze_derivative_behavior(self,interval):
        """
        Menganalisis perilaku turunan dalam suatu interval
  
        Args:
            interval: tuple (a, b) batas interval
      
        Returns:
            Dictionary berisi informasi tentang:
            - Titik-titik stasioner
            - Interval naik/turun
            - Nilai maksimum/minimum lokal
        """
        titik_stasioner = []
        titik_naik = []
        titik_turun = []
        maksimum_lokal = []
        minimum_lokal = []
        
        for i in range(interval[0], interval[1]):
            if self.numerical_derivative(i) <= self.h and self.numerical_derivative(i) >= -self.h:
                x_point = i
                titik_stasioner.append((x_point))
            elif self.numerical_derivative(i) > self.h:
                titik_naik.append((i))
            elif self.numerical_derivative(i) < -self.h:
                titik_turun.append((i))

        maksimum_lokal = interval[0] if self.func(interval[0]) > self.func(interval[1]) else interval[1]
        minimum_lokal = interval[0] if self.func(interval[0]) < self.func(interval[1]) else interval[1]
        value_maksimum = self.func(maksimum_lokal)
        value_minimum = self.func(minimum_lokal)
        
        for titik_stas in titik_stasioner:
            if self.func(titik_stas) > value_maksimum:
                maksimum_lokal = titik_stas
                value_maksimum = self.func(titik_stas)
            
            if self.func(titik_stas) < value_minimum:
                minimum_lokal = titik_stas
                value_minimum = self.func(titik_stas)
        
        
        
        
        dictio = {
            'titik_stasioner': titik_stasioner,
            'titik_naik': titik_naik,
            'titik_turun': titik_turun,
            'maksimum_lokal': maksimum_lokal,
            'minimum_lokal': minimum_lokal
        }
        
        return dictio
        

    def find_critical_points(self,interval):
        """
        Menemukan titik-titik kritis dalam interval
        (titik dimana f'(x) = 0 atau f'(x) tidak ada)
        """
        titik_stasioner = []
        titik_singular = []
        
        
        
        for i in range(interval[0], interval[1]):
            
            right = self.calculate_derivative_right(i)
            left = self.calculate_derivative_left(i)
            
            if right != left:
                titik_singular.append((i))
                
            elif self.numerical_derivative(i) <= self.h and self.numerical_derivative(i) >= -self.h:
                x_point = i
                titik_stasioner.append((x_point))
        
        return titik_stasioner, titik_singular
            
            
    
    def derivative_second(self,x_point):
        """
        Menghitung turunan kedua dalam interval
        """
        
        return (self.func(x_point + 2 * self.h) - 2 * self.func(x_point + self.h) + self.func(x_point))/(self.h**2)
    
    def calculate_derivative_right(self,x):
        """
        Menghitung turunan dari arah kanan
        """
        return (self.func(x + self.h) - self.func(x)) / self.h
    
    def calculate_derivative_left(self,x):
        """
        Menghitung turunan dari arah kiri
        """
        return (self.func(x) - self.func(x + self.h)) / (-self.h)
