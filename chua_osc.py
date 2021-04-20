from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

font = {'family': 'sans-serif',
        'weight': 'regular',
        'size': 10}
mpl.rc('font', **font)

#System parameters
c_1 = 25 * 10 ** (-6) #Value of capacity in F
c_2 = 100 * 10 ** (-6) #Value of capacity in F
l  = 15 * 10 ** (-6) #Value of inductance in H
r  = 2.5 * 10 ** 3 #Value of resistance in Ohms

alpha = 1 / (r * c_1)
beta = 1 / (r * l)

#Chua diode parameters
Ga = -1.143 #Middle slope coefficient
Gb = -0.714 #Side slopes coefficient
E  = 1 #Breaking point between both slopes 

init = [0.1, 0, 0] #initial conditions

#time array
t0 = 0
t1 = 300
tdom = (t0, t1) #time domain
dt   = 10 ** (-3) #number of values in time array
t_eval = np.arange(tdom[0], tdom[1], dt) #time array

def f(v1):
    return (Gb * v1 + (1/2) * (Ga - Gb) * (np.abs(v1 + E) - np.abs(v1 - E)))

def eq(Y, t, alpha, beta):

    dv1 = alpha * (Y[1] - Y[0] - f(Y[0]))
    dv2 = (Y[0] - Y[1] + Y[2])
    di3 = - beta * Y[1]

    return [dv1, dv2, di3]

sol = solve_ivp(lambda t, Y: eq(Y, t, alpha, beta), tdom, init, t_eval=t_eval)
print(min(np.append(sol.y[0,:], np.append(sol.y[1,:], sol.y[2,:]))))

noms = ['v1', 'v2', 'i3']

fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection='3d')

fig, ax = plt.subplots(4,1)
fig.tight_layout(pad=0.5)

for i in range(len(sol.y[:,0])):
    ax[0].plot(sol.t, sol.y[i,:], label=noms[i])
ax[1].plot(sol.y[0,:], sol.y[1,:], label=r'$v_2(v_1)$')
ax[2].plot(sol.y[1,:], sol.y[2,:], label=r'$i_3(v_2)$')
ax[3].plot(sol.y[2,:], sol.y[0,:], label=r'$v_1(i_3)$')

ax[0].set_title("System voltages and current vs time")
ax[1].set_title("2D Double Scroll")

for i in range(4):
    ax[i].legend()
    ax[i].grid()

ax_3d.plot(sol.y[0,:],sol.y[1,:],sol.y[2,:])

ax_3d.set_xlabel(noms[0])
ax_3d.set_ylabel(noms[1])
ax_3d.set_zlabel(noms[2])
ax_3d.set_title("3D Double Scroll")

plt.show()