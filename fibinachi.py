import matplotlib.pyplot as plt
import numpy as np

# 1. Optimal range from -8 to 8
t = np.linspace(-8, 8, 1600)
z = t + 0.3j  # complex index input with small imaginary offset

# 2. Binet's Formula
sqrt_5 = np.sqrt(5)
phi = (1 + sqrt_5) / 2
psi = (1 - sqrt_5) / 2

y = (np.power(phi, z) - np.power(psi, z)) / sqrt_5  # y = F(z)

# 3. Extract coordinates
x_axis = t  # x
y_real = y.real  # real(y)
y_imag = y.imag  # imag(y)

# 4. Create the 3D Plot
fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(projection="3d")

# Plot the continuous spiral
ax.plot(
    x_axis,
    y_real,
    y_imag,
    color="darkorange",
    lw=2,
    label=r"Complex Fibonacci Spiral",
)

# Highlight integer steps from -8 to 8
int_t = np.arange(-8, 9)
int_z = int_t + 0.3j
int_y = (np.power(phi, int_z) - np.power(psi, int_z)) / sqrt_5
ax.scatter(
    int_t,
    int_y.real,
    int_y.imag,
    color="black",
    s=25,
    zorder=5,
    label="Integer Points",
)

# Axis labels
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel(r"real(y)", fontsize=12)
ax.set_zlabel(r"imag(y)", fontsize=12)
ax.set_title(
    r"Full Fibonacci Spiral", fontsize=13, pad=15
)

ax.legend()
plt.tight_layout()
plt.show()