#import pickle
#import numpy as np

#loaded_model= pickle.load(open("C:/Users/512GB/OneDrive/Documents/Major_Files/DevCareer/Another_SupervisedML/Projects/Classification/PredictHearDisease/predictor_model.sav","rb"))

#input_data= (40,140,289,172,0,	0,	0,	1,	0,	0,	1,	0,	0,	1,	0,	1,	0,	0)

#input_data_array= np.asarray(input_data)


#input_data_array_shaped= input_data_array.reshape(1,-1)


#prediction= loaded_model.predict(input_data_array_shaped)
#print(prediction)

#if(prediction[0]==0):
    #print('Patient has no heart disease')
#else:
    #print('Patient has heart disease')
   

