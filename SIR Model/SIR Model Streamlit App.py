import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Import your simulation function
from Assignment3_Functions_Solutions_1 import run_sim

# -----------------------------------
# Title
# -----------------------------------
st.title("Disease Spread Simulator (SIR / SIRD / SIRDV)")
st.write("Simulate infectious disease dynamics using compartmental models.")

# -----------------------------------
# Model selection
# -----------------------------------
model_choice = st.selectbox(
    "Select Model",
    ["SIR", "SIRD", "SIRDV"]
)

# -----------------------------------
# Simulation parameters
# -----------------------------------
days = st.slider("Number of Days", 10, 365, 100)

beta = st.number_input("Infection Rate (beta)", value=0.4)
gamma = st.number_input("Recovery Rate (gamma)", value=0.035)

# -----------------------------------
# Initial populations
# -----------------------------------
st.subheader("Initial Population")

S_0 = st.number_input("Susceptible (S₀)", min_value=0, value=997)
I_0 = st.number_input("Infected (I₀)", min_value=0, value=3)
R_0 = st.number_input("Recovered (R₀)", min_value=0, value=0)

# Defaults
mu = 0
vac_rate = 0

# -----------------------------------
# Model-specific inputs
# -----------------------------------
if model_choice in ["SIRD", "SIRDV"]:
    mu = st.number_input("Death Rate (mu)", value=0.01)

if model_choice == "SIRDV":
    vac_rate = st.number_input("Vaccination Rate", value=0.01)

# Total population
N = S_0 + I_0 + R_0

# -----------------------------------
# Run simulation
# -----------------------------------
if st.button("Run Simulation"):

    Sim_S, Sim_I, Sim_R, Sim_D, Sim_V = run_sim(
        S_0=S_0,
        I_0=I_0,
        R_0=R_0,
        beta=beta,
        gamma=gamma,
        mu=mu,
        vac_rate=vac_rate,
        days=days,
        model_choice=model_choice
    )

    # -----------------------------------
    # Plot
    # -----------------------------------
    t = np.arange(0, days)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(t, Sim_S, label="Susceptible")
    ax.plot(t, Sim_I, label="Infected")
    ax.plot(t, Sim_R, label="Recovered")

    # Add model-specific lines
    if model_choice in ["SIRD", "SIRDV"]:
        ax.plot(t, Sim_D, label="Deceased")

    if model_choice == "SIRDV":
        ax.plot(t, Sim_V, label="Vaccinated")

    ax.set_xlabel(
        f"Days\nS={S_0}, I={I_0}, R={R_0}, beta={beta}, gamma={gamma}, mu={mu}, vac_rate={vac_rate}"
    )
    ax.set_ylabel("Number of People")
    ax.set_title(f"{model_choice} Model Simulation (N={N}, {days} Days)")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)