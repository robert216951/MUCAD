import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import ticker as mtick
from matplotlib.ticker import FuncFormatter
"""raspon = ['< 4000', '4000 - 6000', '6000 - 9000', '> 9000']
team_sum = [2, 5, 6, 1]

fig_size = (9, 3)
plt.subplots(figsize=fig_size)
#New_Colors = ['lightsteelblue','teal','maroon','mediumseagreen']
plt.bar(raspon, team_sum, width=0.3, color="darkslategray", edgecolor='black', linewidth=2)
plt.xlabel('Raspon CAD aktivnosti')
plt.ylabel('Broj timova')
plt.tight_layout()
plt.show()"""

"""df = pd.DataFrame(dict(raspon = ["Tim #1", "Tim #2", "Tim #3", "Tim #4", "Tim #5", "Tim #6", "Tim #7", "Tim #8", "Tim #9", "Tim #10", "Tim #11", "Tim #12", "Tim #13", "Tim #14"], team_sum = [14264, 5090, 7363, 2934, 4405, 8601, 6019, 5112, 6886, 8763, 7898, 5812, 3049, 5460]))
df_sorted = df.sort_values("team_sum")
df_1 = df_sorted.loc[(df_sorted['team_sum'].lt(4000))]
df_2 = df_sorted.loc[(df_sorted['team_sum'].lt(6000)) & (df['team_sum'].gt(4000))]
df_3 = df_sorted.loc[(df_sorted['team_sum'].lt(9000)) & (df['team_sum'].gt(6000))]
df_4 = df_sorted.loc[(df_sorted['team_sum'].gt(9000))]


fig_size = (15, 6)
plt.subplots(figsize=fig_size)
#New_Colors = ['lightsteelblue','teal','maroon','mediumseagreen']
plt.axhline(y=4000, color='goldenrod', linestyle='--')
plt.axhline(y=6000, color='goldenrod', linestyle='--')
plt.axhline(y=9000, color='goldenrod', linestyle='--')
plt.bar("raspon", "team_sum", data=df_1, width=0.3, color="firebrick", edgecolor='black', linewidth=1)
plt.bar("raspon", "team_sum", data=df_2, width=0.3, color="lemonchiffon", edgecolor='black', linewidth=1)
plt.bar("raspon", "team_sum", data=df_3, width=0.3, color="mediumseagreen", edgecolor='black', linewidth=1)
plt.bar("raspon", "team_sum", data=df_4, width=0.3, color="darkslategray", edgecolor='black', linewidth=1)
plt.xlabel('Timovi')
plt.ylabel('Broj CAD aktivnosti')
plt.tight_layout()
plt.show()"""


"""df = pd.DataFrame(dict(raspon = ["Tim #1", "Tim #2", "Tim #3", "Tim #4", "Tim #5", "Tim #6", "Tim #7", "Tim #8", "Tim #9", "Tim #10", "Tim #11", "Tim #12", "Tim #13", "Tim #14"], team_sum = [14264, 5090, 7363, 2934, 4405, 8601, 6019, 5112, 6886, 8763, 7898, 5812, 3049, 5460], bodovi=[44,39,41,39,38,42,41,40,43,44,41,40,29,35]))
df_sorted = df.sort_values("team_sum")
df_1 = df_sorted.loc[(df['bodovi'].lt(34))]
df_2 = df_sorted.loc[(df['bodovi'].lt(40.99)) & (df['bodovi'].gt(34))]
df_4 = df_sorted.loc[(df['bodovi'].gt(40.99))]




fig_size = (10, 5)
plt.subplots(figsize=fig_size)
#New_Colors = ['lightsteelblue','teal','maroon','mediumseagreen']
plt.axhline(y=4000, color='goldenrod', linestyle='--')
plt.axhline(y=6000, color='goldenrod', linestyle='--')
plt.axhline(y=9000, color='goldenrod', linestyle='--')
plt.bar("raspon", "team_sum", data=df_1, width=0.5, color="firebrick", edgecolor='black', linewidth=1, label="29")
plt.bar("raspon", "team_sum", data=df_2, width=0.5, color="lemonchiffon", edgecolor='black', linewidth=1, label="35 - 40")
plt.bar("raspon", "team_sum", data=df_4, width=0.5, color="darkslategray", edgecolor='black', linewidth=1, label="41 - 44")
plt.xlabel('Timovi', fontsize=14)
plt.ylabel('Broj CAD aktivnosti', fontsize=14)
plt.yticks(fontsize=14)
plt.legend(title="Broj bodova:", fontsize=10)
plt.tight_layout()
plt.show()"""


"""df = pd.DataFrame(dict(raspon = ["Tim #1", "Tim #2", "Tim #3", "Tim #4", "Tim #5", "Tim #6", "Tim #7", "Tim #8", "Tim #9", "Tim #10", "Tim #11", "Tim #12", "Tim #13", "Tim #14"], team_sum = [2.96, 2.32, 3.53, 1.88, 4.41, 5.99, 2.59, 3.93, 3.42, 3.61, 2.59, 2.80, 2.98, 3.16]))
#df_sorted = df.sort_values("team_sum")
df_1 = df_sorted.loc[(df['bodovi'].lt(34))]
df_2 = df_sorted.loc[(df['bodovi'].lt(40.99)) & (df['bodovi'].gt(34))]
df_4 = df_sorted.loc[(df['bodovi'].gt(40.99))]




fig_size = (10, 5)
plt.subplots(figsize=fig_size)
#New_Colors = ['lightsteelblue','teal','maroon','mediumseagreen']
plt.axhline(y=4000, color='goldenrod', linestyle='--')
plt.axhline(y=6000, color='goldenrod', linestyle='--')
plt.axhline(y=3.3, color='goldenrod', linestyle='--')
plt.bar("raspon", "team_sum", data=df, width=0.4, color="teal", edgecolor='black', linewidth=1)
#plt.bar("raspon", "team_sum", data=df_2, width=0.5, color="lemonchiffon", edgecolor='black', linewidth=1, label="35 - 40")
#plt.bar("raspon", "team_sum", data=df_4, width=0.5, color="darkslategray", edgecolor='black', linewidth=1, label="41 - 44")
plt.xlabel('Timovi', fontsize=14)
plt.ylabel('Omjer modificiranja i brisanja geometrijskih značajki', fontsize=12)
plt.yticks(fontsize=14)
#plt.legend(title="Broj bodova:", fontsize=10)
plt.tight_layout()
plt.show()"""


"""fig_size = (12, 6)
labels = ["Tim #1", "Tim #2", "Tim #3", "Tim #4", "Tim #5", "Tim #6", "Tim #7", "Tim #8", "Tim #9", "Tim #10", "Tim #11", "Tim #12", "Tim #13", "Tim #14"]
part = [0.38,0.33,0.35,0.36,0.44,0.32,0.37,0.38,0.47,0.44,0.45,0.37,0.46,0.46]
assembly = [0.20,0.33,0.22,0.35,0.17,0.28,0.32,0.26,0.19,0.23,0.20,0.28,0.23,0.20]

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots(figsize=fig_size)
rects1 = ax.bar(x - width/2, part, width, label='Part', color="steelblue", edgecolor='black', linewidth=1)
rects2 = ax.bar(x + width/2, assembly, width, label='Assembly', color="gold", edgecolor='black', linewidth=1)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Udio Part i Assembly CAD aktivnosti', fontsize=14)
ax.set_xlabel('Timovi', fontsize=14)
ax.set_xticks(x, labels)
ax.legend()
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
plt.yticks(fontsize=16)
plt.xticks(fontsize=11)


plt.savefig("partvsassem.jpg",dpi=600)
plt.show()"""



"""x = [15.24, 13.89,21.03,5.66,1.04,3.56,5.04,17.04,5.23,4.83,7.43]
category_names = ["Creating-Part", "Creating-Assembly", "Editing-Part", "Editing-Assembly",
              "Editing-Non-geometry", "Deleting-Part", "Deleting-Assembly", "Reversing", "Organizing-Design",
              "Organizing-Support design process", "Viewing"]
fig1, ax1 = plt.subplots(figsize=(10, 10))
fig1.subplots_adjust(0.3, 0, 1, 1)

theme = plt.get_cmap('cubehelix')(np.linspace(0.15, 0.85, num=11))
ax1.set_prop_cycle(color=theme)

wedges, texts = ax1.pie(x, startangle=90, radius=1800)
for w in wedges:
    w.set_edgecolor('black')

ax1.axis('equal')

total = sum(x)
plt.legend(
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100)
            for l, s in zip(category_names, x)],
    prop={'size': 11},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure
)

plt.show()"""




"""bottom = [0.09,0.09,0.17,0.02,0.00,0.02,0.03,0.10,0.00,0.02,0.01]
delta = [0.12,0.13,0.08,0.12,0.02,0.03,0.05,0.13,0.19,0.05,0.18]
category_names = ["Creating-Part", "Creating-Assembly", "Editing-Part", "Editing-Assembly",
              "Editing-Non-geometry", "Deleting-Part", "Deleting-Assembly", "Reversing", "Organizing-Design",
              "Organizing-Support design process", "Viewing"]
fig1, ax1 = plt.subplots(figsize=(12, 6))
#fig1.subplots_adjust(0.3, 0, 1, 1)

theme = plt.get_cmap('cubehelix')(np.linspace(0.15, 0.85, num=11))
#ax1.set_prop_cycle(color=theme)
plt.setp(ax1.get_xticklabels(), rotation=30, ha="right",
                     rotation_mode="anchor")

ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
plt.yticks(fontsize=15)
plt.xticks(fontsize=12)

plt.bar(category_names, width=0.6, height=delta, bottom=bottom, color=theme, edgecolor='black', linewidth=1)
plt.tight_layout()
plt.show()"""


"""fig_size = (12, 6)
labels = ["Creating-Part", "Creating-Assembly", "Editing-Part", "Editing-Assembly",
              "Editing-Non-geometry", "Deleting-Part", "Deleting-Assembly", "Reversing", "Organizing-Design",
              "Organizing-Support design process", "Viewing"]
best = [0.19, 0.09, 0.22, 0.07, 0.01, 0.04, 0.04, 0.18, 0.04, 0.05, 0.10]
worst = [0.24, 0.08, 0.29, 0.00, 0.00, 0.05, 0.02, 0.15, 0.02, 0.09, 0.05]

#best = [0.16, 0.08, 0.21, 0.10, 0.01, 0.05, 0.03, 0.15, 0.11, 0.03, 0.07]
#worst = [0.19, 0.20, 0.21, 0.03, 0.00, 0.05, 0.05, 0.16, 0.05, 0.04, 0.04]

#best = [0.11, 0.10, 0.20, 0.14, 0.01, 0.04, 0.05, 0.17, 0.10, 0.02, 0.06]
#worst = [0.15, 0.16, 0.19, 0.07, 0.00, 0.04, 0.05, 0.17, 0.04, 0.06, 0.07]

#best = [0.11, 0.12, 0.18, 0.10, 0.04, 0.02, 0.04, 0.15, 0.08, 0.02, 0.13]
#worst = [0.11, 0.22, 0.14, 0.05, 0.02, 0.02, 0.07, 0.16, 0.05, 0.04, 0.11]

x = np.arange(len(labels))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots(figsize=fig_size)
plt.scatter(labels, best, label = "Tri najbolja tima", color="mediumseagreen", marker='s', s=55)
plt.scatter(labels, worst, label = "Tri najlošija tima", color="firebrick", marker='o', s=50)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Prosječne vrijednosti\nudjela CAD kategorija\n ', fontsize=14)
ax.set_xlabel('Kategorije CAD aktivnosti', fontsize=14)
ax.set_xticks(x, labels)
ax.legend()
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
plt.yticks(fontsize=16)
plt.xticks(fontsize=11)
plt.setp(ax.get_xticklabels(), rotation=30, ha="right",
                     rotation_mode="anchor")

plt.tight_layout()
plt.savefig("q1_dot.jpg",dpi=600)
#plt.show()"""

"""fig_size = (10, 8)
df = pd.read_csv("sample_outputs_index/total_user/Book2.csv")
df1 = df.loc[df['# aktivnosti'] == "max"]
df2 = df.loc[df['# aktivnosti'] == "avg"]
df3 = df.loc[df['# aktivnosti'] == "min"]

#ax = df.plot.scatter(x="Hours", y="Totall", c="Colorr", s=25)
fig, ax = plt.subplots(figsize=fig_size)
ax = sns.regplot(ax=ax, x="Sati rada", y="Ukupan broj CAD aktivnosti", data=df1, ci=None, scatter=False, label="", color="mediumseagreen")
ax = sns.regplot(ax=ax, x="Sati rada", y="Ukupan broj CAD aktivnosti", data=df2, ci=None, scatter=False, label="avg", color="gold")
ax = sns.regplot(ax=ax, x="Sati rada", y="Ukupan broj CAD aktivnosti", data=df3, ci=None, scatter=False, label="min", color="maroon")
sns.scatterplot(ax=ax, data=df, x="Sati rada", y="Ukupan broj CAD aktivnosti", hue="Timovi", style = "# aktivnosti", palette="tab20_r", s=150)

#sns.lmplot(data=df, x="Sati rada", y="Ukupan broj CAD aktivnosti", hue="# aktivnosti", scatter=False)

ax.legend(title="Linije regresije",loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()"""

df = pd.read_csv("boxpl.xlsx")
sns.set_style("whitegrid")

sns.boxplot(x='Q', y='Creating-Part', data=df)
plt.show()