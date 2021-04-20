# Chua Oscillator
A Chua Oscillator is a chaotic electronic oscillator, featuring one inductor, two capacitors, one resistor and a non-linear element called a _Chua diode_ referenced as $N_R$ in the picture below. 
![Circuit](./Images/circuit.png)
In this case, the diode's current-voltage characteristic is a three piecewise-linear function that can be built using operational amplifiers and resistors. In our case, it has been modeled by the following parameters:
![Diode characteristic](https://en.wikipedia.org/wiki/Chua%27s_diode#/media/File:Chua_diode_characteristic_curve.svg)
Let f the function representing the diode's characteristic, $v_1$ and $v_2$ the tension of the right and the left capacitor and $i_3$ the current passing through the inductor. Using Kirchhoff's laws of electronics, we can derivate the following system.
![Equations](./Images/circuit.png)
