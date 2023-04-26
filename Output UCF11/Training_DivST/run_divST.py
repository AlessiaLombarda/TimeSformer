import torch
import numpy as np
import random as rnd
import os
import shutil
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split

f = open("dataset.csv", "r")
rows = f.read().split("\n")

train, test = train_test_split(rows, test_size=0.15, random_state=1)
X = train
kf = KFold(n_splits=5, random_state=1, shuffle=True)

#create test.csv and move it to dataset folder
f_test = open("test.csv", "a")
for el in test:
    f_test.write(el+"\n")
shutil.move("test.csv", "UCF-11_preprocessed/test.csv")
i=1
for train_index, val_index in kf.split(X):

    #create train.csv and move it to dataset folder
    f_train = open("train.csv", "a")
    for el in train_index:
        f_train.write(rows[el]+"\n")
    shutil.move("train.csv", "UCF-11_preprocessed/train.csv")

    #create val.csv and move it to dataset folder
    f_val = open("val.csv", "a")
    for el in val_index:
        f_val.write(rows[el]+"\n")
    shutil.move("val.csv", "UCF-11_preprocessed/val.csv")

    #execute training
    os.chdir('TimeSformer')
    os.system('python tools/run_net.py \
  --cfg configs/Kinetics/TimeSformer_divST_8x32_224.yaml \
  DATA.PATH_TO_DATA_DIR /home/studenti/lombarda/UCF-11_preprocessed \
  NUM_GPUS 1 \
  TRAIN.BATCH_SIZE 8 \
  SOLVER.MAX_EPOCH 7 \
  OUTPUT_DIR "output"')

    os.chdir('..')
    #os.remove("UCF-11_preprocessed/train.csv")
    #os.remove("UCF-11_preprocessed/val.csv")

    name = "TimeSformer/o"+str(i)
    os.rename("TimeSformer/output", name)
    shutil.move(name, "output")

    name = "UCF-11_preprocessed/train"+str(i)+".csv"
    os.rename("UCF-11_preprocessed/train.csv", name)
    shutil.move(name, "folds")

    name = "UCF-11_preprocessed/val"+str(i)+".csv"
    os.rename("UCF-11_preprocessed/val.csv", name)
    shutil.move(name, "folds")

    i+=1

shutil.move("UCF-11_preprocessed/test.csv", "folds")
