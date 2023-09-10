import pandas as pd
from transformers import pipeline, set_seed

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
    
    frame = pd.DataFrame(dat)
    Q=model_rf.predict(frame)
    disease = Q[0]

    str = f"Ayurvedic herbs for {disease}"
    generator = pipeline('text-generation', model='gpt2-medium')
    set_seed(42)
    result = generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)
    print(result[0]['generated_text'])

    
    
    return 0


predictDisease(["chills","nausea"])



