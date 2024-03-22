import matplotlib.pyplot as plt
import numpy as np
from ser import SER
import igraph as ig
import os

import timeit
start =timeit.default_timer()

sample = 8
W = np.loadtxt('SC_density/83/Schz/Schz'+str(sample)+'.txt', usecols = range(83)) #Import adjacency matrix
n_nodes = len(W)
W[np.eye(n_nodes, dtype=bool)] = 0 #make main diag zero

W = W.transpose()


Wp = W.copy()

for i in np.arange(0,n_nodes): # Matrix that select which components are conected (if connecteted W[ij]=1, if not W[ij]=0)
    for j in np.arange(0,n_nodes):
        if Wp[i,j]>0.0:
            Wp[i,j] = 1


n_steps =1000 #Number of time steps
transient =100 #Initial steps to be ignored
r1 =2/n_nodes # Probability of a node transitioning from quiescent state to excited state
r2 =pow(r1,1/5) #Probability of a node recovering from a refractory state to a quiescent


for run in range(30): #Multiple runs to make an average
    print('run'+ str(run))
    for T in np.linspace(0.0, 0.15, 35): #Loop on the threshold

        model = SER(n_steps=n_steps, prop_e=0.6, prop_s=0.3, threshold= T,n_transient =transient,prob_recovery=r2,prob_spont_act =r1)
        activity = model.run(adj_mat=W)


        activity_only_active = activity.copy()
        activity_only_active[activity == -1] = 0 # Selecting only the nodes that are active (vector)
        n_active_nodes = activity_only_active.sum(axis=0)


        S1 = [] #Largest cluster
        S2 = [] #Second largest cluster
        
        for t in np.arange(0,n_steps-transient):

            S = np.tensordot(activity_only_active[:,t],activity_only_active[:,t],axes =0) #Make the activity matrix 

            Cp = np.empty((n_nodes,n_nodes))  #Cp will be the matrix with only active nodes that are connected

            for i in np.arange(0,len(Cp)):
                for j in np.arange(0,len(Cp)):
                    Cp[i,j] = Wp[i,j]*S[i,j]

            for i in range(len(Cp)-1,-1,-1):
                Count = 0.0
                for j in range(len(Cp)-1,-1,-1):
                    if Cp[i,j]>0:
                        Count=Count+1

                if Count == 0.0:
                    Cp = np.delete(Cp,i,axis = 0)
                    Cp = np.delete(Cp,i,axis = 1)

            if len(Cp)>0:
                C = ig.Graph.Adjacency(Cp) #Transform the matrix into a graph so igraph can count the components
                
                components = C.connected_components(mode='weak') 
                n_clus = C.components() #number of clusters
                N_clusters = len(components)
                
                sizes = []
                for i in range(0,N_clusters):
                    ss =len(components[i]) #size of each cluster
                    
                    sizes.append(-ss)
                orderedSizes = sorted(sizes) #ordering from bigger cluster to smaller cluster
                
                S1.append(-orderedSizes[0]) #Save size of the bigger cluster
                
                
                if N_clusters>1:
                    S2.append(-orderedSizes[1]) #save size of the secong bigger cluster

 

            else:
                print("no clusters at time ",t)



        # S1
        S1_med = 0
        for i in range(0,len(S1)):
            S1_med =S1_med+ S1[i] #Summing all of the largest clusters for all steps
            

        S1_med = S1_med/(n_steps-transient) #Averaging on steps
        S1_medT = S1_med/n_nodes #Averaging on total nodes


        # S2
        S2_med = 0
        for i in range(0,len(S2)):
            S2_med =S2_med+ S2[i] #Summing all of the second largest clusters for all steps 

        S2_med = S2_med/(n_steps-transient) #Averaging on steps
        S2_medT = S2_med/n_nodes #Averaging on total nodes



        # <A>
        At =0
        for i in range(0, n_steps-transient): 
            At += n_active_nodes[i] #Summing all the active nodes

        At = At/n_nodes #Averaging on total nodes
        A_med = At/(n_steps-transient) #Averaging on time steps


        # Standard deviation of A
        varA = 0
        for i in range(0, n_steps-transient):
            varA += pow((n_active_nodes[i]/n_nodes) - A_med,2)

        varA = varA/ (n_steps -transient)
        varA = np.sqrt(varA)

        print(T, "of 0.15")
        
    


        # Base directory
        baseDir = 'Project/83'


        # Folder paths with base directory
        S1Folder = os.path.join(baseDir, 'S1')
        S2Folder = os.path.join(baseDir, 'S2')
        AmedFolder = os.path.join(baseDir, 'A_med')
        varAFolder = os.path.join(baseDir, 'varA')

        # Create main folders if they don't exist
        os.makedirs(S1Folder, exist_ok=True)
        os.makedirs(S2Folder, exist_ok=True)
        os.makedirs(AmedFolder, exist_ok=True)
        os.makedirs(varAFolder, exist_ok=True)

        # Create subfolders for each sample
        sampleFolder1 = os.path.join(S1Folder, 'Sc' + str(sample))
        sampleFolder2 = os.path.join(S2Folder, 'Sc' + str(sample))
        sampleFolder3 = os.path.join(AmedFolder, 'Sc' + str(sample))
        sampleFolder4 = os.path.join(varAFolder, 'Sc' + str(sample))

        os.makedirs(sampleFolder1, exist_ok=True)
        os.makedirs(sampleFolder2, exist_ok=True)
        os.makedirs(sampleFolder3, exist_ok=True)
        os.makedirs(sampleFolder4, exist_ok=True)

        # Data writing to files within the correct subfolders
        with open(os.path.join(sampleFolder1, 'S1_run' + str(run) + 'Sc' + str(sample) + '.dat'), "a") as file1:
            file1.write(str(T) + "         " + str(S1_med) + "         " + str(S1_medT) + "\n")

        with open(os.path.join(sampleFolder2, 'S2_run' + str(run) + 'Sc' + str(sample) + '.dat'), "a") as file2:
            file2.write(str(T) + "         " + str(S2_med) + "         " + str(S2_medT) + "\n")

        with open(os.path.join(sampleFolder3, 'A_med_run' + str(run) + 'Sc' + str(sample) + '.dat'), "a") as file3:
            file3.write(str(T) + "         " + str(A_med) + "\n")

        with open(os.path.join(sampleFolder4, 'varA_run' + str(run) + 'Sc' + str(sample) + '.dat'), "a") as file4:
            file4.write(str(T) + "         " + str(varA) + "\n")


stop =timeit.default_timer()
print('Time', stop-start )  ##Cheking how long it takes to run the calculations
