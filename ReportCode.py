import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import pandas_profiling as pp 
import csv 
filin=pd.read_csv("indianEco.csv")

profrep=pp.ProfileReport(filin)
profrep.to_file("ProfilingReport.html")