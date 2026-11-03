import matplotlib.pyplot as plt
import numpy as np
def imaginary_log(x):
    return np.log(x + 0j)

# Example usage:
z_values = np.linspace(0.1, 10, 100)
x_values = z_values
y_values = imaginary_log(x_values)

plt.plot(x_values, y_values.real, label='Real part')
plt.plot(x_values, y_values.imag, label='Imaginary part')
plt.xlabel('x')
plt.ylabel('log(x + 0j)')
plt.legend()
plt.show()