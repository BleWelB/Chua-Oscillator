from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import matplotlib as mpl

font = {'family': 'sans-serif',
        'weight': 'regular',
        'size': 10}
mpl.rc('font', **font)

#System parameters
c_1 = 25 * 10 ** (-6) #Value of capacity in F
c_2 = 100 * 10 ** (-6) #Value of capacity in F
l  = 15 * 10 ** (-6) #Value of inductance in H
r  = np.arange(2 * 10 ** 3, 3 * 10 ** 3, 5) #Array of resistance in Ohms

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


fig, ax = plt.subplots(2,1)
fig.tight_layout()

v1, = ax[0].plot([], [], label='v1', linewidth=0.5)
v2, = ax[0].plot([], [], label='v2', linewidth=0.5)
i3, = ax[0].plot([], [], label='i3', linewidth=0.5)

v2v1, = ax[1].plot([], [], 'k', label=r'$v_2(v_1)$', linewidth=0.5)

num_r = ax[1].text(0.1, 0.9, "", transform=ax[1].transAxes, ha="center")

ax[0].set_title("System voltages and current vs time")
ax[1].set_title("2D Double Scroll")

ax[0].grid()
for i in range(2):
    ax[i].legend(loc='upper right')

def animate(i):

    num_r.set_text(r"$R =$ {} $\Omega$".format(r[i]))

    sol = solve_ivp(lambda t, Y:eq(Y, t, alpha[i], beta[i]), tdom, init, t_eval=t_eval)

    v1.set_data(sol.t, sol.y[0,:])
    v2.set_data(sol.t, sol.y[1,:])
    i3.set_data(sol.t, sol.y[2,:])

    v2v1.set_data(sol.y[0,:], sol.y[1,:])

    ymin = min(np.append(sol.y[0,:], np.append(sol.y[1,:], sol.y[2,:])))
    ymax = max(np.append(sol.y[0,:], np.append(sol.y[1,:], sol.y[2,:])))

    ax[0].set_xlim([t_eval[0], t_eval[-1]])
    ax[0].set_ylim([ymin, ymax])
    ax[1].set_xlim([min(sol.y[0,:]), max(sol.y[0,:])])
    ax[1].set_ylim([min(sol.y[1,:]), max(sol.y[1,:])])

    return v1, v2, i3, v2v1, num_r

anim = animation.FuncAnimation(fig, animate, frames=len(r), blit=True)
#anim.save('2D_scroll.gif', writer='imagemagick', fps=5)

plt.show()