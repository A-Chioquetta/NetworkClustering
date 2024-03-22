import os

Measure = input("What are you averaging? ")
num_files = int(input("Number of files: "))  #Number of files
num_files = num_files-1
Sample = input("Which sample? ")
sample = 'Sc'+ Sample
file_base_name = Measure+'_run' #Name of the files 
output_file_name = Measure+'_average' #Name of the output file

folderPath = Measure+'/'+sample

values = [[] for _ in range(num_files)]
thresh = []

# Open files and extract data
for i in range(0, num_files + 1):
    filename = os.path.join(folderPath, f'{file_base_name}{i}'+sample+'.dat')
    with open(filename, 'r') as file:
        for row in file:
            columns = row.rstrip('\n').split('      ')
            T, value = float(columns[0]), float(columns[1])
            if i == num_files:  # For the last file, store T values in thresh list
                thresh.append(T)
            values[i-1].append(value)

# Calculate averages and write to file
averages = [sum(v) / len(v) for v in zip(*values)]
with open(folderPath+'/'+output_file_name+sample+'.dat', 'a') as file:
    for T, avg in zip(thresh, averages):
        file.write(f"{T}    {avg}\n")

