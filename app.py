import streamlit as st
import os
import pandas as pd
import joblib as jb

heading_style = '''
<div style="color:red;" align='center'>
<h1>Healthcare</h1>
</div>
'''
def return_df(id,
gender,
    	age,
		hypertension,
		heart_disease,
		ever_married,
		work_type,
		Residence_type,
		avg_glucose_level,
		bmi,
		smoking_status
		):
	'id':[id],
    'gender':[gender],
	'age':[age],
		'hypertension':[hypertension],
		'heart_disease':[heart_disease],
		'ever_married':[ever_married],
		'work_type':[work_type],
		'Residence_type':[Residence_type],
		'avg_glucose_level':[avg_glucose_level],
		'bmi':[bmi],
		'smoking_status':[smoking_status]
    
    }   
    final_df=pd.DataFrame(kbn)
    return final_df


def base_model():
    base=jb.load(os.path.join('finalised_rf_model.pkl'))
    return bmodel

st.markdown(heading_style, unsafe_allow_html=True)
Gender=st.selectbox('Select your gender',['Male','Female'])
hypertension=st.selectbox('hypertension',0,10)
heart_disease=st.slider('heart_disease',0,10)
ever_married=st.selectbox('ever_maried',['yes','no'])
work_type=st.selectbox('work_type',['privite','government','govt_job'])
Residence_type=st.number_input('Residence_type',['Urban','Rural'])
avg_glucose_level=st.number_input('avg_glucose_level', min_value=0)
bmi=st.number_input('bmi',min_value=0)
smoking_status=st.number_input('smoking_status',['fomaly_smoked','never_smoked','Unknown','smokes'])

df=return_df(
id,
gender,
    	age,
		hypertension	'
		heart_disease,
		ever_married	,
		work_type,
		Residence_type,
		avg_glucose_level,
		bmi,
		smoking_status
        )
if st.button('Submit'):
	model=base_model()
	preds=model.predict(df)
	predictions=preds[0]
	if predictions==1:
	st.write('stroke')
	else predictions==0:
		st.write('not stroke')
		st.ballons()
