# Constants for conversion
KPA_TO_PSI = 0.145038
KPA_TO_MMHG = 7.50062
KPA_TO_ATM = 0.00986923

def convert_pressure(kpa):
    psi = kpa * KPA_TO_PSI
    mmhg = kpa * KPA_TO_MMHG
    atm = kpa * KPA_TO_ATM
    return psi, mmhg, atm

# Input pressure in kilopascals
kpa = float(input("Enter pressure in kilopascals: "))

# Convert pressure
psi, mmhg, atm = convert_pressure(kpa)

# Display the results
print(f"{kpa} kilopascals is equivalent to:")
print(f"{psi:.2f} pounds per square inch (psi)")
print(f"{mmhg:.2f} millimeters of mercury (mmHg)")
print(f"{atm:.5f} atmospheres (atm)")
