import matplotlib.pyplot as plt
import numpy as np

# All of our inputs 
N = int(input("Type in your interval: "))                       # Our number of intervals 
d = float(input("Type in your distance (in meters): "))         # Max Distance (in meters)
t = float(input("Type in your max time (in seconds): "))        # Max time (in seconds)
v_walk = 1.0                                                    # Walking velocity (m/s)

interval_S = [] 
interval_t = [] 
interval_D = [] 
interval_Dr = [] 

# Dynamically collect dose rates for N + 1 grid points
print(f"\nPlease enter the {N + 1} dose rate values at each boundary point:")
for i in range(N + 1):
    dr_val = float(input(f"  Dose rate at point {i}: "))
    interval_Dr.append(dr_val)

h1 = d / N 
h2 = t / N 

def find_position_interval(N, d, h1):
    x = 0.0
    while len(interval_S) < (N + 1):
        if len(interval_S) == N: 
            interval_S.append(d)
            return interval_S
        else: 
            interval_S.append(round(x, 7))
            x += h1

def find_time_interval(N, t, h2):
    x = 0.0
    while len(interval_t) < (N + 1):
        if len(interval_t) == N: 
            interval_t.append(t) 
            return interval_t
        else: 
            interval_t.append(round(x, 7))
            x += h2

def find_dosage():
    k = 0
    # Loop over the N intervals
    while k < N:
        # Trapezoidal rule: average dose rate of the interval multiplied by delta_t
        delta_t = interval_t[k+1] - interval_t[k]
        D_k = ((interval_Dr[k] + interval_Dr[k+1]) / 2) * delta_t
        interval_D.append(round(D_k, 7))
        k += 1
    return interval_D

a = find_position_interval(N, d, h1)
b = find_time_interval(N, t, h2)

print("\nOur position vector for each point is:")
print(a)

print("\nOur time vector for each position point is: ")
print(b)

c = find_dosage()
print("\nDose vector per interval:")
print(c)

print("\nDose total:")
print(round(sum(interval_D), 7))

cumulative_dose = [0.0] + list(np.cumsum(interval_D))

# -------------------------------- Plot --------------------------------------

fig, ax1 = plt.subplots(figsize=(9, 6))

# Bottom Axis: Position vs. Dose Rate
ax1.plot(interval_S, interval_Dr, 'go-', label='Dose Rate Profile', markersize=8)  
ax1.set_title('Radiation Dose Rate Along Path Distance', fontsize=14, fontweight='bold', pad=25)
ax1.set_xlabel('Position Along Path [m]', fontsize=12)
ax1.set_ylabel('Dose Rate [Sv/s]', fontsize=12)
ax1.set_xticks(interval_S)
ax1.grid(True, linestyle=':', alpha=0.6)

# Top Axis: Shared mapping for Elapsed Time
ax2 = ax1.twiny()  
ax2.set_xlim(ax1.get_xlim()) 
ax2.set_xticks(interval_S)   
time_labels = [f"{t_val}s" for t_val in interval_t]
ax2.set_xticklabels(time_labels, fontsize=10, color='dimgray')
ax2.set_xlabel('Elapsed Time [s]', fontsize=12, color='dimgray', labelpad=10)

ax1.legend(loc='upper right', fontsize=10, framealpha=0.4, facecolor='white', edgecolor='gray')
plt.tight_layout()
plt.show()

fig, ax1 = plt.subplots(figsize=(9, 6))

# Bottom Axis: Position vs. Cumulative Dose
ax1.plot(interval_S, cumulative_dose, 'bo-', label='Accumulated Dose', markersize=8)  
ax1.set_title('Total Integrated Dose vs. Path Metrics', fontsize=14, fontweight='bold', pad=25)
ax1.set_xlabel('Position Along Path [m]', fontsize=12)
ax1.set_ylabel('Total Dose Received [Sv]', fontsize=12)
ax1.set_xticks(interval_S)
ax1.grid(True, linestyle=':', alpha=0.6)

# Top Axis: Shared mapping for Elapsed Time
ax2 = ax1.twiny()  
ax2.set_xlim(ax1.get_xlim()) 
ax2.set_xticks(interval_S)   
ax2.set_xticklabels(time_labels, fontsize=10, color='dimgray') # Uses the same time_labels list
ax2.set_xlabel('Elapsed Time [s]', fontsize=12, color='dimgray', labelpad=10)

ax1.legend(loc='lower right', fontsize=10, framealpha=0.4, facecolor='white', edgecolor='gray')
plt.tight_layout()
plt.show()
