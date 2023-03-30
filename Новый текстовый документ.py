import numpy as np
import matplotlib.pyplot as plt

# заданные параметры цепи
f = 50
w = 2*np.pi*f
U = 90
Rk = 25
Lk = 0.1
Xlk = w*Lk
Crez = 1/(w*Xlk)

# диапазон изменения ёмкости
Cmin = 1e-6
Cmax = 200e-6
deltaC = 2*Cmin

# массив значений емкости для вычислений
C_array = np.arange(Cmin, Cmax+deltaC, deltaC)

# вычисление характеристик цепи для каждого значения емкости
Xc_array = 1/(w*C_array)
X_array = Xlk - Xc_array
I_array = U/np.sqrt(Rk**2 + (Xlk - 1/(w*C_array))**2)
Ulk_array = Xlk*I_array
Ua_array = Rk*I_array
Uc_array = Xc_array*I_array
Uk_array = np.sqrt(Rk*I_array**2 + Ulk_array**2)
Z_array = np.sqrt(Rk**2 + (Xlk - 1/(w*C_array))**2)
S_array = U*I_array
P_array = Rk*I_array**2
Qlk_array = Xlk*I_array**2
Qc_array = Xc_array*I_array**2
Q_array = Qlk_array - Qc_array
phi_rad_array = np.arctan(X_array/Rk)
phi_deg_array = phi_rad_array/np.pi*180

# построение векторных диаграмм
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20,6))
for i in range(3):
    ax[i].plot([0, Ua_array[i*40]], [0, 0], label='Ua')
    ax[i].plot([Ua_array[i*40], Ua_array[i*40]], [0, Uc_array[i*40]], label='Uc')
    ax[i].plot([0, Ua_array[i*40]], [0, Ulk_array[i*40]], label='Ulk')
    ax[i].plot([0, Ua_array[i*40]], [0, Uk_array[i*40]], label='Uk')
    ax[i].plot([0, Ua_array[i*40]], [0, S_array[i*40]], label='S')
    ax[i].plot([0, Ua_array[i*40]], [0, Q_array[i*40]], label='Q')
    ax[i].plot([0, Ua_array[i*40]], [0, P_array[i*40]], label='P')
    ax[i].set_xlim([-1.1*Ua_array[i*40], 1.1*Ua_array[i*40]])
    ax[i].set_ylim([-1.1*Ua_array[i*40], 1.1*Ua_array[i*40]])
    ax[i].set_aspect('equal')
    ax[i].set_title('C = {} мкФ'.format(C_array[i*40]*1e6))
    ax[i].legend()
plt.show()
