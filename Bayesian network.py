import numpy as np 
import pandas as pd 
 
# Define the probabilities 
P_A = {"yes": 0.8, "no": 0.2} 
P_C = {"yes": 0.5, "no": 0.5} 
P_G_given_A_C = { 
("yes", "yes"): {"Good": 0.8, "OK": 0.2}, 
("no", "yes"): {"Good": 0.2, "OK": 0.8}, 
("yes", "no"): {"Good": 0.5, "OK": 0.5}, 
("no", "no"): {"Good": 0.1, "OK": 0.9}, 
} 
P_S_given_G = { 
"Good": {"yes": 0.7, "no": 0.3}, 
"OK": {"yes": 0.3, "no": 0.7}, 
} 
 
 
# Monte Carlo simulation function 
def monte_carlo_simulation(num_samples=10000, show_steps=False): 
simulation_data = [] 
count_S_yes_given_G_good = 0 
count_G_good = 0 
 
 
for i in range(num_samples): 
# Sample Aptitude Skills (A) 
A = "yes" if np.random.rand() < P_A["yes"] else "no" 
 
 
# Sample Coding Skills (C) 
C = "yes" if np.random.rand() < P_C["yes"] else "no" 
 
 
# Sample Grade (G) based on A and C 
G_probs = P_G_given_A_C[(A, C)] 
G = "Good" if np.random.rand() < G_probs["Good"] else "OK" 
 
 
# Sample Startup (S) based on G 
S_probs = P_S_given_G[G] 
S = "yes" if np.random.rand() < S_probs["yes"] else "no" 
 
 
# Update counts 
if G == "Good": 
count_G_good += 1 
if S == "yes": 
count_S_yes_given_G_good += 1 
 
 
# Store simulation details for the first 10 samples 
if i < 10 and show_steps: 
simulation_data.append({ 
"Sample": i + 1, 
"Aptitude (A)": A, 
"Coding (C)": C, 
"Grade (G)": G, 
"Startup (S)": S, 
"Count(G=Good)": count_G_good, 
"Count(S=yes|G=Good)": count_S_yes_given_G_good, 
}) 
 
 
# Print the simulation steps as a table 
if show_steps: 
df = pd.DataFrame(simulation_data) 
print("Simulation Steps (First 10 Samples):") 
print(df) 
 
# Calculate conditional probability 
if count_G_good == 0: 
return 0 # Avoid division by zero 
return count_S_yes_given_G_good / count_G_good 
 
 
# Run simulation with steps 
print("=== Monte Carlo Simulation (Detailed Steps) ===") 
num_samples = 10000 
estimated_probability = monte_carlo_simulation(num_samples, show_steps=True) 
 
 
# Print final output 
print(f"\nEstimated P(S=yes | G=Good) with {num_samples} samples: {estimated_probability}") 
