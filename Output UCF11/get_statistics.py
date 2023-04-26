import numpy
import statistics

file = open("Results/Results_jointST.txt", 'r')
lines = file.readlines()

top1_acc = []
top5_acc = []

for el in lines:
    i = el.index("top1_acc")
    i= i + len("top1_acc") + 4
    top1_acc.append(float(el[i:i+5]))

    j = el.index("top5_acc")
    j= j + len("top5_acc") + 4
    top5_acc.append(float(el[j:j+5]))

top1_mean = statistics.mean(top1_acc)
top5_mean = statistics.mean(top5_acc)
top1_std = statistics.stdev(top1_acc)
top5_std = statistics.stdev(top5_acc)
file.close()
file = open("statistics.txt", 'a')
file.write("Top1_mean: "+str(top1_mean)+"\n")
file.write("Top5_mean: "+str(top5_mean)+"\n")
file.write("Top1_std: "+str(top1_std)+"\n")
file.write("Top5_std: "+str(top5_std)+"\n")
