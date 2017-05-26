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

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births/births.sum();
    return group;
    # print group;



column_names = ['names', 'sex', 'births']

# name_infos_2016 = pd.read_csv(path, names=column_names);

# print name_infos_2016[:10];

# male_female_totals = name_infos_2016.groupby('sex')['births'].sum();

# print male_female_totals[:50]

df = appendCsvFiles(path, column_names);

pivot_table = pd.pivot_table(df, columns=["sex", "names"], index=["year"], aggfunc="sum", values="births").fillna(value=0);
# pivot_table = df.pivot_table('births', columns="sex", aggfunc="sum", )

print pivot_table[:20];
# print df


# print df.groupby([ 'year','sex']).describe();
# result = df.groupby([ 'year','sex']).apply(add_prop);
# print result

# top_10 = result.sort_values(by='prop', ascending=False);

# pivot_table_sexes = pd.pivot_table(top_10, columns=['sex'], index=['names'], values='prop');
# print pivot_table_sexes;

#finding the index to filter
# womens_indexes = result.index[result['sex'] == 'F'];

# women_table = result.loc[womens_indexes];

#top 10 
# print women_table.sort_values(by='prop', ascending=False)[:10];

# Taking the cuilative sum so that you can see where the sum leads to 50%
# props_cumsum = result.sort_values(by='prop', ascending=False).reset_index(drop=True).prop.cumsum();
# fifty_percent_index = props_cumsum.searchsorted(props_cumsum.quantile(0.5));


# print fifty_percent_index
# print props_cumsum[fifty_percent_index + 1];
