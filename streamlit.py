import streamlit as st
import pandas as pd
import numpy as np
# Create a random dataframe for demonstration purposes
df = pd.DataFrame({
  'x': range(1, 101),
  'y': [int(np.round(np.sin(0.1 * x))) for x in range(100)]
})

st.title('Simple Line Chart')
st.line_chart([int(np.round(np.sin(0.1 * x))) for x in range(100)])
