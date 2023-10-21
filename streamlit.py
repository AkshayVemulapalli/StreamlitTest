import streamlit as st

import pandas as pd
import numpy as np

# Create a random dataframe for demonstration purposes
df = pd.DataFrame({
  'x': range(1, 101),
  'y': np.random.randint(1, 101, size=100)
})

st.title('Simple Line Chart')

st.line_chart(df.y)
