#-------------------------------------------------------------------
# This script codes a simulation of the SIR model
#-------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt #can name it anything you want

#------------------Functions used for simulation---------------------
# SIR model differential equations
def sir_model(S, I, R, beta, gamma):
    """'
    This function takes in a specified infection rate (beta), recovery rate (gamma) and the
    current number of susceptible (S), infected (I) and recovered individuals (R) for a given day. N is equivalent to S+I+R.
    It returns the rate of change in the number of susceptible individuals (dS/dt), change in the number
    of infected individuals (dI/dt), and change in the number of recovered individuals (dS/dt) for that day.
    """
    #n= S+I+R # Can define it in the function, so it only exists here (local variable)
    dS_dt = -beta * ((S*I)/(S+I+R))
    dI_dt = beta * ((S*I)/(S+I+R)) - (gamma*I)
    dR_dt = gamma * I
    return dS_dt, dI_dt, dR_dt
#-------------------------------------------------------------------

#---------------------------Main simulation-------------------------
#Intialize parameters-----------------------------------------------
# Total population, N
N = 1000
# Initial number of infected and recovered individuals
I0 = 46 # number of infected individuals at day 0
R0 = 79 # number of recovered individuals at day 0
S0 = N - I0 - R0 # Everyone else is susceptible to infection initially
# Contact rate, beta, and mean recovery rate, gamma
BETA = 0.4   # Infection rate (this equates to 40%)
GAMMA = 0.6  # Recovery rate (this equates to 60%)
# Time grid (in days)
DAYS = 10
t = np.linspace(0, DAYS, DAYS+1) #start, stop, number of increments
#Alternative: np.arrange(0, DAYS) # returns an array of integers

# Initialize arrays
S = np.zeros(DAYS+1)
I = np.zeros(DAYS+1)
R = np.zeros(DAYS+1)

# Set initial values
S[0], I[0], R[0] = S0, I0, R0
#Equivalent code
#S[0] = S0
#I[0] = I0
#R[0] = R0

#------------------------Run Simulation-----------------------------------
# Run the model
for day in range(1, DAYS+1):   #1, 2, ....50
   dS, dI, dR = sir_model(S=S[day-1], I=I[day-1], R=R[day-1], beta=BETA, gamma=GAMMA)
   S[day] = S[day-1] + dS
   I[day] = I[day-1] + dI
   R[day] = R[day-1] + dR

print(S); print(I); print(R)

#---------------------Summarizing and Plotting the Same Results-----------
plt.figure(figsize=(20,20))
plt.plot(t, S, label="Number of Susceptible Individuals")
plt.plot(t, I, label="Number of Infected Individuals")
plt.plot(t, R, label="Number of Recovered Individuals")
plt.xlabel("Days")
plt.ylabel("Number of Individuals")
plt.title("SIR  Simulation")
plt.legend()
plt.show()