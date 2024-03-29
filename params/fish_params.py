import numpy as np


horizon = 600
state_dimemsion = 27
control_dimension = 5

Q = 9*np.diag(np.concatenate([[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], np.zeros((13,))]))
Q_final = 1500*np.diag(np.concatenate([[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], np.zeros((13,))]))
R = .05*np.diag([2, 2, 2, 2, 2])


nominal_init_stddev = 0.1
n_substeps = 5


# D2C parameters
feedback_n_samples = 40