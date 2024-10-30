import control as ct
import matplotlib.pyplot as plt

s = ct.TransferFunction.s

K = 1

# Transfer function
R = K/(s**2 + 10*s +K)

# Plot root-locus of R
plt.figure()
ct.root_locus(R)

# Close-loop transfer function
D = ct.feedback(R, 1)

# Plot Nyquist diagram
plt.figure()
ct.nyquist_plot(R)

# Ideal step response
t,yout = ct.step_response(D)
plt.figure()
plt.plot(t, yout)
plt.grid()
plt.xlabel("Time [s]")

# Show plots
plt.show()