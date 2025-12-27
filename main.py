import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

st.set_page_config(page_title="Simulated Lévy Process (Brownian + Poisson jumps)", layout="wide")  # Unique browser tab title
# Title
st.title("Lévy Process Simulator")

# Sidebar for user input
st.sidebar.header("Parameters")
T = st.sidebar.number_input("Total Time (T)", min_value=0.1, value=1.0, step=0.1)
N = st.sidebar.number_input("Number of Steps (N)", min_value=100, value=1000, step=100)
lam = st.sidebar.number_input("Poisson Intensity (λ)", min_value=0.1, value=10.0, step=0.1)
mu_j = st.sidebar.number_input("Jump Size Mean (μ_j)", value=0.0, step=0.1)
sigma_j = st.sidebar.number_input("Jump Size Std (σ_j)", min_value=0.01, value=0.1, step=0.01)

# Calculate dt
dt = T / N

# Simulate Brownian component
B = np.cumsum(np.random.normal(0, np.sqrt(dt), N))

# Simulate Poisson jumps
J = np.random.poisson(lam * dt, N) * np.random.normal(mu_j, sigma_j, N)
X = B + np.cumsum(J)

# Plot
fig, ax = plt.subplots()
ax.plot(np.linspace(0, T, N), X)
ax.set_title("Simulated Lévy Process (Brownian + Poisson jumps)")
ax.set_xlabel("Time")
ax.set_ylabel("Value")

# Display plot in Streamlit
st.pyplot(fig)
