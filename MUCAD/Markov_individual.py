import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

directory_multi = "markov/individual_csv/"
directory_save_pic = "markov/individual_img/"

for filename in os.scandir(directory_multi):    # petlja za citanje filea neovisno o nazivu filea
    if filename.is_file():
        if filename.path.endswith(".csv"):
            naziv = str(filename.name).replace(".csv", "")


            df1 = pd.read_csv('markov/KD.csv')
            df2 = pd.read_csv(filename.path)

            for og in df1['vars'].to_list():
                df2.loc[df2['Description'].str.contains(og), 'Description'] = og

            df2.loc[df2['Description'].str.contains('created|renamed|deleted|moved'), 'Description'] = df2['Description'] + ' tab'
            df2.loc[df2['Description'].str.contains('updated'), 'Description'] = df2['Description'] + ' metadata by user'
            df2.to_csv('markov/k11_test.csv')

            f = open('markov/usporedba.csv', 'r+')
            f.truncate(0)
            graf = pd.read_csv("markov/results.csv")
            graf = graf.iloc[:0]
            graf.to_csv('markov/usporedba.csv',index=False)

            df3 = pd.read_csv('markov/usporedba.csv')
            df = pd.read_csv('markov/k11_test.csv')
            df3['classification'] = df['Description']
            df3['classification2'] = df3['classification'].shift(-1)
            df3.to_csv('markov/usporedba.csv', index=False)

            df = pd.read_csv('markov/usporedba.csv')
            df1 = df.value_counts(["classification", "classification2"]).reset_index()
            df1.columns = ['classification', 'classification2', 'conutz']
            df1.to_csv('markov/results.csv', index=False)
            df1 = pd.read_csv('markov/results.csv')
            df1.sort_values(['classification', 'classification2']).to_csv('markov/results.csv', index=False)

            # percentage graph
            df = pd.read_csv('markov/results.csv')
            df = df.merge(df.groupby('classification')['conutz'].sum().rename('sumz'), on = ['classification'])
            df['percentages'] = (df['conutz']/df['sumz']).round(2)
            df.to_csv('markov/results.csv', index=False)
            corr = df.pivot(index='classification', columns='classification2', values='percentages').fillna(0)
            print(corr)

            actions = df['classification'].unique().tolist()
            print(actions)

            fig, ax = plt.subplots(figsize=(18, 16))
            masked_array = np.ma.masked_where(corr == 0, corr)
            cmap = matplotlib.cm.Reds
            cmap.set_bad(color='white')
            im = ax.imshow(masked_array, cmap=cmap, vmin=0, vmax=1)
            # Show all ticks and label them with the respective list entries
            ax.set_xticks(np.arange(len(actions)), labels=actions, fontsize=10)
            ax.set_yticks(np.arange(len(actions)), labels=actions, fontsize=10)

            # Rotate the tick labels and set their alignment.
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                     rotation_mode="anchor")
            percentages = np.array(corr)
            rounded_percentages = np.round_(percentages, decimals=2)
            # Loop over data dimensions and create text annotations.
            for i in range(len(actions)):
                for j in range(len(actions)):
                    text = ax.text(j, i, rounded_percentages[i, j],
                                   ha="center", va="center",color="white" if rounded_percentages[i, j] == 0 or rounded_percentages[i, j] > 0.5 else "black", fontsize=10)

            ax.set_title("Markov chain")
            #ax.scatter(*np.argwhere(rounded_percentages.T == 0).T, marker="x", color="black", s=100)
            fig.tight_layout()
            cbar = fig.colorbar(im, fraction=0.046, pad=0.04)
            cbar.ax.tick_params(labelsize=14)
            #plt.show()
            #sb.heatmap(corr, cmap="Blues", annot=True)
            plt.savefig("markov/Plotting_Correlation_HeatMap{}.png".format(naziv), bbox_inches='tight')

            # absolute graph
            #df = pd.read_csv('markov/results.csv')
            #df[df.conutz > 100].to_csv('markov/results.csv', index=False)
            df = pd.read_csv('markov/results.csv')
            corr = df.pivot(index='classification', columns='classification2', values='conutz').fillna(0)
            #print(corr)

            actions = df['classification'].unique().tolist()

            fig, ax = plt.subplots(figsize=(18, 16))
            masked_array = np.ma.masked_where(corr == 0, corr)
            cmap = matplotlib.cm.Reds
            cmap.set_bad(color='white')
            im = ax.imshow(masked_array, cmap=cmap)
            # Show all ticks and label them with the respective list entries
            ax.set_xticks(np.arange(len(actions)), labels=actions, fontsize=10)
            ax.set_yticks(np.arange(len(actions)), labels=actions, fontsize=10)

            # Rotate the tick labels and set their alignment.
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                     rotation_mode="anchor")
            percentages = np.array((corr), dtype=int)
            # Loop over data dimensions and create text annotations.
            thresh = percentages.max() / 2
            for i in range(len(actions)):
                for j in range(len(actions)):
                    text = ax.text(j, i, percentages[i, j],
                                   ha="center", va="center", color="white" if percentages[i, j] == 0 or percentages[i, j] > thresh else "black", fontsize=10)

            ax.set_title("Markov chain")
            fig.tight_layout()
            cbar = fig.colorbar(im, fraction=0.046, pad=0.04)
            cbar.ax.tick_params(labelsize=14)
            # plt.show()
            # sb.heatmap(corr, cmap="Blues", annot=True)
            plt.savefig(directory_save_pic + "{}.png".format(naziv), bbox_inches='tight')
