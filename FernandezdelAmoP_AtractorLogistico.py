"""
This program performs computations related to the Logistic Map.
Author: PABLO FERNÁNDEZ DEL AMO
UNIT: GEOMETRÍA COMPUTACIONAL

EXTRA PRACTICE 1
"""

import matplotlib.pyplot as plt
import numpy as np
import random

# Tolerance for numerical comparison
tolerance = 0.0005

def logistic_function(x, r):
    """
    Logistic function parameterized by r
    Args:
    x: input value
    r: rate parameter
    Returns:
    result of logistic function
    """
    return r*x*(1-x)

def numerical_equals(x, y, epsilon=0.001):
    """
    Check if two numbers are approximately equal within a tolerance
    Args:
    x, y: numbers to compare
    epsilon: tolerance for comparison
    Returns:
    True if |x - y| < epsilon, else False
    """
    return abs(x - y) < epsilon

def compute_orbit(initial_point, r, f, initial_size):
    """
    Compute the orbit of a point under a given function.
    Args:
    initial_point: starting point
    r: parameter for the function
    f: function to apply
    initial_size: initial size of the orbit
    Returns:
    orbit: array of points in the orbit
    """
    amplitude = 0
    orbit = np.empty(initial_size)
    x = initial_point
    for i in range(initial_size):
        orbit[i] = x
        x = f(x, r)
        
    prev_amplitude = amplitude
    amplitude = np.max(orbit) - np.min(orbit)
    
    while not numerical_equals(amplitude, prev_amplitude, tolerance):
        for i in range(initial_size):
            orbit = np.append(orbit, x)
            x = f(x, r)
        prev_amplitude = amplitude
        amplitude = np.max(orbit[-initial_size:]) - np.min(orbit[-initial_size:])
    
    return orbit

def compute_period(orbit, epsilon=0.001):
    """
    Compute the period of an orbit
    Args:
    orbit: array of points in the orbit
    epsilon: tolerance for comparing points
    Returns:
    period: number of iterations between repeated points
    """
    N = len(orbit)
    for i in np.arange(2, N-1, 1):
        if numerical_equals(orbit[N-1], orbit[N-i]) :
            break
    return i - 1

def check_stability(initial_point, r, period, limit_set, epsilon, initial_size):
    """
    Check if a limit set is stable
    Args:
    initial_point: starting point
    r: rate parameter
    period: period of the limit set
    limit_set: array of points in the limit set
    epsilon: tolerance for comparison
    initial_size: initial size of the orbit
    Returns:
    True if the limit set is stable, else False
    """
    for modified_initial_point in np.arange(-10*epsilon + initial_point, 10 * epsilon + initial_point, epsilon):
        modified_orbit = compute_orbit(modified_initial_point, r, logistic_function, initial_size)
        modified_period = compute_period(modified_orbit, epsilon)

        if period != modified_period: # not sharing the same period means not having the same long term behaviour, implying inestability
            return False         
        
        modified_limit_set = np.sort(modified_orbit[modified_orbit.size-modified_period:])
        difference = np.max(np.absolute(limit_set - modified_limit_set))
        max_difference = np.max(difference)


        if (max_difference >= epsilon):  # if the difference in the limit set is bigger than our tolerance threshold, it is not stable
            return False
    return True

def check_bifurcations(initial_point, r, delta):
    plt.figure(6, 6)
    for r in np.arange(-10 * delta, 10 * delta, delta):
        V0, _, _ = find_attractor_set(r, initial_point, tolerance)
        limit_set = [V0[i][0] for i in range(len(V0))]
        plt.plot([r] * len(V0), limit_set, 'ro', markersize=1)

    plt.xlabel = 'r'
    plt.ylabel = 'V_0'
    plt.axvline(x=r, ls="--")
    plt.show()

def find_attractor_set(r, initial_point, epsilon):
    """
    Find an attraсtor set for a given r and initial point.
    Args:
    r: rate parameter
    initial_point: starting point
    epsilon: tolerance for comparison
    Returns:
    limit_set, orbit, is_stable: the limit set, the full orbit, and a boolean indicating stability
    """
    initial_size = 25
    orbit = compute_orbit(initial_point, r, logistic_function, initial_size)
    period = compute_period(orbit, epsilon)
     
    limit_set = [(orbit[orbit.size-period+i],abs(orbit[orbit.size-period+i] - orbit[orbit.size-2*period+i])) for i in range(period)]
       
    limit_set.sort()
    is_stable = check_stability(initial_point, r, period, [element[0] for element in limit_set], epsilon, initial_size)
    
    return limit_set, orbit, is_stable
    
def apartadoI():
    """
    Compute and plot three attractor sets for given r and initial point values.
    """
    print("Section 1:")
    r_values = [3.4, 3.35, 3.1]
    initial_points = [0.5, 0.79, 0.9]
 
    for i in range(len(r_values)):
        print(f"Atractor set {i}: \nr = {r_values[i]}, initial point = {initial_points[i]} \n")
        limit_set, orbit, is_stable = find_attractor_set(r_values[i], initial_points[i], tolerance)

        if is_stable:
            for (x, epsilon) in limit_set:
                print(f"{x} ± {epsilon}")
            
            plt.title(f"Attractor set for r = {r_values[i]}")
            plt.plot(orbit)
            plt.xlabel("Nth element of the succession")
            plt.ylabel("Value X")
            plt.savefig(f"atractor_set{i}.png")
            plt.show()
        else:
            print("No stable set for r: {r_values[i]} and x_0: {initial_points[i]} found")


def apartadoII():
    """
    Estimate r values for which the attractor set has 8 elements.
    """
    print("Section 2:")

    initial_point = random.uniform(0, 1)
    r_error = 0.001
    counter = 0

    r_values = np.arange(3.001, 4, r_error)
    all_r_values = []
    f_r_values = []
    r_8elems = []
    atractor_set8 = []


    for r in r_values:
        limit_set0, orbit, _ = find_attractor_set(r, initial_point, tolerance)
        limit_set = [limit_set0[i][0] for i in range(len(limit_set0))]
        
        all_r_values.extend([r]* len(limit_set))
        f_r_values.extend(limit_set)
            

        if len(limit_set) == 8:
                
            for element in limit_set:
                r_8elems.append(r)
                atractor_set8.append(element)
            
            if counter == 0:
                example_values = limit_set0
                example_r = r
                example_orbit = orbit
                counter = 1
                
    plt.title(f"Attractor set for r = {round(example_r,4)} with x0 = {round(initial_point, 3)}")
    plt.plot(example_orbit)
    plt.xlabel("Nth element of the succession")
    plt.ylabel("X value")
    plt.savefig("attractor_set_8_elements.png")
    plt.show()
        
    plt.title(f"r values for 8-period attractors with x0 = {round(initial_point, 3)}")
    plt.plot(all_r_values, f_r_values, 'g,', markersize=0.01,label = 'Values from atraction sets')
    plt.plot(r_8elems, atractor_set8, 'r+', markersize=1.5, label = 'Values from atraction sets with 8 elements')
    plt.xlabel("r")
    plt.ylabel("x values")
    plt.legend()
    plt.savefig("AtractionSetsII.png")
    plt.show()

    print(f"The atractor set with x0 = {round(initial_point, 3)}  has 8 elements if r is:")
    r_8elems = list(set(r_8elems))
    r_8elems.sort()
    for r in r_8elems:
        print(f"{r} ± {r_error}")
    

    print(f"Example of an attractor set with x0 = {round(initial_point, 3)} and r = {example_r}:")
    for (x, epsilon) in example_values:
        print(f"{x} ± {epsilon}")


if __name__ == '__main__':
    apartadoI()
    apartadoII()

