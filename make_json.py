import csv  # noqa
import json

with open('itoth.txt', 'r') as f:
    r = csv.reader(f, delimiter='|')
    rows = [row for row in r]
rows = [(row[0], row[4], row[5], row[13], row[14], row[15]) for row in rows]
with open('transfers.json', 'w') as f:
    json.dump(rows, f)

with open('cm.txt', 'r') as f:
    r = csv.reader(f, delimiter='|')
    rows = [row for row in r]
with open('committees.json', 'w') as f:
    json.dump({c[0]: c[1:] for c in rows}, f)

with open('cn.txt', 'r') as f:
    r = csv.reader(f, delimiter='|')
    rows = [row for row in r]
with open('candidates.json', 'w') as f:
    json.dump({c[0]: c[1:] for c in rows}, f)
