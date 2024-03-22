reset 
set terminal postscript eps enhanced color size 14.0cm,8.0cm font 'Helvetica,32pt'
set output "A_med.eps"
set palette model RGB defined (0 'purple', 1 'blue', 2 'green', 3 'yellow', 4 'orange', 5 'red')
set key font 'Helvetica, 24pt'
set xlabel 'T' 
set ylabel '<A>' offset 1.5,0 

plot 'A_med_averagesCt.dat' w l title "Control",  'A_med_averagesSc.dat' w l title "Schizophrenia"
