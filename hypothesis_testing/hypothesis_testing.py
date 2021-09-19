'''
To understand the hypothesis testing
'''

# importing the libraries needed.

import pandas as pd
import math
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import logging
import sys
import re

# pattern used for regex
comparator_pattern= "\<\=|\>\=|\<|\>|="
greater_than_pattern = "\<\=X|X\>\="
lesser_than_pattern = "\>\=X|X\<\="
equal_pattern = "X\=|\=X"
def check_equality(input_string):
    if not input_string:
        return

    try:
        if re.search(greater_than_pattern, input_string.replace(" ", "").upper()):
            return "Left"
        elif re.search(lesser_than_pattern, input_string.replace(" ", "").upper()):
            return "Right"
        elif re.search(equal_pattern, input_string.replace(" ", "").upper()):
            return "Center"
        else:
            return "Invalid"

    except:
        return

def plot_graph_left_right(z1, z2, Z):
    print(z1, z2, Z)
    x = np.arange(z1, z2, 0.001)  # range of x in spec
    x_all = np.arange(-10, 10, 0.001)  # entire range of x, both in and out of spec
    # mean = 0, stddev = 1, since Z-transform was calculated
    y = norm.pdf(x, 0, 1)
    y2 = norm.pdf(x_all, 0, 1)
    fig, ax = plt.subplots(figsize=(9, 6))
    plt.style.use('fivethirtyeight')
    ax.plot(x_all, y2)

    ax.fill_between(x, y, 0, alpha=0.3, color='b')
    ax.fill_between(x_all, y2, 0, alpha=0.1)
    ax.set_xlim([-4, 4])
    ax.set_xlabel('# of Standard Deviations Outside the Mean')

    # mark the Z line
    x_coordinates = [Z, Z]
    y1 = norm.pdf(Z, 0, 1)
    y_coordinates = [0, y1]

    plt.plot(x_coordinates, y_coordinates, alpha=0.3, color='r')

    ax.set_yticklabels([])
    ax.set_title('Normal Gaussian Curve')

    plt.savefig('normal_curve.png', dpi=72, bbox_inches='tight')
    plt.show()

def plot_graph_two(zL1, zL2, zR1, zR2, Z):
    print(zL1, zL2, zR1, zR2, Z)
    left_x = np.arange(zL1, zL2, 0.001)  # range of x in spec
    right_x = np.arange(zR1, zR2, 0.001)  # range of x in spec
    x_all = np.arange(-10, 10, 0.001)  # entire range of x, both in and out of spec

    # mean = 0, stddev = 1, since Z-transform was calculated
    left_y = norm.pdf(left_x, 0, 1)
    right_y = norm.pdf(right_x, 0, 1)
    y_all = norm.pdf(x_all, 0, 1)
    fig, ax = plt.subplots(figsize=(9, 6))
    plt.style.use('fivethirtyeight')
    ax.plot(x_all, y_all)

    ax.fill_between(left_x, left_y, 0, alpha=0.3, color='b')
    ax.fill_between(right_x, right_y, 0, alpha=0.3, color='b')
    ax.fill_between(x_all, y_all, 0, alpha=0.1)
    ax.set_xlim([-4, 4])
    ax.set_xlabel('# of Standard Deviations Outside the Mean')

    # mark the Z line
    x_coordinates = [Z, Z]
    y1 = norm.pdf(Z, 0, 1)
    y_coordinates = [0, y1]

    plt.plot(x_coordinates, y_coordinates, alpha=0.3, color='r')

    ax.set_yticklabels([])
    ax.set_title('Hypothesis')

    # plt.savefig('normal_curve.png', dpi=72, bbox_inches='tight')
    plt.show()

def hypothesis(population_mean, sample_number, sample_mean, std_deviation, null_hypothesis, confidence_level = 0.95):
    x_bar_mew = sample_mean - population_mean
    sigma_sqrt_number = std_deviation / math.sqrt(sample_number)
    level_of_siginificance = 1 - confidence_level
    test_statistic = x_bar_mew / sigma_sqrt_number
    critical_value = norm.ppf(level_of_siginificance)

    equality_condition = check_equality(null_hypothesis)
    if equality_condition == "Left":
        z1 = -4
        if critical_value < 0:
            z2 = critical_value
        else:
            z2 = -critical_value
        min_value = -sys.maxsize - 1
        if test_statistic > (min_value)  and test_statistic < z2:
            print("Falls in Rejection region")
        else:
            print("Not Falls in Rejection region")
        plot_graph_left_right(z1, z2, test_statistic)
    elif equality_condition == "Right":
        z1 = abs(critical_value)
        z2 = 4
        max_size = sys.maxsize
        if test_statistic > (z1)  and test_statistic < max_size:
            print("Falls in Rejection region")
        else:
            print("Not Falls in Rejection region")
        plot_graph_left_right(z1, z2, test_statistic)
    else:
        critical_value_left = norm.ppf(level_of_siginificance/2)
        if critical_value_left > 0:
            critical_value_left = -critical_value_left
        critical_value_right = norm.ppf(level_of_siginificance/2)
        critical_value_right = abs(critical_value_right)
        print(critical_value_right, critical_value_left, test_statistic)

        if test_statistic > critical_value_left and critical_value_right > test_statistic:
            print("Not Falls in Rejection region")
        else:
            print("Falls in Rejection region")

        plot_graph_two(-4, critical_value_left, critical_value_right, 4, test_statistic)



if __name__ == '__main__':
    population_mean = 700
    std_deviation = 120
    sample_number = 100
    sample_mean = 650
    confidence_level = 0.99
    null_hypothesis = "X >= 700"
    if sample_number < 30:
        print("use T test")
        sys.exit()
    hypothesis(population_mean, sample_number, sample_mean, std_deviation, null_hypothesis, confidence_level)
    # print(result)
