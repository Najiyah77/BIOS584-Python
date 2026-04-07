#-----------------------------------------------------------------------------------------------------------------------
# Name: Najiyah Williamson
# Date: 4/6/26
# BIOS 584 Assignment 3 (Helper Functions Module file)
#-----------------------------------------------------------------------------------------------------------------------
""" This module contains functions to simulate and visualize the spread of an infectious disease """

import numpy as np

#====================================================================================================
# SIR Model differential equations Helper Function
#====================================================================================================
def sir_model(S_t, I_t, R_t, beta, gamma):
    """
    This function takes in a specified infection rate (beta), recovery rate (gamma) and the
    current number of susceptible (S_t), infected (I_t) and recovered individuals (R_t) for a given day.
    It returns the rate of change in the number of susceptible individuals (dS/dt), change in the number
    of infected individuals (dI/dt), and change in the number of recovered individuals (dR/dt) for that day.
    """
    dS_dt = -beta * ((S_t*I_t)/(S_t+I_t+R_t)) #Change in number of susceptible individuals at day t
    dI_dt  = beta * ((S_t*I_t)/(S_t+I_t+R_t)) - gamma*I_t #Change in number of infected people at day t
    dR_dt = gamma*I_t #Change in number of recovered individuals at day t
    return dS_dt, dI_dt, dR_dt

#Note: Instead of using a fixed N, you can use S+I+R because N=S+I+R. (When doing the sird_model, you have to do this
# because N will change since people die. So it's best not to feed in a fixed N and use S+I+R).

#====================================================================================================
# SIRD Model differential equations Helper Function (5 points)
#====================================================================================================
def sird_model(S_t, I_t, R_t, beta, gamma, mu):
    """
    This function takes in a specified infection rate (beta), recovery rate (gamma) and the
    current number of susceptible (S), infected (I) and recovered individuals (R) for a given day. N is equivalent to S+I+R.
    It returns the rate of change in the number of susceptible individuals (dS/dt), change in the number
    of infected individuals (dI/dt), change in the number of recovered individuals (dR/dt), and the change in deceased
     individuals (dD/dt) for that day. The people who died are (mu*I).
    """
    dS_dt = -beta * ((S_t*I_t)/(S_t+I_t+R_t))
    dI_dt = beta * ((S_t*I_t)/(S_t+I_t+R_t))  - (gamma * I_t) - (mu * I_t)
    dR_dt = gamma * I_t
    dD_dt = mu * I_t
    return dS_dt, dI_dt, dR_dt, dD_dt

#Note: N = S_t + I_t + R_t

#====================================================================================================
# SIRDV Model differential equations Helper Function
#====================================================================================================
def sirdv_model(S_t, I_t, R_t, V_t, beta, gamma, mu, vac_rate):
    """
    This function takes in a specified infection rate (beta), recovery rate (gamma) and the
    current number of susceptible (S), infected (I), recovered individuals (R), and vaccinated individuals (V)
    for a given day. N is equivalent to S+I+R+V. It returns the rate of change in the number of susceptible
    individuals (dS/dt), which may decrease based on the vaccination rate (-vac_rate * S_t), change in the number of
    infected individuals (dI/dt), change in the number of recovered individuals (dR/dt), the change in deceased
     individuals (dD/dt), and the change in vaccinated individuals (dV/dt) for that day. The people
    who died are (mu*I). Vaccinated individuals are formerly susceptible individuals who got vaccinated (vac_rate * S_t).
    """
    dS_dt = -beta * ((S_t * I_t) / (S_t + I_t + R_t + V_t)) - vac_rate * S_t
    dI_dt = beta * ((S_t * I_t)/(S_t + I_t + R_t + V_t))  - (gamma * I_t) - (mu * I_t)
    dR_dt = gamma * I_t
    dD_dt = mu * I_t
    dV_dt = vac_rate * S_t
    return dS_dt, dI_dt, dR_dt, dD_dt, dV_dt

#Note for this model: N = S_t + I_t + R_t + V_t
#====================================================================================================
# Function to Run the Whole Simulation based on the model ("SIR", "SIRD" or "SIRDV") the user specifies
#====================================================================================================

#I've written the parameters for the run_sim function for you. Tweak the function definition so the function
# simulates a "SIR" model for 100 days where S_0 = 997, I_0 = 3, R_0 = 0, V_0, beta=.4, gamma = .035,
# mu = 0, vac_rate = 0 BY DEFAULT.
# Hint: see Functions cheat sheet to remember how to set default arguments

def run_sim(S_0=997, I_0=3, R_0=0, V_0=0, beta=0.4, gamma=.035, mu=0, vac_rate=0, days=100, model_choice="SIR"):
    """
    The parameters are S_0 (the number of susceptible individuals at day 0), I_0
    (number of infected individuals at day 0), R_0 (number recovered individuals at day 0), beta (in-
    fection rate), gamma (recovery rate), mu (death rate), vac_rate (vaccination rate), days (number of
    days to simulate the outbreak), model choice (the simulation the user requested, it can be“SIR”,
    “SIRD” or “SIRDV”). The function will default to a "SIR" model for 100 days.
    """
    # -----------------------------------------------------------------------
    # Initialize arrays of zeroes with length "days" to keep track of the S, I, R, D and V individuals for each day
    S = np.zeros(days)
    I = np.zeros(days)
    R = np.zeros(days)
    D = np.zeros(days)
    V = np.zeros(days)

    # Set initial number of susceptible (S), infected (I), recovered (R) people on day 0 in the S, I, R arrays
    # based on the parameters S_0, I_0, R_0
    S[0], I[0], R[0], V[0] = S_0, I_0, R_0, V_0 # added since V_0=0 was blurred out above
    #-----------------------------------------------------------------------
    # Note: Deceased and vaccinated individuals day 0 will be 0, so you don't need to assign D[0] or V[0] to anything,
    # as the first element of your initialized array is already 0


    # -----------------------------------------------------------------------
    # Simulate the number of susceptible (S), infected (I), recovered (R) and if relevant,
    # the deceased (D) & vaccinated (V) people for the specified number of days
    # -----------------------------------------------------------------------
    for day in range(1, days): #For each day...
    #Get dS, dI, dR and if relevant, dD and dV to count up the number of S,I,R,D and V people for that day
    #based on the specified infection, recovery, death and vaccination rates and the # of S,I,R,D and V people the day before
    #Hint: use an if, elif, else loop based on "model_choice" and call the sir_model, sird_model or sirdv_model
    # helper functions you defined above

        #Get rates of change (dS, dI, dR, & if needed, dD, dV)
        if model_choice == "SIR":
            dS, dI, dR = sir_model(S_t=S[day - 1], I_t=I[day - 1], R_t=R[day - 1], beta=beta, gamma=gamma)
            dV = dD = 0 #Vaccination and death rates not considered in SIR model so the "change" is 0

        #YOU FILL IN THE REST: elif model_choice == ....else...
        elif model_choice == "SIRD":
            dS, dI, dR, dD = sird_model(S[day - 1], I[day - 1], R[day - 1], beta, gamma, mu)
            dV = 0

        elif model_choice == "SIRDV":
            dS, dI, dR, dD, dV = sirdv_model(S[day - 1], I[day - 1], R[day - 1], V[day - 1], beta, gamma, mu, vac_rate)

        else:
            raise ValueError("Invalid model. Choose 'SIR', 'SIRD', or 'SIRDV'.")

        #Fill in the arrays w/ # of indv for that day based on the calculated dS, dI, dR, dD, dV
       #and the # of indv from the day before (day -1).
       # Example: S[day] = S[day-1] + dS
        S[day] = S[day - 1] + dS
        I[day] = I[day - 1] + dI
        R[day] = R[day - 1] + dR
        D[day] = D[day - 1] + dD
        V[day] = V[day - 1] + dV
        # -----------------------------------------------------------------------
    # Return the final arrays S, I, R, D, V
    # -----------------------------------------------------------------------
    return S, I, R, D, V


