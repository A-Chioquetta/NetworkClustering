num_files = int(input(10))  #Number of files
sample = 'Sc'+str(1)
file_base_name = input('A_med_run') #Name of the files 
output_file_name = input("A_med_averagest.dat") #Name of the output file

values = [[] for _ in range(num_files)]
thresh = []

# Open files and extract data
for i in range(1, num_files + 1):
    filename = f'{file_base_name}{i}'+sample+'.dat'
    with open(filename, 'r') as file:
        for row in file:
            columns = row.rstrip('\n').split('      ')
            T, value = float(columns[0]), float(columns[1])
            if i == num_files:  # For the last file, store T values in thresh list
                thresh.append(T)
            values[i - 1].append(value)

# Calculate averages and write to file
averages = [sum(v) / len(v) for v in zip(*values)]
with open(output_file_name+sample, 'a') as file:
    for T, avg in zip(thresh, averages):
        file.write(f"{T}    {avg}\n")

