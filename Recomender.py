import pandas as pd
import numpy as np

def transfo(value):
    return np.array([int(elem) for elem in value[1:-1].split(',')])

class Recomender:
    
    def __init__(self, filename):
        self.filename = filename;
        self.data = pd.read_csv(filename)[['id','0',' time']]
        self.data['0'] = self.data['0'].transform(transfo)
      
    
    def recommend(self, uservector):
        recoms = self.data[self.data['id'].isin(uservector) == True]['0'].values[0]
        return [{'id':self.data.iloc[rec]['id'], 'time':self.data.iloc[rec][' time']} for rec in recoms]