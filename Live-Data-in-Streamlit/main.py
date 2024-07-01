import time
import psutil
import streamlit as st

# Function to get the memory usage.
def memory_usage():
  return psutil.virtual_memory().percent

# Assigning Streamlit metric to a variable.
memory_data = st.metric(label="Live Memory Data", value=memory_usage())

# Updating the data
while True:
    time.sleep(1)
    memory_data.metric(label="Live Memory Data", value=memory_usage())