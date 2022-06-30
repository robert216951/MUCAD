import pandas as pd
import os

directory_multi = "sample_audit_trails/multi_user/"
directory_multi_stud = "sample_audit_trails/rename_tab/"
actions = 'Add part studio feature|Add assembly feature|Add assembly instance|Copy paste sketch|Paste :|Linked document insert|Start edit of part studio feature|Start edit of assembly feature|Set mate values|Fix :|Unfix :|Replace :|Suppress :|Unsuppress :|Select context|Update context|Change configuration|Configure suppression state|Delete part studio feature|Delete assembly feature|Delete assembly instance|Cancel Operation|Reset mates to initial positions|Animate action called|Move to origin|Move :|Hide :|Show :|created|renamed|deleted|moved|Rename part :|Rename document :| Restructure :|Create new folder :|Update document description|Change Description :|Change Vendor :|Copy workspace|Move document|Create version|Assign material :|updated|Change properties|Change part appearance :|Comment on a Document|Use automatic tessellation setting :|Use best available tessellation :|Restore Document From History|Load named position|Edit configuration table|Rename tab :'

for filename in os.scandir(directory_multi):    # petlja za citanje filea neovisno o nazivu filea
    if filename.is_file():
        if filename.path.endswith(".csv"):
            print(filename.path)
            df = pd.read_csv(filename.path)
            df['Time'] = pd.to_datetime(df['Time'])
            df = df.loc[(df['User'].str.contains('@stud.fsb.hr')) & (
                ~df['Document'].str.contains('crtez|drawing')) & (
                ~df['Description'].str.contains('Drawing|drawing|BOM')) & (df["Time"] < '2021-12-13 08:00:00') & (
                ~df['Tab'].str.contains('Drawing|BOM', na=False)) & (
                 df['Description'].str.contains(actions))]
            df1 = df.iloc[::-1]     # reverse order by timestamp - najraniji datum pocetni
            df1.drop(df1.columns[0], axis=1, inplace=True)
            df1.to_csv(directory_multi_stud + '{}'.format(filename.name), index=False)

name = "Audit Trail 4A.csv"
df = pd.read_csv(directory_multi + name)
df['Time'] = pd.to_datetime(df['Time'])
df = df.loc[(df['User'].str.contains('@stud.fsb.hr')) & (
    ~df['Document'].str.contains('crtez|drawing')) & (
    ~df['Description'].str.contains('Drawing|drawing|BOM')) & (df["Time"] < '2021-12-13 09:10:00') & (
    ~df['Tab'].str.contains('Drawing|BOM', na=False)) & (
     df['Description'].str.contains(actions))]
df1 = df.iloc[::-1]     # reverse order by timestamp - najraniji datum pocetni
df1.drop(df1.columns[0], axis=1, inplace=True)
df1.to_csv(directory_multi_stud + name, index=False)

name = "Audit Trail 7D.csv"
df = pd.read_csv(directory_multi + name)
df['Time'] = pd.to_datetime(df['Time'])
df = df.loc[(df['User'].str.contains('@stud.fsb.hr')) & (
    ~df['Document'].str.contains('crtez|drawing')) & (
    ~df['Description'].str.contains('Drawing|drawing|BOM')) & (df["Time"] < '2021-12-13 08:40:00') & (
    ~df['Tab'].str.contains('Drawing|BOM', na=False)) & (
     df['Description'].str.contains(actions))]
df1 = df.iloc[::-1]     # reverse order by timestamp - najraniji datum pocetni
df1.drop(df1.columns[0], axis=1, inplace=True)
df1.to_csv(directory_multi_stud + name, index=False)

name = "Audit Trail 7B.csv"
df = pd.read_csv(directory_multi + name)
df['Time'] = pd.to_datetime(df['Time'])
df = df.loc[(df['User'].str.contains('@stud.fsb.hr')) & (
    ~df['Document'].str.contains('crtez|drawing')) & (
    ~df['Description'].str.contains('Drawing|drawing|BOM')) & (df["Time"] < '2021-12-13 18:05:00') & (
    ~df['Tab'].str.contains('Drawing|BOM', na=False)) & (
     df['Description'].str.contains(actions))]
df1 = df.iloc[::-1]     # reverse order by timestamp - najraniji datum pocetni
df1.drop(df1.columns[0], axis=1, inplace=True)
df1.to_csv(directory_multi_stud + name, index=False)

name = "Audit Trail 7A.csv"
df = pd.read_csv(directory_multi + name)
df['Time'] = pd.to_datetime(df['Time'])
df = df.loc[(df['User'].str.contains('@stud.fsb.hr')) & (
    ~df['Document'].str.contains('crtez|drawing')) & (
    ~df['Description'].str.contains('Drawing|drawing|BOM')) & (df["Time"] < '2021-12-14 11:20:00') & (
    ~df['Tab'].str.contains('Drawing|BOM', na=False)) & (
     df['Description'].str.contains(actions))]
df1 = df.iloc[::-1]     # reverse order by timestamp - najraniji datum pocetni
df1.drop(df1.columns[0], axis=1, inplace=True)
df1.to_csv(directory_multi_stud + name, index=False)

# Individual obrez
for filename in os.scandir(directory_multi_stud):    # petlja za citanje filea neovisno o nazivu filea
    if filename.is_file():
        if filename.path.endswith(".csv"):
            print(filename.path)
            df = pd.read_csv(filename.path)