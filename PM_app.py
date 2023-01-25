import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def predictive_maintenace(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'No Failure'
    else:
      return 'Failure'
  
    
  
def main():
    
    
    # giving a title
    st.title('Machine Predictive Maintenance Classification')
    
    
    # getting the input data from the user
    
    st.write('Enter the information for a Machine ')

    MT = st.selectbox('Type', ('L','M','H'))
    if MT == 'L':
        MT = 1
    elif MT == 'M':
        MT = 2
    else:
        MT = 3


    AT = st.number_input('Air Temperature [K]')
    PT = st.number_input('Process Temperature [K]')
    RS = st.number_input('Rotational_speed[rpm]')
    T = st.number_input('Torque[Nm]')
    TW = st.slider('Tool_wear_[min]', min_value=0, max_value=250)
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('PM Test Result'):
        diagnosis = predictive_maintenace([MT,AT,PT,RS,T,TW])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()