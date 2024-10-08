# -*- coding: utf-8 -*-
"""
script:             tools_ids_profiles_plot.py

creation date:      13/10/2015, 16h10
modification date:  16/08/2024, 17h45

@author: Millot Laurent
"""


import numpy as np
import matplotlib.pyplot as plt
import math


# ----------
def magnitude(the_value):
    
    if (the_value == 0):
        return 0

    return int(math.floor(math.log10(abs(the_value))))


# ----------
def calculate_amplification_coefficient(the_value):
    
    the_value = np.abs(the_value)
    
    if the_value < 1.0:
        the_exponent = np.log10(the_value)
        the_exponent = np.floor(the_exponent)
        the_amp_coef = 10 ** (-the_exponent)
    else:
        the_amp_coef = 1.0

    return the_amp_coef


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
        y_max_val = np.round(y_max_val, 1)

    if np.abs(y_min_val) < 1.0:
        y_min_val = np.round(y_min_val, 1)

#    if not y_max_val:
#        y_max_val = the_step / 100.

    if I_debug:
        print("y_max_val: " + str(y_max_val))
        print("y_min_val: " + str(y_min_val))
        print("the_dynamic: " + str(the_dynamic))
        print("relative_dynamic: " + str(relative_dynamic))
        print("the_step: " + str(the_step))

    return y_min_val, y_max_val


# ----------
def calculate_xticks(the_xticks):
    # calculate the positions of subband number indications as a function
    # of the subband width
    delta_xticks = the_xticks[1:] - the_xticks[:-1]

    for the_index in range(len(delta_xticks)):
        the_delta = delta_xticks[the_index]
        if the_delta >= .5:
            the_xticks[the_index] = the_xticks[the_index] + .45 * the_delta
        else:
            the_xticks[the_index] = the_xticks[the_index] + .2

    return the_xticks


# ----------
def make_ticks_and_box_invisible(ax):
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_color("none")
    ax.spines["left"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.set(xticks=[], yticks=[])


# ----------
def calculate_subbands_limits_abciss(freq_array):
    x_limits = freq_array[2:] / freq_array[1:-1]
    x_limits = np.hstack((np.array([0, 1]), np.log2(x_limits)))

    x_cumul = 0

    for the_index in range(len(x_limits)):
        x_cumul = x_cumul + x_limits[the_index]
        x_limits[the_index] = x_cumul

    return x_limits


# ----------
def plot_IDS_profile(ids_array, ids_mean_level, freq_array,
                     channels_number, min_ids_value, max_ids_value,
                     fig_name, fig_path, the_radical="ids_profile_",
                     the_format="pdf", the_fig_size=(11, 8.5), the_dpi=72,
                     I_close_fig=1):

    x_limits = calculate_subbands_limits_abciss(freq_array)

    if channels_number == 1:
        y_ids_array = np.hstack((ids_array[0], ids_array))
    else:
        y0 = np.array([[ids_array[0, 0]], [ids_array[1, 0]]])
        y_ids_array = np.hstack((y0, ids_array))

    sb_tick_locations = x_limits.copy()
    sb_tick_locations = calculate_xticks(sb_tick_locations)

    plt.figure(0, figsize=the_fig_size, dpi=the_dpi)

    # ---- relative weights axe ----
    ax2 = plt.subplot2grid((10, 12), (1, 0), rowspan=9, colspan=3)
    x_pos = -.5
    y_pos = .9
    y_offset = .05

    the_str = "Relative Weights (dB)"
    plt.text(x_pos, y_pos, the_str, size=12)

    if channels_number == 1:
        for the_index in range(len(ids_array)):
            y_pos = y_pos - y_offset
            the_str = str(the_index+1) + ":  " + str(ids_array[the_index])
            plt.text(x_pos, y_pos, the_str, size=12)
    else:
        subbands_number = ids_array.shape
        subbands_number = subbands_number[1]
        
        for the_index in range(subbands_number):
            y_pos = y_pos - y_offset
            plt.text(x_pos, y_pos, str(the_index+1) + ":", size=12)

            plt.text(x_pos+.25, y_pos, str(ids_array[0, the_index]),
                     color="red", size=12)

            plt.text(x_pos+.75, y_pos, str(ids_array[1, the_index]), size=12)

    plt.xlim(0, 1)
    make_ticks_and_box_invisible(ax2)

    # ---- mean level axe ----
    ax4 = plt.subplot2grid((10, 12), (0, 0), colspan=3)

    if channels_number == 1:
        the_str = "Mean Level (dB FS)"
        plt.text(x_pos, .55, the_str, size=12)

        plt.text(x_pos, 0, str(ids_mean_level), color="red", size=12)
    else:
        the_str = "Mean Levels (dB FS)"
        plt.text(x_pos, .55, the_str, size=12)

        plt.text(x_pos, 0, str(ids_mean_level[0]), color="red", size=12)

        plt.text(x_pos+.35, 0, str(ids_mean_level[1]), size=12)

    plt.xlim(0, 1)
    make_ticks_and_box_invisible(ax4)

    # ---- IDS profile axe ----
    ax3 = plt.subplot2grid((10, 12), (0, 3), rowspan=10, colspan=9)

    # plot the ids profile
    if channels_number == 1:
        ax3.step(x_limits, y_ids_array, color="red",
                 linewidth=3.5, linestyle="-")
    else:
        ax3.step(x_limits, y_ids_array[0], color="red",
                 linewidth=3.5, linestyle="-")

        ax3.step(x_limits, y_ids_array[1], color="black",
                 linewidth=3.5, linestyle="-")

    # set the y_min_val, y_max_val and the y position for the subband numbers
    # indications (second xaxis, at the top of the plot)

    if min_ids_value == 0.0 and max_ids_value == 0.0:
        y_min_val = -5.
        y_max_val = 5
    else:
        y_min_val, y_max_val = calculate_plot_ylimits(min_ids_value, 
                                                      max_ids_value)

    sbIndicationy_pos = y_max_val + .25

    # add the top axis: subband number indications
    for the_index in range(len(sb_tick_locations) - 1):
        plt.text(sb_tick_locations[the_index], sbIndicationy_pos,
                 str(the_index+1), horizontalalignment="center",
                 size=12)

    # set x and y limits
    plt.xlim(x_limits[0], x_limits[-1])

    plt.ylim(y_min_val, y_max_val)

    # set x ticks
    plt.xticks(x_limits, freq_array, rotation=90, fontsize=11)

    # set the font size for x and y axes
    xticklabels = plt.getp(plt.gca(), "xticklabels")
    yticklabels = plt.getp(plt.gca(), "yticklabels")
    plt.setp(xticklabels, fontsize=11)

    plt.setp(yticklabels, fontsize=11)

    # add the xlabel
    plt.xlabel("Frequency (Hz)", fontsize=12, labelpad=0)

    # building the grid
    ax3.grid(which="major", axis="x", linewidth=0.75, linestyle="-",
             color="0.75")
    ax3.grid(which="minor", axis="x", linewidth=0.25, linestyle="-",
             color="0.75")
    ax3.grid(which="major", axis="y", linewidth=0.75, linestyle="-",
             color="0.75")
    ax3.grid(which="minor", axis="y", linewidth=0.25, linestyle="-",
             color="0.75")

    # ---- main title ----
    # (crossing the different subplots!)
    plt.suptitle("IDS profile: " + fig_name, fontsize=14)

    # ---- create the figure file -----
    file_name = the_radical + fig_name + ".pdf"
    plt.savefig(fig_path / file_name, format="pdf")

    if I_close_fig == 1:
        plt.close()


# ----------
def main():
    fig_name = "e5L"
    fig_path = "../"

    ids_array = np.array([[-17.07, -3.96, -6.2, -7.81, -12.1, -12.53,
                          -13.69, -24.53, -23.94, -38.89],
                         [-18.07, -4.96, -7.2, -8.81, -13.1, -14.53,
                          -14.69, -25.53, -24.94, -39.89]])

    # gives:
    # - the rows number for a matrix,
    # - the elements number for an 1D-array !
    channels_number = len(ids_array)

    if channels_number > 2:
        channels_number = 1

    ids_mean_level = np.array([-18.51, -19.51])
    freqsArray = np.array([0, 50, 200, 400, 800, 1200, 1800,
                           3000, 6000, 15000, 22050])

    min_ids_value = ids_array.min()
    max_ids_value = ids_array.max()

    plot_IDS_profile(ids_array, ids_mean_level, freqsArray,
                     channels_number, min_ids_value, max_ids_value,
                     fig_name, fig_path)


# ----------
if __name__ == "__main__":
    main()
