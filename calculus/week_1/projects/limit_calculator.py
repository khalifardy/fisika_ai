import numpy as np
import matplotlib.pyplot as plt

class LimitCalculator:
    def __init__(self):
        self.x_range = np.linspace(-10, 10, 1000)
    
    def plot_function(self, funx, point, epsilon=0.1):
        """
        Plot fungsi dan visualisasi limit di sekitar titik tertentu

        Args:
            funx (_type_): fungsi yang akan di plot
            point (_type_): titik x dimana limit akan di evaluasi
            epsilon (float, optional): jarak dari titik untuk visualisasi pendekatan 
        """
        
        y_values = [funx(x) for x in self.x_range if x != point]
        x_values = [x for x in self.x_range if x != point]
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, 'b-',label='f(x)')
        plt.axvline(x=point, color='r',linestyle='--',label=f'x={point}')
        plt.grid(True)
        plt.legend()
        plt.title(f'Limit analisis di x={point}')
        plt.show()
        
    def calculate_numerical_limit(self,f, point, delta=0.0001):
       """
       Menghitung limit numerik fungsi f ketika x mendekati point
       """
       x_values = np.linspace(point-delta, point+delta, 1000)
       y_values = [f(x) for x in x_values]
       return np.mean(y_values)
       
    
   
    def analyze_limit_existence(self,f, point,delta=0.0001):
        """
        Menganalisis keberadaan limit dengan memeriksa
        pendekatan dari kiri dan kanan
        """
        left_limit = f(point-delta)
        right_limit = f(point+delta)
        print(left_limit, right_limit)
        if abs(left_limit - right_limit) <= 0.1:
            return True
        else:
            return False
    
    def calculate_right_limit(self,f,point,delta=0.0001):
        """
        Menghitung limit dari fungsi f ketika x mendekati point dari arah kanan
        """
        x_values = np.linspace(point, point+delta, 1000)
        y_values = [f(x) for x in x_values if x != point]
        return np.mean(y_values)
    
    def calculate_left_limit(self,f,point,delta=0.0001):
        """
        Menghitung limit dari fungsi f ketika x mendekati point dari arah kiri
        """
        x_values = np.linspace(point-delta, point, 1000)
        y_values = [f(x) for x in x_values if x != point]
        return np.mean(y_values)