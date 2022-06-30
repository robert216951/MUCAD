import pandas as pd
import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
from matplotlib import ticker as mtick


def markov():
    data = pd.read_csv('action_counting/results.csv')

    df = pd.DataFrame(data)

    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    fig_size = (16, 8)

    # Plot the data using bar() method
    fig, ax = plt.subplots(figsize=fig_size)
    ax.bar(X, Y, color=np.random.rand(len(X), 3), width=0.75)
    plt.title("Markov chain")
    plt.xlabel("'X' aktivnost na 'Y' aktivnost")
    plt.xticks(rotation=90, fontsize=8)
    plt.ylabel("Broj ponavljanja")
    plt.tight_layout()
    plt.savefig("rezultati/markov.png", bbox_inches='tight', figsize=fig_size)

def action_plot_total(df: pd.DataFrame, save_fig="") -> None:
    category_names = ["Creating-Part", "Creating-Assembly", "Editing-Part", "Editing-Assembly",
              "Editing-Non-geometry", "Deleting-Part", "Deleting-Assembly", "Reversing", "Organizing-Design",
              "Organizing-Support design process", "Viewing"]
    fig_size = (2, 8)
    data = df[category_names].to_numpy(dtype=float)
    user_labels = df['File Name'].to_numpy(dtype=str)
    data_labels = df[category_names].to_numpy(dtype=int)
    data_labels = np.where(data_labels <= 0, ' ', data_labels)

    for i in range(len(data)):
        temp_sum = sum(data[i])
        if temp_sum == 0:
            for j in range(11):
                data[i][j] = temp_sum
        else:
            for j in range(11):
                data[i][j] /= temp_sum

    fig, ax = plt.subplots(figsize=fig_size)
    category_colors = plt.get_cmap('cubehelix')(np.linspace(0.15, 0.85, data.shape[1]))  # Set colour

    # ax.invert_xaxis()
    # ax.set_ylim(0, 1)
    ax.set_xlabel("Total", fontsize=16)  # label na x osi
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    # print(data)
    data_cum = data.cumsum(axis=1)
    # print(data_cum)
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.bar(user_labels, widths, bottom=starts, width=0.5, label=colname, color=color, edgecolor='black',
                       linewidth=1.25)
        # ax.bar_label(rects, labels=data_labels[:, i], label_type='center', color="black")

    # ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', mode='expand')
    # ax.yaxis.set_major_formatter(ticker.PercentFormatter(ymax=1))
    ax.set_xticks([])
    plt.yticks(fontsize=16)
    plt.tight_layout()
    # if save_fig:
    # plt.savefig(save_fig,bbox_inches='tight')
    if save_fig:
        plt.savefig(save_fig, bbox_inches='tight')
    #plt.savefig("rezultati/action_type_plot_total.png", bbox_inches='tight')
    # plt.show()


def action_plot_single(save_fig="") -> None:
    count = 1
    df = pd.read_csv('sample_outputs_index/Graph/graf.csv')
    max_value = df['Total'].max()
    upper_limit = max_value + 50
    while count <= 3:
        df = pd.read_csv("sample_outputs_index/Graph/graf_user{}.csv".format(count))
        category_names = ["Creating-Part", "Creating-Assembly", "Editing-Part", "Editing-Assembly",
              "Editing-Non-geometry", "Deleting-Part", "Deleting-Assembly", "Reversing", "Organizing-Design",
              "Organizing-Support design process", "Viewing"]
        fig_size = (15, 16)
        data = df[category_names].to_numpy(dtype=float)
        user_labels = (df['User_name_index']).to_numpy(dtype=str)
        data_labels = df[category_names].to_numpy(dtype=int)
        data_labels = np.where(data_labels <= 0, ' ', data_labels)
        xlabel = df['anon'][1]
        """
        for i in range(len(data)):
            temp_sum = sum(data[i])
            if temp_sum == 0:
                for j in range(7):
                    data[i][j] = temp_sum
            else:
                for j in range(7):
                    data[i][j] /= temp_sum
        """
        fig, ax = plt.subplots(figsize=fig_size)
        category_colors = plt.get_cmap('cubehelix')(np.linspace(0.15, 0.85, data.shape[1]))  # Set colour

        # ax.invert_xaxis()
        ax.set_ylim(0, upper_limit)
        # ax.yaxis.set_major_formatter(mtick.PercentFormatter())
        # ax.set_xlabel("TM{}".format(count), fontsize=36)  # label na x osi
        ax.set_xlabel(xlabel, fontsize=36)  # label na x osi
        # print(data)
        data_cum = data.cumsum(axis=1)
        # print(data_cum)
        for i, (colname, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            rects = ax.bar(user_labels, widths, bottom=starts, width=0.4, label=colname, color=color, edgecolor='black',
                           linewidth=1)
            # ax.bar_label(rects, labels=data_labels[:, i], label_type='center', color="black")

        # ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1.02, 1, 0.2),fontsize=4, loc='lower left', mode='expand')
        ax.set_xticks([])
        plt.yticks(fontsize=36)
        # ax.yaxis.set_major_formatter(ticker.PercentFormatter(ymax=1))

        plt.tight_layout()
        # if save_fig:
        # plt.savefig(save_fig,bbox_inches='tight')
        if save_fig:
            plt.savefig(save_fig + "action_type_plotTM{}.png".format(count), bbox_inches='tight')
        #plt.savefig("rezultati/action_type_plotTM{}.png".format(count), bbox_inches='tight')
        # plt.show()
        count += 1

def action_plot_team(save_fig="") -> None:
    df = pd.read_csv("sample_outputs_index_teams/Graph/graf.csv")
    category_names = ["Creating-Part", "Creating-Assembly", "Editing-Part", "Editing-Assembly",
              "Editing-Non-geometry", "Deleting-Part", "Deleting-Assembly", "Reversing", "Organizing-Design",
              "Organizing-Support design process", "Viewing"]
    fig_size = (14, 8)
    data = df[category_names].to_numpy(dtype=float)
    user_labels = df['index'].to_numpy(dtype=str)
    data_labels = df[category_names].to_numpy(dtype=int)
    data_labels = np.where(data_labels <= 0, ' ', data_labels)

    for i in range(len(data)):
        temp_sum = sum(data[i])
        if temp_sum == 0:
            for j in range(11):
                data[i][j] = temp_sum
        else:
            for j in range(11):
                data[i][j] /= temp_sum

    fig, ax = plt.subplots(figsize=fig_size)
    category_colors = plt.get_cmap('cubehelix')(np.linspace(0.15, 0.85, data.shape[1]))  # Set colour

    # ax.invert_xaxis()
    # ax.set_ylim(0, 1)
    # ax.set_xlabel("Users")  # label na x osi
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    # print(data)
    data_cum = data.cumsum(axis=1)
    # print(data_cum)
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.bar(user_labels, widths, bottom=starts, label=colname, width=0.4, color=color, edgecolor='black',
                       linewidth=1.25)
        # ax.bar_label(rects, labels=data_labels[:, i], label_type='center', color="black")

    ax.legend(ncol=6, bbox_to_anchor=(0, 1.02, 1, 0.2), loc='lower left', mode='expand', fontsize=11.5)
    # ax.yaxis.set_major_formatter(ticker.PercentFormatter(ymax=1))
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)
    plt.tight_layout()
    # if save_fig:
    # plt.savefig(save_fig,bbox_inches='tight')
    if save_fig:
        plt.savefig(save_fig, bbox_inches='tight')
    # plt.show()