# multiply_charged_ions.py
import numpy as np
import matplotlib.pyplot as plt

# Constants
e = 1.602e-19  # Coulombs
M_xe = 131.3 * 1.66054e-27  # kg (mass of Xe atom)
V_accel = 1000  # Acceleration voltage in Volts

# Range of Xe2+ fractions
fractions = np.linspace(0, 1, 100)

# Lists to store results
total_current = []
total_mass_flow = []
thrust = []

for f_xe2 in fractions:
    f_xe1 = 1 - f_xe2

    # Velocities
    v1 = np.sqrt(2 * e * V_accel / M_xe)       # Xe+
    v2 = np.sqrt(2 * 2 * e * V_accel / M_xe)   # Xe2+

    # Assume total ion count = 1 (unit basis)
    n1 = f_xe1
    n2 = f_xe2

    # Beam current: I = q * n * v
    I = n1 * e * v1 + n2 * 2 * e * v2
    total_current.append(I)

    # Mass flow: m_dot = n * m * v
    m_dot = n1 * M_xe * v1 + n2 * M_xe * v2
    total_mass_flow.append(m_dot)

    # Thrust ~ m_dot * v_avg = n * m * v^2
    T = n1 * M_xe * v1**2 + n2 * M_xe * v2**2
    thrust.append(T)

# Normalize
I_norm = np.array(total_current) / max(total_current)
m_dot_norm = np.array(total_mass_flow) / max(total_mass_flow)
T_norm = np.array(thrust) / max(thrust)

# MatPlot stiff 
plt.figure(figsize=(10, 6))
plt.plot(fractions, I_norm, label='Normalized Beam Current')
plt.plot(fractions, m_dot_norm, label='Normalized Mass Flow Rate')
plt.plot(fractions, T_norm, label='Normalized Thrust')
plt.xlabel('Fraction of Xe²⁺ in Beam')
plt.ylabel('Normalized Value')
plt.title('Effect of Multiply Charged Ions on Beam Characteristics')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("ion_beam_characteristics.png")
