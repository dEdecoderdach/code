import numpy as np
import matplotlib.pyplot as plt

# 1. Define the complex function
def complex_tetrate_2(x):
    return (x + 0j) ** (x + 0j)

# 2. Generate a dense range for the continuous negative decimal spiral
x_neg_decimals = np.linspace(-3.5, -0.001, 3000)
outputs_neg = complex_tetrate_2(x_neg_decimals)

# 3. Generate a dense range for the continuous positive real branch
x_pos = np.linspace(0.0, 2.0, 1000)
outputs_pos = complex_tetrate_2(x_pos)

# 4. Explicitly define the negative integer coordinates (Purely Real)
neg_integers = np.array([-1.0, -2.0, -3.0])
outputs_integers = complex_tetrate_2(neg_integers)

# 5. Set up the dark-mode 3D plotting environment
plt.style.use('dark_background')
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# --- THE RED PATH: Imaginary Outputs ---
ax.plot(x_neg_decimals, np.real(outputs_neg), np.imag(outputs_neg),
        color='#FF3366', linewidth=3, alpha=0.75, label='Imaginary Part')

# --- THE GREEN PATH: Real Outputs ---
# A. Continuous positive branch
ax.plot(x_pos, np.real(outputs_pos), np.imag(outputs_pos),
        color='#00FF66', linewidth=3, label='Real Part')

# B. Discrete negative integer points
ax.scatter(neg_integers, np.real(outputs_integers), np.imag(outputs_integers),
           color='#00FF66', s=100, zorder=5, edgecolors='white', linewidths=1.5,)


# 7. Axis baseline configurations and limits
ax.plot([-5, 5], [0, 0], [0, 0], color='#555555', linestyle='--', linewidth=1) # X-axis
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
ticks = np.arange(-5, 6, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_zticks(ticks)
# Labels and perspective alignment
ax.set_title("$f(x) = {^2}x$ for Real Inputs", fontsize=14, pad=15)
ax.set_xlabel('Real Input (x)')
ax.set_ylabel('Real Output (y)')
ax.set_zlabel('Imaginary Output Part (z)')

ax.view_init(elev=22, azim=-65)
ax.legend(loc='upper left', frameon=True, facecolor='#111111', edgecolor='#333333')

plt.show()
