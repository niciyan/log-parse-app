import apache_log_parser
import pandas as pd

combined_format = '%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"'

parser = apache_log_parser.make_parser(combined_format)
data = []

with open("access.log") as f:
    for line in f: 
        ans = parser(line)
        # print(ans["request_url"])
        data.append(ans)

df = pd.DataFrame.from_dict(data)
# df.describe()
# print(df)
df.info(verbose=True)

print("{} data detected.".format(len(data)))
print("done")
