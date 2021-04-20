# Chua Oscillator
## Theory
A Chua Oscillator is a chaotic electronic oscillator, featuring one inductor, two capacitors, one resistor and a non-linear element called a _Chua diode_ referenced as _NR_ in the picture below. 
![Circuit](./Images/circuit.png)
In this case, the diode's current-voltage characteristic is a three piecewise-linear function that can be built using operational amplifiers and resistors. In our case, it has been modeled by the following parameters:
![Diode characteristic](./Images/charac.png)
Let f the function representing the diode's characteristic, `v1` and `v2` the tension of the right and the left capacitor and `i3` the current passing through the inductor. Using Kirchhoff's laws of electronics, we can derivate the following system.
![Equations](./Images/equations.png)
