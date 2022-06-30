from action_classification import action_classification
from typing import List, Dict
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def count_action_type(reader: iter) -> List[int]:
    """
    Aggregate count of actions classified in action type.
    :param reader: the csv reader of the audit trail file.
    :return: a list of count of actions classified in action type.
            Output list items correspond to the following action type count:
            [creating, editing, deleting, revising, viewing, others]
    """
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    next(reader)
    for row in reader:
        """
        Each row has format: 
        ['Index', 'Event Time', 'Document', 'Tab', 'User', 'Description']
        Example: 
        ['1', '2021-08-21 19:12:19', 'Doc', 'N/A', 'x@x.com', 'Close document']
        """
        # Classify actions in action type
        action_type = action_classification.classify_action_type(row[4].strip())
        if action_type >= 0:
            count[action_type] += 1
    return count


def aggregate_count(reader: iter, file_name: str, separate_users=False) -> Dict:
    """
    Aggregate count of actions classified using the design space classification and the
    action type classification method.
    :param reader: the csv reader of the audit trail file.
    :param file_name: the file name of the csv that is being analyzed.
    :param separate_users: if more than one user is found in one csv file, would their counts be
                            counted separately?
    :return: a dictionary of counts for the file/each user in the file (depending on
            if separate_users is selected); counts are stored a nested list of count
            of actions classified using the design space and the action type
            classification methods.

            List items in the output Dict correspond to the following count:
            [[sketching, 3D features, mating, visualizing, browsing, other organizing],
             [creating, editing, deleting, revising, viewing, other]]
    """
    empty_count = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    next(reader)
    if not separate_users:
        count = empty_count
    else:
        count = {}

    for row in reader:
        """
        Each row has format: 
        ['Index', 'Event Time', 'Document', 'Tab', 'User', 'Description']
        Example: 
        ['1', '2021-08-21 19:12:19', 'Doc', 'N/A', 'x@x.com', 'Close document']
        """
        # Classify actions in action type
        action_type = action_classification.classify_action_type(row[4].strip())
        if action_type >= 0:
            if not separate_users:
                count[0][action_type] += 1
            else:
                user = file_name + '/' + row[4].strip().split("@")[0]
                if user not in count:
                    count[user] = empty_count
                count[user][1][action_type] += 1
    if separate_users:
        return count
    else:
        return {file_name: count}



def markov(reader: iter, file_name: str, separate_users=False) -> Dict:
    """
    Aggregate count of actions classified using the design space classification and the
    action type classification method.
    :param reader: the csv reader of the audit trail file.
    :param file_name: the file name of the csv that is being analyzed.
    :param separate_users: if more than one user is found in one csv file, would their counts be
                            counted separately?
    :return: a dictionary of counts for the file/each user in the file (depending on
            if separate_users is selected); counts are stored a nested list of count
            of actions classified using the design space and the action type
            classification methods.

            List items in the output Dict correspond to the following count:
            [[sketching, 3D features, mating, visualizing, browsing, other organizing],
             [creating, editing, deleting, revising, viewing, other]]
    """
    f = open('action_counting/Test.csv', 'r+')
    f.truncate(0)
    classifi = []
    next(reader)

    for row in reader:
        """
        Each row has format: 
        ['Index', 'Event Time', 'Document', 'Tab', 'User', 'Description']
        Example: 
        ['1', '2021-08-21 19:12:19', 'Doc', 'N/A', 'x@x.com', 'Close document']
        """
        # Classify actions in action type
        action_type = action_classification.classify_action_type(row[4].strip())
        if action_type >= 0:
            classifi.append(action_type)

    dff = pd.read_csv('action_counting/Test.csv', names=['classification', 'classification2'])
    dff['classification'] = classifi
    dff['classification2'] = dff['classification'].shift(-1)
    dff.to_csv('action_counting/Test.csv', index=False)
    # print(classifi)

def markovv(save_fig=""):
    df = pd.read_csv('action_counting/Test.csv')
    """
    df = pd.read_csv('action_counting/Prob.csv')

    df['sequence'] = ['Creating&Creating', 'Creating&Editing', 'Creating&Deleting', 'Creating&Reversing',
                      'Creating&Organizing', 'Creating&Viewing', 'Editing&Creating', 'Editing&Editing',
                      'Editing&Deleting', 'Editing&Reversing', 'Editing&Organizing', 'Editing&Viewing',
                      'Deleting&Creating', 'Deleting&Editing', 'Deleting&Deleting', 'Deleting&Reversing',
                      'Deleting&Organizing', 'Deleting&Viewing', 'Reversing&Creating', 'Reversing&Editing',
                      'Reversing&Deleting',
                      'Reversing&Reversing', 'Reversing&Organizing', 'Reversing&Viewing', 'Viewing&Creating',
                      'Viewing&Editing', 'Viewing&Deleting', 'Viewing&Reversing', 'Viewing&Organizing',
                      'Viewing&Viewing', 'Organizing&Creating', 'Organizing&Editing',
                      'Organizing&Deleting', 'Organizing&Reversing', 'Organizing&Organizing', 'Organizing&Viewing']

    df.to_csv('action_counting/Prob.csv', index=False)

    df = pd.read_csv('action_counting/Test.csv')
    df.loc[(df['classification'] == 0) & (df['classification2'] == 0), 'sequence'] = 'Creating&Creating'
    df.loc[(df['classification'] == 0) & (df['classification2'] == 1), 'sequence'] = 'Creating&Editing'
    df.loc[(df['classification'] == 0) & (df['classification2'] == 2), 'sequence'] = 'Creating&Deleting'
    df.loc[(df['classification'] == 0) & (df['classification2'] == 3), 'sequence'] = 'Creating&Reversing'
    df.loc[(df['classification'] == 0) & (df['classification2'] == 4), 'sequence'] = 'Creating&Organizing'
    df.loc[(df['classification'] == 0) & (df['classification2'] == 5), 'sequence'] = 'Creating&Viewing'
    df.loc[(df['classification'] == 1) & (df['classification2'] == 0), 'sequence'] = 'Editing&Creating'
    df.loc[(df['classification'] == 1) & (df['classification2'] == 1), 'sequence'] = 'Editing&Editing'
    df.loc[(df['classification'] == 1) & (df['classification2'] == 2), 'sequence'] = 'Editing&Deleting'
    df.loc[(df['classification'] == 1) & (df['classification2'] == 3), 'sequence'] = 'Editing&Reversing'
    df.loc[(df['classification'] == 1) & (df['classification2'] == 4), 'sequence'] = 'Editing&Organizing'
    df.loc[(df['classification'] == 1) & (df['classification2'] == 5), 'sequence'] = 'Editing&Viewing'
    df.loc[(df['classification'] == 2) & (df['classification2'] == 0), 'sequence'] = 'Deleting&Creating'
    df.loc[(df['classification'] == 2) & (df['classification2'] == 1), 'sequence'] = 'Deleting&Editing'
    df.loc[(df['classification'] == 2) & (df['classification2'] == 2), 'sequence'] = 'Deleting&Deleting'
    df.loc[(df['classification'] == 2) & (df['classification2'] == 3), 'sequence'] = 'Deleting&Reversing'
    df.loc[(df['classification'] == 2) & (df['classification2'] == 4), 'sequence'] = 'Deleting&Organizing'
    df.loc[(df['classification'] == 2) & (df['classification2'] == 5), 'sequence'] = 'Deleting&Viewing'
    df.loc[(df['classification'] == 3) & (df['classification2'] == 0), 'sequence'] = 'Reversing&Creating'
    df.loc[(df['classification'] == 3) & (df['classification2'] == 1), 'sequence'] = 'Reversing&Editing'
    df.loc[(df['classification'] == 3) & (df['classification2'] == 2), 'sequence'] = 'Reversing&Deleting'
    df.loc[(df['classification'] == 3) & (df['classification2'] == 3), 'sequence'] = 'Reversing&Reversing'
    df.loc[(df['classification'] == 3) & (df['classification2'] == 4), 'sequence'] = 'Reversing&Organizing'
    df.loc[(df['classification'] == 3) & (df['classification2'] == 5), 'sequence'] = 'Reversing&Viewing'
    df.loc[(df['classification'] == 4) & (df['classification2'] == 0), 'sequence'] = 'Organizing&Creating'
    df.loc[(df['classification'] == 4) & (df['classification2'] == 1), 'sequence'] = 'Organizing&Editing'
    df.loc[(df['classification'] == 4) & (df['classification2'] == 2), 'sequence'] = 'Organizing&Deleting'
    df.loc[(df['classification'] == 4) & (df['classification2'] == 3), 'sequence'] = 'Organizing&Reversing'
    df.loc[(df['classification'] == 4) & (df['classification2'] == 4), 'sequence'] = 'Organizing&Organizing'
    df.loc[(df['classification'] == 4) & (df['classification2'] == 5), 'sequence'] = 'Organizing&Viewing'
    df.loc[(df['classification'] == 5) & (df['classification2'] == 0), 'sequence'] = 'Viewing&Creating'
    df.loc[(df['classification'] == 5) & (df['classification2'] == 1), 'sequence'] = 'Viewing&Editing'
    df.loc[(df['classification'] == 5) & (df['classification2'] == 2), 'sequence'] = 'Viewing&Deleting'
    df.loc[(df['classification'] == 5) & (df['classification2'] == 3), 'sequence'] = 'Viewing&Reversing'
    df.loc[(df['classification'] == 5) & (df['classification2'] == 4), 'sequence'] = 'Viewing&Organizing'
    df.loc[(df['classification'] == 5) & (df['classification2'] == 5), 'sequence'] = 'Viewing&Viewing'
    df.to_csv('action_counting/Test.csv', index=False)
    df.groupby('sequence').size().to_csv('action_counting/Rezz.csv')
"""
    df1 = df.value_counts(["classification", "classification2"]).to_csv('action_counting/results.csv')
    df1 = pd.read_csv('action_counting/results.csv')
    df1.sort_values(['classification', 'classification2']).to_csv('action_counting/results.csv', index=False)

    df1 = pd.read_csv('action_counting/Helpp.csv')
    df2 = pd.read_csv('action_counting/results.csv')
    result = pd.merge(df2, df1, on=['classification', 'classification2'], how='outer')
    result['0'] = result['0'].fillna(0)
    result = result.sort_values(['classification', 'classification2'])
    result.to_csv('action_counting/output.csv', index=False)

    df = pd.read_csv('action_counting/output.csv')

    pocetak = 0
    kraj = 11
    i = 1
    df.insert(loc=3, column='percentages', value=0)
    listy = []

    while i <= 11:
        df1 = df.iloc[pocetak:kraj, 2]
        s = sum(df1)
        df2 = df.iloc[pocetak:kraj, 2].tolist()
        df3 = [x / s for x in df2]
        listy.extend(df3)
        pocetak = kraj
        kraj += 11
        i += 1

    df['percentages'] = pd.Series(listy)
    df.to_csv('action_counting/Rezzy.csv', index=False)

    # Read the .csv
    df = pd.read_csv('action_counting/Rezzy.csv')

    # Variables
    start = 0
    end = 11
    i = 1
    matrix = []  # for values
    actions = ["Creating-Part", "Creating-Assembly", "Editing-Part", "Editing-Assembly",
              "Editing-Non-geometry", "Deleting-Part", "Deleting-Assembly", "Reversing", "Organizing-Design",
              "Organizing-Support design process", "Viewing"]
    action_sum = 11  # number of actions

    # Iterate through .csv
    while i <= action_sum:
        df1 = df.iloc[start:end, 3].tolist()  # store .csv values in fourth column (percentages for analysis) to list
        matrix.append(df1)  # append a list to matrix in each iteration
        start = end
        end += action_sum
        i += 1
    # Prepare matrix for visualizing
    percentages = np.array(matrix)
    rounded_percentages = np.round_(percentages, decimals=2)

    # Visualization
    fig, ax = plt.subplots(figsize=(15, 15))
    masked_array = np.ma.masked_where(rounded_percentages == 0, rounded_percentages)
    cmap = matplotlib.cm.Reds
    cmap.set_bad(color='white')
    im = ax.imshow(masked_array, cmap=cmap, vmin=0, vmax=1)

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(actions)), labels=actions, fontsize=16)
    ax.set_yticks(np.arange(len(actions)), labels=actions, fontsize=16)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(actions)):
        for j in range(len(actions)):
            text = ax.text(j, i, rounded_percentages[i, j],
                           ha="center", va="center", color="white" if percentages[i, j] < 0.005 or percentages[i, j] > 0.5 else "black", fontsize=14)

    ax.set_title("Markov chain")
    fig.tight_layout()
    cbar = fig.colorbar(im,fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=14)
    #plt.show()
    if save_fig:
        plt.savefig(save_fig, bbox_inches='tight')
    #plt.savefig("rezultati/markov_matrix.png", bbox_inches='tight')

def markovv_abs(save_fig=""):
    # Absolute graph
    # Read the .csv
    df = pd.read_csv('action_counting/Rezzy.csv')

    # Variables
    start = 0
    end = 11
    i = 1
    matrix = []  # for values
    actions = ["Creating-Part", "Creating-Assembly", "Editing-Part", "Editing-Assembly",
               "Editing-Non-geometry", "Deleting-Part", "Deleting-Assembly", "Reversing", "Organizing-Design",
               "Organizing-Support design process", "Viewing"]
    action_sum = 11  # number of actions

    # Iterate through .csv
    while i <= action_sum:
        df1 = df.iloc[start:end, 2].tolist()  # store .csv values in fourth column (percentages for analysis) to list
        matrix.append(df1)  # append a list to matrix in each iteration
        start = end
        end += action_sum
        i += 1
    # Prepare matrix for visualizing
    sums = np.array(matrix, dtype=int)

    # Visualization
    fig, ax = plt.subplots(figsize=(15, 15))
    masked_array = np.ma.masked_where(sums == 0, sums)
    cmap = matplotlib.cm.Reds
    cmap.set_bad(color='white')
    im = ax.imshow(masked_array, cmap=cmap)

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(actions)), labels=actions, fontsize=16)
    ax.set_yticks(np.arange(len(actions)), labels=actions, fontsize=16)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    thresh = sums.max() / 2
    for i in range(len(actions)):
        for j in range(len(actions)):
            text = ax.text(j, i, sums[i, j],
                           ha="center", va="center", color="white" if sums[i, j] == 0 or sums[i, j] > thresh else "black", fontsize=14)

    ax.set_title("Markov chain")
    fig.tight_layout()
    cbar = fig.colorbar(im, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=14)
    # plt.show()
    if save_fig:
        plt.savefig(save_fig, bbox_inches='tight')
    # plt.savefig("rezultati/markov_matrix.png", bbox_inches='tight')