import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Streamlit UI inputs
st.title('Transformer Voltage Regulation')
impedance = st.slider("Impedance %", 1, 15, 6)
XR_ratio = st.slider("X/R Ratio", 1, 20, 10)

# Transformer Calculation Logic (simplified)
pf_values = np.linspace(-1, 1, 200)
Z = impedance / 100
X = Z / np.sqrt(1 + (1/XR_ratio)**2)
R = X / XR_ratio

VR = [(R*abs(pf) + np.sign(-pf)*X*np.sin(np.arccos(abs(pf))))*100 for pf in pf_values]

fig = go.Figure()
fig.add_trace(go.Scatter(x=pf_values, y=VR, name='Voltage Regulation'))
fig.update_layout(xaxis_title="Power Factor", yaxis_title="Voltage Regulation (%)")
st.plotly_chart(fig)
