#!/usr/bin/env python3

import matplotlib.pyplot as plt
import statistics
import csv
import numpy as np
import statsmodels.api as sm
import scipy.stats
import pandas as pd
import seaborn as sns
import sys
import matplotlib.mlab as mlab
from scipy.stats import norm
from statsmodels.nonparametric.kde import kernel_switch


def get_statistics(file):
    N_of_columns = 0
    df = pd.read_csv(file+'.csv', sep=',|;')
    Columns = list(df.columns)
    for i in Columns:
        if N_of_columns <= 10:
            X = df[i].describe()
            N_of_columns += 1
            print (X)


def plot_graph(file):
    sns.set(color_codes=True)
    df = pd.read_csv(file+'.csv', sep=',|;')
    df.replace(to_replace=',', value=None, inplace=False, regex=True)
    df1 = df.iloc[:,0:10]
    df1.plot(kind='line')
    plt.legend(loc='lower left', bbox_to_anchor= (1.0, 0.1), ncol=1, borderaxespad=0, frameon=False)
    plt.title('Expression of 10 genes in 39 patients')
    #plt.savefig('Graph.png')
    plt.show()


def apply_transformation(data):
    df = pd.read_csv(data+'.csv', sep=',|;')
    Class_1 = 0
    Class_2 = 0
    #fig = plt.figure(figsize=(12, 5))
    #bc = PowerTransformer(method='box-cox')
    #yc = PowerTransformer(method='yeo-johnson')
    #DF = df.iloc[:, 1]
    Labels = df.iloc[:, -1]
    for items in Labels.iteritems():
        item = items[1]
        item = item.replace('"','')
        if item == "ALL":
            Class_1 += 1
        elif item == "AML":
            Class_2 += 1
            
    DF_ALL = df.iloc[0:Class_1, 1]
    DF_AML = df.iloc[Class_1 :, 1]
    
    #Row = df.iloc[:, 0]
    #Columns = list(DF.columns)
    #DF.apply()
    #colors = ['#D81B60']
    #ax = fig.add_subplot(111)
    #DF.plot.density(DF, bw_method = 'scott', ind=None)
    #kde = sm.nonparametric.KDEUnivariate(DF)
    #fig = plt.figure(figsize=(12, 5))

    # Enumerate every option for the kernel
    #for i, kernel in enumerate(kernel_switch.keys()):
    #    ax = fig.add_subplot(2, 4, i + 1)
    #    ax.set_title('Kernel function "{}"'.format(kernel))
    #    kde.fit(kernel=kernel, fft=False, gridsize=2**10)
    #    ax.plot(kde.support, kde.density, lw=1, label='KDE from samples', zorder=5)
    #    ax.scatter(DF, np.zeros_like(DF), marker='x', color='red')
    #    plt.grid(True, zorder=-10)
    #    ax.set_xlim([-750, 750])

    #plt.tight_layout()
    
    print (Class_1)
    
    (mu, sigma) = norm.fit(DF_ALL)
    n, bins, patches = plt.hist(DF_ALL, bins=Class_1, normed=1, facecolor='green', alpha=0.75)
    y = norm.pdf(bins, mu, sigma)
    l = plt.plot(bins, y, 'g--', linewidth=2)
    plt.legend(loc='lower left', bbox_to_anchor= (1.0, 0.1), ncol=1, borderaxespad=0, frameon=False)
    plt.grid(True)
    
    (mu2, sigma2) = norm.fit(DF_AML)
    n, bins, patches = plt.hist(DF_ALL, bins=Class_2, normed=1, facecolor='red', alpha=0.75)
    y2 = norm.pdf(bins, mu2, sigma2)
    l2 = plt.plot(bins, y2, 'r--', linewidth=2)
    #bx = DF_AML.plot.kde()
    plt.legend(loc='lower left', bbox_to_anchor= (1.0, 0.1), ncol=1, borderaxespad=0, frameon=False)
    plt.title('Expression of 1 gene in sick(red) and healty(green) patients, with Gaussian KDE')
    #plt.savefig('Combined.png')
    plt.show()

    line = plt.gca().get_lines()[n]
    xd = line.get_xdata()
    yd = line.get_ydata()



if __name__=='__main__':
    #File = sys.argv[1]
    #plot_graph('/home/blasfemus/Documents/Thesis/leukemia_train_38x7129')
    #get_statistics('/home/blasfemus/Documents/Thesis/leukemia_train_38x7129')
    apply_transformation('/home/blasfemus/Documents/Thesis/leukemia_train_38x7129')





