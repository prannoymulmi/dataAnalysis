from pandas import DataFrame, Series
import numpy as np
from pylab import *
import json


path = 'D:\python\pydata-book\ch02\usagov_bitly_data2012-03-16-1331923249.txt';

records = [json.loads(line) for line in open(path)];
timeZones = [rec['tz']for rec in records if 'tz' in rec];
frame = DataFrame(records);

clean_frame = frame[frame.a.notnull()];
os = np.where(clean_frame['a'].str.contains('Windows'), 'Windows', 'others');

sort_by_tz_and_os = clean_frame.groupby(['tz', os]);
agg_counts = sort_by_tz_and_os.size().unstack().fillna(0);

ascending_sort = agg_counts.sum(1).argsort(); # sorting ins ascending order
print ascending_sort[:10];

count_subset = agg_counts.take(ascending_sort)[:-10];
plot(count_subset)


#print sort_by_tz_and_os.get_group('tz');
