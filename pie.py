from pandas.core.frame import DataFrame
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("c:/Users/ADI/Downloads/Sampling-distribution-master/Sampling-distribution-master/data.csv")
data= df["temp"].tolist()
fig = ff.create_distplot([data], ["temp"], show_hist=False)
#fig.show()

mean = statistics.mean(data)
print("mean is:", mean )
stdv = statistics.stdev(data)
print (stdv)

dataset = []
for i in range(0, 1000):
     random_index= random.randint(0,len(data))
     value = data[random_index]
     dataset.append(value)
Mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)
print(Mean)
print(std_deviation)

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()