import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import re
sns.set_style('whitegrid')

def missing_heat_map(DataFrame):
        
    # plot the missing values
        fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (18, 6))
        sns.heatmap(DataFrame.isnull(), yticklabels=False, ax = ax, cbar=False,\
                    cmap='viridis')
        ax.set_title('dataset')
        plt.show()
        
    # Calculate the missing values to get a percentage 

        for i in DataFrame:
            print(i,': %',int((DataFrame[i].isnull().sum()/len(DataFrame[i]))*100),\
                  'With {} missing values'.format((DataFrame[i].isnull().sum())))

#This function will give a brief description of the distribution of data with and without outliers
def no_outlier(Data_column,data_set):

    X = data_set[Data_column] #set the dataframe
    no_outlier = [] 
    confidence = []
    
    q1 = float(X.describe()['25%']) #get the q1 from the describe function 
    q3 = float(X.describe()['75%']) #get the q3 from the describe function
    iqr = (q3 - q1)*1.5 #get the iqr
    std = float(X.describe()['std']) #get the standered deviation
    mean = float(X.mean()) #get mean
    lower_limit = mean-(1.645*(std/np.sqrt(len(X)))) # calculate the lower limit for 90% confidence
    higher_limit = mean+(1.645*(std/np.sqrt(len(X)))) # calculate the higher limit for 90% confidence
    
    for total in X: #iterate over the data
        if lower_limit < total < higher_limit:
            confidence.append(total) #if the value is in the 90% confidence append to confidence 
        
        if (q1 - iqr) < (total) < (q3 + iqr):
            no_outlier.append(total) #if the value is between the outliers append it to list
        else:
            pass
    #print result
    print('Tukeys method number of outliers is {}'.format((len(X)-len(sorted(no_outlier)))))
    print('90% confidence interval has {} values between {} and {}'.format(len(sorted(confidence)),\
        round(lower_limit),round(higher_limit)))
    #plot 
    fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(12, 12))
    sns.distplot(X, ax=ax[0,0])
    sns.distplot(no_outlier,color='red', ax=ax[0,1])
    sns.boxplot(X,notch=True,orient='v',ax=ax[1,0])
    sns.boxplot(no_outlier,notch=True,orient='v',color='red',ax=ax[1,1])
    
    fig.suptitle('{}'.format(Data_column), fontsize=24)
    ax[0,0].set_title('Distribution of {}'.format(Data_column), fontsize=12)
    ax[0,1].set_title('Distribution of {} after removing outliers'.format(Data_column), fontsize=10)
    ax[1,0].set_title('Boxplot of {}'.format(Data_column), fontsize=10)
    ax[1,1].set_title('Boxplot of {} after removing outliers'.format(Data_column), fontsize=10)


def get_wordcount(column,df):

    return df[str(column)].apply(lambda x : len(x.split(' ')) if type(x) == str else 0)


def get_number(str):

    return float(re.sub("[^0-9]", "", str))

