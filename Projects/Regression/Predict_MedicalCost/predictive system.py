import numpy as np
import pickle

model= pickle.load(open('C:/Users/512GB/OneDrive/Documents/Major_Files/DevCareer/Another_SupervisedML/Projects/Regression/Predict_MedicalCost', 'rb'))

data= (34,23.6,1,0,1,1,0,1,0,2,0)

arrayed_data= np.asarray(data)
shaped_data= arrayed_data.reshape(1,-1)

prediction= model.predict(data)
print(prediction)