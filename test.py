import json
from collections import defaultdict

path = 'D:\python\pydata-book\ch02\usagov_bitly_data2012-03-16-1331923249.txt';

records = [json.loads(line) for line in open(path)];
timeZones = [rec['tz']for rec in records if 'tz' in rec];



def getCounts(seq):
    count = defaultdict(int);
    for x in seq :
        count[x] += 1;

    return count;

counts = getCounts(timeZones[:10]);

print counts['America/New_York'];