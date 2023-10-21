import streamlit as st

import pandas as pd
import numpy as np

# Create a random dataframe for demonstration purposes
df = pd.DataFrame({
  'x': range(1, 101),
  'y': np.random.randn(100).cumsum()
})

st.title('Simple Line Chart')

st.line_chart(df.y)
