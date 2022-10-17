

pip install streamlit
import streamlit as st


df =pickle.load(open('df.pkl','rb'))

st.title("Battery life prediction") pip install sklearn

maxVoltage = st.selectbox('Max. Voltage Dischar. (V)',df['Max. Voltage Dischar. (V)'].unique())

minVoltage = st.selectbox('Min. Voltage Charg. (V)',df['Min. Voltage Charg. (V)'].unique())

time = st.selectbox('Time at 4.15V (s)',df['Time at 4.15V (s)'].unique())

timeconstantcurrent = st.selectbox('Time constant current (s)',df['Time constant current (s)'].unique())

DischargeTime = st.selectbox('Discharge Time (s)',df['Discharge Time (s)'].unique())

chargingtime = st.selectbox('Charging time (s)',df['Charging time (s)'].unique())

RUL = st.number_input('RUL')

if st.button('Predict Battery life'):
    pass
