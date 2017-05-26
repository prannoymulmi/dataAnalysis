import pandas as pd;
from pandas import DataFrame;
from matplotlib import pyplot as plt;



path = 'D:\python\pydata-book\ch02\US-babies';

def appendCsvFiles(path, column_names) :
    years = range(1888, 2017);
    datas = [];

    for year in years:
        file_name = "\\"
        csv_path ="%s%s%s%d%s" %(path, "\\", "yob", year, '.txt')
        frame = pd.read_csv(csv_path, names=column_names);
        frame['year'] = year;
        datas.append(frame);
    names = pd.concat(datas, ignore_index="true");
    return names;

def add_last_letter(group):
    last_letter = lambda x:  x[-1];
    group['last_letter'] = group.names.map(last_letter);
    return group;

column_names = ['names', 'sex', 'births'];

df = appendCsvFiles(path, column_names);

df_with_last_letter = add_last_letter(df);
# print df


pivot_table = pd.pivot_table(df, columns=["sex","last_letter"], index=["year"], aggfunc="sum", values="births").fillna(value=0);

# print pivot_table;
data_according_to_year = pivot_table.loc[lambda x: x.index == 2010];

#
print data_according_to_year["F"][["a", "b"]];
plt.plot(data_according_to_year["F"])
plt.show();