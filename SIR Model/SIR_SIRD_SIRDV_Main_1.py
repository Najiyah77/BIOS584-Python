#-----------------------------------------------------------------------------------------------------------------------
# Name: Najiyah Williamson
# Date: 4/6/26
# BIOS 584 Assignment 4 Application 1 ("Main" Python script)

# Explain the purpose of this file here and the main steps
""" This module contains prompts to simulate and visualize the spread of an infectious disease """
#-----------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
#import your functions module
import SIR_SIRD_SIRDV_Functions_1 as functions
#=========================================================================================
# Get user input
#=========================================================================================
#Ask user "Do you want to simulate the SIR, SIRD or SIRDV model?" & assign their input to the variable MODEL_CHOICE
MODEL_CHOICE = input("Do you want to simulate the SIR, SIRD, SIRDV model?").upper() # makes sure user does uppercase
#Ask user relevant questions based on the model they chose and store the information in variables.

    # If the user requested a SIR model, ask them 4 questions:
        #"What is the infection rate you want to simulate?" Assign this user input to the variable BETA
        #"What is the recovery rate you want to simulate?" Assign this user input to the variable GAMMA
        #"How many days do you want to simulate the disease outbreak?" Assign this user input to the variable DAYS
        #"Give me a list of 3 numbers: the # of susceptible, # of infected and # of recovered individuals at day 0."
        # Assign the list the user inputted to the variable DAY0_INDV
if MODEL_CHOICE == "SIR":
    BETA = float(input("What is the infection rate you want to simulate?"))
    GAMMA = float(input("What is the recovery rate you want to simulate?"))
    DAYS = int(input("How many days do you want to simulate the disease outbreak?"))
    DAY0_INDV = eval(input("Give me a list of 3 numbers: the # of susceptible, # of infected, and # of recovered individuals at day 0: "))

    # If the user requested a SIRD model, ask the same questions as above but also:
        #"What is the death rate from the disease that you want to simulate?" Assign this user input to the variable MU
elif MODEL_CHOICE == "SIRD":
    BETA = float(input("What is the infection rate you want to simulate?"))
    GAMMA = float(input("What is the recovery rate you want to simulate?"))
    DAYS = int(input("How many days do you want to simulate the disease outbreak?"))
    DAY0_INDV = eval(input("Give me a list of 3 numbers: the # of susceptible, # of infected, and # of recovered individuals at day 0: "))
    MU = float(input("What is the death rate from the disease that you want to simulate?"))

    #If the user requested a SIRDV model, ask the same questions as above but also:
        #"What is the vaccination rate you want to simulate?" Assign this user input to the variable VAC_RATE
elif MODEL_CHOICE == "SIRDV":
    BETA = float(input("What is the infection rate you want to simulate?"))
    GAMMA = float(input("What is the recovery rate you want to simulate?"))
    DAYS = int(input("How many days do you want to simulate the disease outbreak?"))
    DAY0_INDV = eval(input("Give me a list of 3 numbers: the # of susceptible, # of infected, and # of recovered individuals at day 0: "))
    MU = float(input("What is the death rate from the disease that you want to simulate?"))
    VAC_RATE = float(input("What is the vaccination rate you want to simulate? "))

else:
    print("Invalid model choice.")

        # Note: Make sure you convert all the user input numbers to floats!
# You do NOT have to validate any input, assume user wrote in correct input.

#=========================================================================================
# Run default simulation and generate plot. Save the plot as png file called
# DefaultSIR_N1000_100Days_.4,.035.png. The .4, .035 are the default infection and recovery rates
#=========================================================================================
#Call the run_sim function to run the *default* SIR Model simulation, save the arrays returned by the function
# as Sim_S, Sim_I, Sim_R, Sim_D, Sim_V
Sim_S, Sim_I, Sim_R, Sim_D, Sim_V = functions.run_sim(
    S_0=DAY0_INDV[0],
    I_0=DAY0_INDV[1],
    R_0=DAY0_INDV[2],
    beta=BETA,
    gamma=GAMMA,
    mu=MU if MODEL_CHOICE in ["SIRD", "SIRDV"] else 0,
    vac_rate=VAC_RATE if MODEL_CHOICE == "SIRDV" else 0,
    days=DAYS,
    model_choice=MODEL_CHOICE
) #you don't have to specify parameters that have defualt arguments

# Create a plot for this default simulation (SIR Model) and make sure it matches the sample output
# I've given you the code below.
t = np.arange(0, 100) #array of time points (0 to 100 days)
plt.figure(figsize=(10,6))
plt.plot(t, Sim_S, label="Susceptible")
plt.plot(t, Sim_I, label="Infected")
plt.plot(t, Sim_R, label="Recovered")
plt.xlabel("Days \n Simulation Parameters: S=997, I=3, Beta = .4, Gamma = .035.")
plt.ylabel("Number of People")
plt.title("Default SIR Model (N=1000, 100 Days)")
plt.legend()
plt.grid(True)
plt.savefig("DefaultSIR_N1000_100Days_.4,.035.png")
plt.show() #Make sure to do plt.savefig before you type plt.show() otherwise, the plot will be empty

#=========================================================================================
# Run the simulation the user wants and generate plot. Save the plot as a png file with a name that includes the
# name of the model the user specified,
# the population N (this is S+I+R if the model is SIR or SIRD, or S+I+R+V if SIRDV model) and
# the rates (infection, recovery, and if relevant, vaccination and/or death rate)
# Run the simulation the user wants
Sim_S, Sim_I, Sim_R, Sim_D, Sim_V = functions.run_sim(
    S_0=DAY0_INDV[0],
    I_0=DAY0_INDV[1],
    R_0=DAY0_INDV[2],
    beta=BETA,
    gamma=GAMMA,
    mu=MU if MODEL_CHOICE in ["SIRD", "SIRDV"] else 0,
    vac_rate=VAC_RATE if MODEL_CHOICE == "SIRDV" else 0,
    days=DAYS,
    model_choice=MODEL_CHOICE
)

# Compute population N
if MODEL_CHOICE in ["SIR", "SIRD"]:
    N = DAY0_INDV[0] + DAY0_INDV[1] + DAY0_INDV[2]
else:  # SIRDV
    N = DAY0_INDV[0] + DAY0_INDV[1] + DAY0_INDV[2] + 0  # V0 = 0

# Build filename using f-strings
if MODEL_CHOICE == "SIR":
    filename = f"SIR_N{N}_{DAYS}Days_Rates{BETA},{GAMMA}.png"
elif MODEL_CHOICE == "SIRD":
    filename = f"SIRD_N{N}_{DAYS}Days_Rates{BETA},{GAMMA},{MU}.png"
else:  # SIRDV
    filename = f"SIRDV_N{N}_{DAYS}Days_Rates{BETA},{GAMMA},{MU},{VAC_RATE}.png"

#Example: SIRD_N1000_100Days_Rates.4,.035,.005.png
#(if the user requested a SIRD model of 100 days for 1000 people with infection,recovery & death rates of .4,.035,.005)
#Hint: use f-strings!
#=========================================================================================
#Call the run_sim function to run the user's requested simulation & save the arrays returned by the function
# as Sim_S, Sim_I, Sim_R, Sim_D, Sim_V
Sim_S, Sim_I, Sim_R, Sim_D, Sim_V = functions.run_sim(
    S_0=DAY0_INDV[0],
    I_0=DAY0_INDV[1],
    R_0=DAY0_INDV[2],
    beta=BETA,
    gamma=GAMMA,
    mu=MU if MODEL_CHOICE in ["SIRD", "SIRDV"] else 0,
    vac_rate=VAC_RATE if MODEL_CHOICE == "SIRDV" else 0,
    days=DAYS,
    model_choice=MODEL_CHOICE
)



