# -*- coding: utf-8 -*-
"""
script:             tools_ids_ylimits_determination.py

creation date:      25/11/2015, 22h53
modification date:  29/09/2024, 01h12

@author: Millot Laurent"""


import numpy as np


# ----------
def calculate_amplification_coefficient(the_value):
    
    the_value = np.abs(the_value)
    
    if the_value < 1.0:
        the_exponent = np.log10(the_value)
        the_exponent = np.floor(the_exponent)
        the_amp = 10 ** (-the_exponent)
    else:
        the_amp = 1.0

    return the_amp


# ----------
def calculate_plot_ylimits(min_ids_value, max_ids_value, I_debug=0):

    the_dynamic = np.abs(min_ids_value - max_ids_value)
    the_order = np.floor(np.log10(the_dynamic))
    the_coef = np.power(10, the_order)

    relative_dynamic = np.ceil(the_dynamic / the_coef)

    if relative_dynamic > 5.01:
        the_step = relative_dynamic / 10

    else:
        the_step = relative_dynamic / 5

    y_max_val = np.ceil(max_ids_value / the_step) * the_step
    y_min_val = np.floor(min_ids_value / the_step) * the_step

    if np.abs(y_max_val) < 1.0:
#        y_max_val = np.round(y_max_val, 1)
        y_max_val = np.ceil(y_max_val)
    else:
        y_max_val = 10 * np.ceil(y_max_val / 10)

    if np.abs(y_min_val) < 1.0:
#        y_min_val = np.round(y_min_val, 1)
        y_min_val = np.floor(y_min_val)
    else:
        y_min_val = 10 * np.floor(y_min_val / 10)

#    if not y_max_val:
#        y_max_val = the_step / 100.

    if I_debug:
        print('y_max_val: ' + str(y_max_val))
        print('y_min_val: ' + str(y_min_val))
        print('the_dynamic: ' + str(the_dynamic))
        print('relative_dynamic: ' + str(relative_dynamic))
        print('the_step: ' + str(the_step))

    return y_min_val, y_max_val


# ----------
def main():
    I_debug = 1
    the_min, the_max = calculate_plot_ylimits(-52.32, -.37, I_debug)

    print()
    print('valeur min: ' + str(the_min))
    print('valeur max: ' + str(the_max))
    print()


# ----------
if __name__ == "__main__":
    main()
