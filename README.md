# Network Dynamics Analysis

This project conducts a comprehensive analysis of network dynamics, specifically focusing on the behavior of clusters within a given network over time. Utilizing the SER model, it simulates the transitions between different states of nodes within a network and analyzes the formation and evolution of clusters. The project is designed to work with adjacency matrices that represent the connectivity of the network.

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- iGraph
- SER (a custom library for simulating the SER model - https://github.com/fabridamicelli/ser) 

Ensure you have the above dependencies installed in your environment to run the code successfully.

## Overview

The code performs the following operations:

1. **Load and Preprocess Data:** Reads an adjacency matrix from a text file, representing the network's connectivity. It preprocesses this matrix to ensure it is suitable for simulation.

2. **Simulation Setup:** Sets up the parameters for the SER model, including the number of time steps, the transient phase to be ignored, and probabilities for node state transitions.

3. **Execution of Multiple Runs:** For each threshold value within a specified range, the code executes multiple simulation runs. Each run simulates the network dynamics, tracking the active nodes and analyzing the cluster formations over time.

4. **Analysis and Output:** Calculates the size of the largest and second largest clusters, the average activity level, and the standard deviation of activity across the network. These metrics are computed for each simulation run and threshold level, and the results are saved to files within a structured directory system.

5. **Performance Measurement:** Tracks the execution time of the simulation runs to evaluate performance.

## Directory Structure

The code organizes output files into a specific directory structure under `Project/83`. For each sample, it creates subdirectories (`S1`, `S2`, `A_med`, `varA`) to store the simulation results. This structure facilitates easy navigation and analysis of the results across different simulation parameters.

## Running the Simulation

To execute the simulation, simply run the script. Ensure you have the required adjacency matrix file in the expected location and format. The script takes no argume
