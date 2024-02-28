def calculate(x, a, K1, K2, K3):
    return (x + 3*a - K1*x) / (K2*x + K3*x)
x_values = [5, 10, 15, 20, 25]  
a_value = 2  
K1_value = 1  
K2_value = 2  
K3_value = 3  

for x in x_values:
    result = calculate(x, a_value, K1_value, K2_value, K3_value)
    print(f"Значення для x={x}: {result}")
