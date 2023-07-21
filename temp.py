import numpy as np
import pickle

loaded_model = pickle.load(open('E:/pythonProject/model/trained_model.sav', 'rb'))
# loaded_model = pickle.load(open('trained_model.sav', 'rb'))

input_data = (26,12,4323,69,3,0,0,6640,2170162,546,0.437342424,2020,3412.0,119,60,317)

# changing the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==1):
  print('High Video Quality')
else:
  print('Low Video Quality')
