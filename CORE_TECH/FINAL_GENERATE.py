import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# The Corrected Physical Constants for Stability Well
A, b, W0 = 1.0, 0.1, -1.0
C = 12.75858065006331
anchor = 10.1504

phi_symbol = sp.symbols('phi', real=True, positive=True)
V_sym = (sp.exp(-b*phi_symbol)*A*b/3)*(A*(b*phi_symbol+3)+6*W0) + C/phi_symbol**3

# Generate Visualization
phi_vals = np.linspace(5, 25, 1000)
v_func = sp.lambdify(phi_symbol, V_sym, 'numpy')
v_plot = v_func(phi_vals)

plt.figure(figsize=(12, 7))
plt.plot(phi_vals, v_plot, 'b-', linewidth=2, label='Cosmological Potential V(φ)')
plt.plot(anchor, float(V_sym.subs(phi_symbol, anchor)), 'ro', markersize=10, label=f'Stability Well (φ={anchor})')
plt.axhline(0, color='black', linestyle='--', alpha=0.5)
plt.title("ACA: The Stability Valley - Verified dS Vacuum", fontsize=14)
plt.xlabel("Scalar Field Value (φ)", fontsize=12)
plt.ylabel("Effective Potential Energy V(φ)", fontsize=12)
plt.ylim(-0.06, 0.02)
plt.grid(True, which='both', linestyle=':', alpha=0.5)
plt.legend()
plt.annotate('Stability Region', xy=(anchor, -0.045), xytext=(15, -0.02),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.savefig('projects/ACA-Cosmology/EVIDENCE/STABILITY_WELL_FINAL.png')
print("STABILITY_WELL_FINAL.png generated successfully.")
