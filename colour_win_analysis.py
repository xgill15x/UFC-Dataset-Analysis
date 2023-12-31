"""
Author: Jason Gill

Description:
Our goal in this program is to determine if there is a difference in the number of wins between red-gloved and blue-gloved fighters. 
Further, we want to determine if one of the colours wins significantly more than the other. Conclusion can be found in the report.
"""

import pandas as pd
import numpy as np
from scipy import stats

import helper

def wins_per_event(red_wins, blue_wins):
    red_wins_per_event = red_wins.groupby('date').count()['R_fighter']
    blue_wins_per_event = blue_wins.groupby('date').count()['B_fighter']

    colour_wins_per_event = pd.merge(red_wins_per_event, blue_wins_per_event, left_index=True, right_index=True)
    colour_wins_per_event = colour_wins_per_event.rename(columns={'R_fighter': 'red_wins_per_event', 'B_fighter': 'blue_wins_per_event'})

    return colour_wins_per_event['red_wins_per_event'], colour_wins_per_event['blue_wins_per_event']

def main():
    red_wins, blue_wins = helper.seperate_colour_wins("data_sets/preprocessed_data.csv")

    red_wins_per_event, blue_wins_per_event = wins_per_event(red_wins, blue_wins)

    # pre-transformed average colour wins per event (left for debugging/curiosity) ----------------------------------
    # red_wins_per_event_avg = red_wins_per_event.mean()
    # blue_wins_per_event_avg = blue_wins_per_event.mean()
    # print(red_wins_per_event_avg, blue_wins_per_event_avg)
    # -----------------------------------------------------------

    red_wins_per_event_sqrt = np.sqrt(red_wins_per_event)
    blue_wins_per_event_sqrt = np.sqrt(blue_wins_per_event)
    
    helper.draw_colour_wins_plots([red_wins_per_event, blue_wins_per_event, red_wins_per_event_sqrt, blue_wins_per_event_sqrt])

    levene_result = stats.levene(red_wins_per_event_sqrt, blue_wins_per_event_sqrt)
    t_test_result = stats.ttest_ind(red_wins_per_event_sqrt, blue_wins_per_event_sqrt, equal_var=False)

    # Display the result
    print("Levene p-value:", levene_result.pvalue)
    print("T_test_statistic (Group1 - Red; Group2 - Blue):", t_test_result.statistic, "T_test p-value:", t_test_result.pvalue)

if __name__=='__main__':
    main()
