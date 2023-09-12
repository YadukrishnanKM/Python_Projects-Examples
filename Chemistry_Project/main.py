import numpy as np
import LAB

# program to Estimate Copper present in Electroplatting Effluent

cu = LAB.ConductionExperiments(None, None, None)
SO = cu.Estimation_of_Copper(np.linspace(
    5, 20, 4), np.array([.11, .21, .29, .39]))
