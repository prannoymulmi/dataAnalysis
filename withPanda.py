from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt
import json

path = 'D:\python\pydata-book\ch02\usagov_bitly_data2012-03-16-1331923249.txt';

records = [json.loads(line) for line in open(path)];
timeZones = [rec['tz']for rec in records if 'tz' in rec];

frame = DataFrame(records);


clean_tz = frame['tz'].fillna('Missing');
clean_tz [clean_tz == ''] = 'Empty';
counts = clean_tz.value_counts();
#print frame['tz']
print counts[:10];

plt.plot(counts[:10])
