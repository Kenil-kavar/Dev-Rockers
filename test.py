import pandas as pd

import pickle
# Replace 'file_path.pkl' with the path to your pickle file
with open('modelForPredictionDisease.pkl', 'rb') as file:
    model_rf = pickle.load(file)
def predictDisease(symp_in):
    if(len(symp_in) == 0):
        return "No symptoms!"
    
    header = pd.read_csv("symptoms.csv")
    symptoms = []
    for a in header:
        symptoms.append(a)

    dat = {}
    for i in range(132):
        dat[symptoms[i]] = [0]

    for sym in symp_in:
        dat[sym] = [1]

    print(symptoms)
    
    frame = pd.DataFrame(dat)
    Q=model_rf.predict(frame)
    print(Q[0])

    
    
    return 0


predictDisease(["chills","nausea"])



