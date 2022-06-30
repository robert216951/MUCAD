import os
import pandas as pd
import math
import csv

from action_counting import aggregate_count
from action_count_plotting import plotting
import graphing

# directories
directory_multi = "sample_audit_trails/multi_user/"
directory_multi_stud = "sample_audit_trails/multi_user_stud/"
directory_multi_1 = "sample_audit_trails/multi1/"
directory_single_1 = "sample_audit_trails/single1/"

# Store the counts computed for each audit trail file
counts = {}
categories = ["File Name", "Creating", "Editing", "Deleting", "Reversing", "Viewing", "Organizing", "Other", "Total"]

# pocetni .csv za analizu se ubacuje u directory 'multi_user'
# sljedeci dio koda filitrira pocetni .csv
for filename in os.scandir(directory_multi):    # petlja za citanje filea neovisno o nazivu filea
    if filename.is_file():
        df = pd.read_csv(filename.path)
        df = df.loc[(df['User Data User Name Photo'].str.contains('@stud.fsb.hr')) & (
            ~df['Document Data Document'].str.contains('crtez|drawing')) & (
            ~df['v_audit_trail Event Description'].str.contains('Drawing|drawing|BOM')) & (
             df['v_audit_trail Event Time'] < '2021-02-11') & (
            ~df['v_audit_trail Tab'].str.contains('Drawing|BOM', na=False)) & (
             df['v_audit_trail Event Description'].str.contains(
                'Add part studio feature|Add assembly feature|Add assembly instance|Copy paste sketch|Paste :|Linked document insert|Start edit of part studio feature|Start edit of assembly feature|Set mate values|Fix :|Unfix :|Replace :|Suppress :|Unsuppress :|Select context|Update context|Change configuration|Configure suppression state|Delete part studio feature|Delete assembly feature|Delete assembly instance|Cancel Operation|Undo Redo Operation|Reset mates to initial positions|Animate action called|Start assembly drag|Move to origin|Move :|Hide :|Show :|created|renamed|deleted|opened|moved|Rename part :|Rename document :| Restructure :|Create new folder :|Update document description|Change Description :|Change Vendor :|Copy workspace|Move document|Create version|Assign material :|updated|Change properties|Change part appearance :|Comment on a Document|Use automatic tessellation setting :|Use best available tessellation :|Restore Document From History'))]
        df1 = df.iloc[::-1]     # reverse order by timestamp - najraniji datum pocetni
        df1.to_csv(directory_multi_stud + 'multi_stud.csv', index=False)

# VRATI SE NA OVO
f = open('sample_outputs_index/Graph/graf.csv', 'r+')
f.truncate(0)
graf = pd.read_csv("sample_audit_trails/x/graf_index.csv")
graf = graf.iloc[:0]
graf.to_csv("sample_outputs_index/Graph/graf.csv",index=False)

# deletanje zaostalih fileova od prethodne analize
for filename in os.scandir(directory_single_1):
    if filename.is_file():
        os.remove(filename)

df = pd.read_csv(directory_multi_stud + 'multi_stud.csv')
x = 10  # broj dijelova na koje dijelim file
podjela = math.ceil(len(df.index) / x)
prvi = 0
drugi = podjela
count = 1

while count <= x:
    # razdvaja .csv na dijelove
    df = pd.read_csv(directory_multi_stud + "multi_stud.csv")
    df = df.iloc[prvi:drugi]
    df.to_csv(directory_multi_1 + 'dio.csv', index=False)
    df.to_csv("sample_outputs_index/sample_outputs{}/dio.csv".format(count), index=False)

    # grupira .csv dijelovi na pojedinacne korisnike
    for filename in os.scandir(directory_multi_1):
        if filename.is_file():
            df = pd.read_csv(filename.path)
            df = df.sort_values('User Data User Name Photo')
            for i, g in df.groupby('User Data User Name Photo'):
                g.to_csv(directory_single_1 + '{}.csv'.format(i), index=False)

    # poziva subprogram za brojanje aktivnosti
    for _, _, files in os.walk(directory_single_1):
        for File in files:
            if File.endswith(".csv"):
                with open(directory_single_1 + File, 'r') as audit_trail_csv:
                    reader = csv.reader(audit_trail_csv)
                    counts = {**counts, **aggregate_count.aggregate_count(reader, File[:-4])}

    # Record counts in a new csv file
    with open("sample_outputs_index/sample_outputs{}/Counts.csv".format(count), 'w') as record_csv:
        writer = csv.writer(record_csv)
        writer.writerow(categories)
        for name, count_list in counts.items():
            temp = [name]
            temp.extend(count_list[0])
            writer.writerow(temp)

    count_data = pd.read_csv("sample_outputs_index/sample_outputs{}/Counts.csv".format(count))
    count_data["anon"] = ["TM1", "TM2", "TM3"]

#    plotting.action_type_percentage(count_data, save_fig="sample_outputs_index/sample_outputs{}/action_type_plot".format(count))
#    plotting.cr_ratio(count_data, save_fig="sample_outputs_index/sample_outputs{}/CR_ratio_plot".format(count))


    # Analyze the specified CSV file
    for filename in os.scandir(directory_multi_1):
        with open(filename.path) as audit_trail_csv:
            print(audit_trail_csv)
            reader = csv.reader(audit_trail_csv)
            contri_counts = aggregate_count.aggregate_count(reader, filename.path.split("/")[-1])

    # Record counts in a new csv file
    with open("sample_outputs_index/sample_outputs{}/Counts.csv".format(count), 'w') as record_csv:
        writer = csv.writer(record_csv)
        writer.writerow(categories)
        for name, count_list in counts.items():
            temp = [name]
            temp.extend(count_list[0])
            temp.append(sum(count_list[0]))
            writer.writerow(temp)

    count_data = pd.read_csv("sample_outputs_index/sample_outputs{}/Counts.csv".format(count))
    count_data["anon"] = ["TM1", "TM2", "TM3"]

#    plotting.plot_contribution(count_data, "Total", save_fig="sample_outputs_index/sample_outputs{}/contribution_per_plot".format(count))

    za_graf = pd.read_csv("sample_outputs_index/sample_outputs{}/Counts.csv".format(count))
    file_total = za_graf['Total'].sum()  # sumira brojeve u column "total" - daje CJELOKUPAN broj aktivnosti
    za_graf["contri"] = (za_graf['Total'] / file_total) * 100
    za_graf["cr"] = za_graf["Creating"] / (za_graf["Editing"] + za_graf["Deleting"] + za_graf["Reversing"])
    za_graf["index"] = [str(count) + ". cluster", str(count) + ". cluster", str(count) + ". cluster"]
    za_graf["anon"] = ["TM1", "TM2", "TM3"]
    za_graf.to_csv("sample_outputs_index/Graph/graf.csv", mode='a', header=False, index=False)

    prvi = prvi + podjela
    drugi = drugi + podjela
    count += 1

df = pd.read_csv("sample_outputs_index/Graph/graf.csv")
df.insert(1, 'User_name_index', '-')
df.User_name_index = df['anon'] + ' ' + df['index']
df.to_csv("sample_outputs_index/Graph/graf.csv")
graphing.cr_plot(df)
graphing.time_plot(df)
graphing.action_type_percentage(df, save_fig="sample_outputs_index/Graph/action_type_plot.png")

df.iloc[0::3, :].to_csv("sample_outputs_index/Graph/graf_user1.csv", index=False)
df.iloc[1::3, :].to_csv("sample_outputs_index/Graph/graf_user2.csv", index=False)
df.iloc[2::3, :].to_csv("sample_outputs_index/Graph/graf_user3.csv", index=False)
df = pd.read_csv("sample_outputs_index/Graph/graf_user1.csv")
graphing.action_type_percentage(df, save_fig="sample_outputs_index/Graph/action_type_plot_user1.png")
df = pd.read_csv("sample_outputs_index/Graph/graf_user2.csv")
graphing.action_type_percentage(df, save_fig="sample_outputs_index/Graph/action_type_plot_user2.png")
df = pd.read_csv("sample_outputs_index/Graph/graf_user3.csv")
graphing.action_type_percentage(df, save_fig="sample_outputs_index/Graph/action_type_plot_user3.png")