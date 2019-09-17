I used the Beocat cluster to compute the probabilities. I submitted
"Mean_discrepancy.py" as an array job, via "Mean_discrepancy.bash". Each
individual job computed the means, respectively, of X and Y, for a different
value of N (the number of times each distribution was sampled). I then
compiled the outputs of these array jobs via "Mean_discrepancy_compiler.py"
(submitted to Beocat with "Mean_discrepancy_compiler.bash") and plotted
P(<x> < <y>) and P(<x> > <y>) with "Mean_plotter.py". These results are
presented in "Mean_discrepancy_plot.pdf". I found that, if I computed
the mean 10^5 times for each value of N, the smallest N for which
P(<x> > <y>) < 0.01 was 1074.