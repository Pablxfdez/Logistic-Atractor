# Logistic Attractor Analysis Project

## Introduction
This project is focused on the study of the convergence of a nonlinear dynamic system defined by the logistic function sequence, i.e., the sequence xn+1 = f(xn), with f(x) = rx(1-x). This example provides an insightful look into the inherent complexity of such systems.

## Project Description
The practice involves exploring the logistic function sequence to understand the behavior of nonlinear dynamic systems. Key aspects of the study include:

- **Calculating Attractors**: Using the algorithm discussed in class for calculating attractor sets. The orbit is calculated with the number of elements in this orbit delimited by the amplitude of the new set of elements.
- **Error Estimation**: Estimating the values of the elements in the limit set along with their errors. The stability of the selected set is studied to decide if it is an attractor.
- **Visualization**: Implementing the algorithm in Python using scientific calculation libraries like Numpy and visualization libraries like Matplotlib.plot to obtain and visualize the results.

## Materials and Methods
The problem was approached using mathematical and geometrical principles, along with several Python libraries:

- **Numpy**: Used for matrix and vector management.
- **Matplotlib.plot**: Employed for creating graphs and visualizing data.
- **Random Library**: Utilized to obtain the initial x0 from a uniform distribution over the interval (0,1).

## Repository Contents

1. **FernandezdelAmoP_AtractorLogistico.pdf**
   - **Description**: This document provides a comprehensive overview of the project, including theoretical background, methodology, and explanation of the computational techniques used in the analysis.

2. **FernandezdelAmoP_AtractorLogistico.py**
   - **Description**: The Python script is the core of the project, containing the implementation of the logistic function sequence analysis. It includes the calculation of attractor sets and the estimation of their errors.

## Conclusion
Through this practice, the existence and stability of attractor sets for different initial values and the parameter r were studied. Values of r were found for an initial random value with a final attractor set of 8 elements, providing these results with the highest possible precision along with their respective error intervals. This project successfully addresses the questions posed, offering a deep understanding of the behavior of nonlinear dynamic systems and the complexity inherent in such systems. The associated Python file provides additional insights and results for the study.
