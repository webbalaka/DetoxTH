import pandas as pd
import numpy as np
import IPython.display as ipd
import numpy as np
from playsound import playsound

df = pd.read_csv('r1.csv')

corrected = []

for index, row in df.iterrows():
    x = "data_test/r/r1/" + row['path']
    print(row['before_sentence'])
    #ipd.display(ipd.Audio(data = x , autoplay=True, rate=16000))
    while(True) :
        playsound(x)
        k = input()
        if(k != '') : break
    correct = input("Input : ")
    corrected.append(correct)
    print('pass')