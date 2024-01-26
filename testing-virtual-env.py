#IMport standard libraries
import numpy as np
import matplotlib.pyplot as plt
import argparse

#Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-amplitude', default=1.0,help="Amplitude of function sin()", type=float)
parser.add_argument('-initial_angle', default=0.0,help="Initial angle where the function sin() will be evaluated", type=float)
parser.add_argument('-final_angle', default=6.28,help="Final angle where the function sin() will be evaluated", type=float)
parser.add_argument('-n_samples', default=1000,help="Number of samples between initial and final angle", type=int)

args = parser.parse_args()

#Initialise a numpy-type list
theta = np.linspace(start=args.initial_angle, stop=args.final_angle, num=args.n_samples)

#Evaluate the function sin() for each value of theta
y = args.amplitude*np.sin(theta)

#Plot the function
plt.figure(1)
plt.plot(theta,y, linewidth=2.0)
plt.title(r"Function $y=\sin(\theta)$")
plt.xlabel(r"$\theta$")
plt.ylabel("y")
plt.show()
