"""
Fitting tools for battery model parameter extraction
"""

import numpy as np

def least_squares(v_vec, i_vec, ocv, dt):
    """
    Use least squares to estimate ECM parameters
    """

    ocv = np.asarray(ocv)
    ocv_size = ocv.shape[0] if len(ocv.shape) > 0 else 1

    if ocv_size == 1:
        phi = np.vstack([-i_vec[1:], -i_vec[:-1], -(ocv - v_vec[:-1])]).T
        YY = ocv - v_vec[1:]
    elif ocv_size == len(v_vec):
        phi = np.vstack([-i_vec[1:], -i_vec[:-1], -(ocv[:-1] - v_vec[:-1])]).T
        YY  = ocv[1:] - v_vec[1:]
    else:
        raise ValueError('Dimensions of V0 is incompatible with V')

    theta = np.linalg.lstsq(phi, YY, rcond=None)[0]

    # Unpack the parameters
    b1 = theta[0]
    b0 = theta[1]
    a0 = theta[2]

    # Calculate the final values
    R1 = (b0 - a0*b1) / (a0+1)
    C1 = dt / (b0 - a0*b1)
    Rs = b1

    cond_num = np.linalg.cond(phi.T @ phi)

    return Rs, R1, C1, cond_num
