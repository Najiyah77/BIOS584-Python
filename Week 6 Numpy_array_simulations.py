#---------------------------------------------------------------
# Module 6 Exercises: Numpy Array Simulations
# Name:
# Date:
#---------------------------------------------------------------

import numpy as np #np is an alias
import matplotlib.pyplot as plt #plt is an alias

#-------------------------------------------------------------
# np.random and np.random.seed
#-------------------------------------------------------------
np.random.seed(42) #Add a seed to make it reproducible and the
#random numbers are drawn from a “pre-generated” set. Can be 42 or any other number.

random_normal_vector = np.random.normal(loc = 0, scale = 1, size=100)
print(random_normal_vector)

random_normal_vector2 = np.random.normal(loc = 0, scale = 1, size=100)
print(random_normal_vector2)

random_normal_vector == random_normal_vector2 #Equality of vectors is done ELEMENT-WISE
#They are the same because the random numbers were generated using the same random seed (42)
# and we set the np.random.seed

#-------------------- Size parameter, simulating random 1D vs 2D numpy arrays)
random_normal_2d = np.random.normal(loc = 0, scale = 1, size = (100,3)) #size(rows,columns)
print(random_normal_2d)

###############################################################
# Normal Distribution Simulation Application
###############################################################
np.random.seed(2026) #Set random seed

#--------- Initialize simulation parameters -----------
N = 500 # Sample size of people who come to that clinic
# Assume SBP is approximately Normal in this population
mean_sbp = 125     # average systolic BP (mmHg)
sd_sbp = 15        # standard deviation (mmHg)

#--------- Begin simulation -----------
# Simulate SBP values for N randomly sampled people from the population
sbp = np.random.normal(loc=mean_sbp, scale=sd_sbp, size=N)

# Classify the N people as having hypertension vs not based on their SBP (hypertension: SBP >= 140)
hypertensive = sbp >= 140 #creates a numpy array of boolean True/False values

#--------- Summarize and Visualize Sim Results -----------
#Number of people with hypertension
print(hypertensive.sum()) #returns the number of True values. "True" is equal to 1, "False" = 0
#Proportion of people who have hypertension in Clinic (prevalence) is the mean
print(f"Estimated hypertension prevalence in {N} Clinic Patients: {hypertensive.mean()}")
print(f"Average SBP of {N} Clinic Patients: {sbp.mean():.3f}")

# Visualization of dist of SBP values for clinic patients (histogram)
plt.hist(sbp, bins=25)
plt.xlabel("Systolic BP (mmHg)")
plt.ylabel("Number of Clinic Patients")
plt.title("Simulated SBP distribution (Normal)")
plt.grid(True) #adds gridlines
plt.show()

###############################################################
# Poisson Distribution Simulation Application
###############################################################
np.random.seed(1) #set random seed

#--------- Initialize simulation parameters -----------
DAYS = 30
average_daily_cases = 12   # expected number of cases per day (lambda or rate/day)

#--------- Begin Simulation -----------
# Simulate daily counts
daily_cases = np.random.poisson(lam = average_daily_cases, size = DAYS)
print(f"Daily cases: {daily_cases}")
#--------- Summarize and Visualize Sim Results -----------
# Print summary statistics
print(f"Mean cases: {daily_cases.mean()}")
print(f"Variance: {daily_cases.var()}")
print(f"Standard Deviation: {daily_cases.std()}")
#Visualization
plt.plot(daily_cases)
plt.xlabel("Day")
plt.ylabel("ED Visits")
plt.title("Simulated Daily ED Visits (Poisson)")
plt.grid(True)
plt.show()

###############################################################
# Binomial Distribution Simulation Application
###############################################################
np.random.seed(1992)
#--------- Initialize simulation parameters -----------
N = 1000 #sample size for each simulation
p = 0.30 #population/true infection rate of disease
REPS = 500  # repeat simulation this many times

# Initialize 1D arrays to store numbers for each simulation
binom1_totals = np.zeros(REPS) #each element in array = # of people infected in simulation
binom2_totals = np.zeros(REPS)

#--------- Begin simulation -----------
for i in range(REPS): #range(REPS) = 0,1,2,3...(REPS - 1)

    # Method 1: Binomial (individual Bernoulli trials)
    infected1 = np.random.binomial(1, p, size=N) #returns array of 0's and 1's
    binom1_totals[i] = infected1.sum()

    # Method 2: Single binomial draw
    binom2_totals[i] = np.random.binomial(N, p) #returns an integer of # of "successes"
    #In this application, "successes" = people infected

#--------- Summarize and Visualize Sim Results -----------
# Print summary statistics
print("Binom Method 1 mean:", binom1_totals.mean())
print("Binom Method 2 mean:", binom2_totals.mean())
print("Expected value:", N * p)

