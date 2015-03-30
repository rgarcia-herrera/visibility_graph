from itertools import combinations
import fileinput

# convert list of magnitudes into list of tuples that hold the index
series = []
n = 0
for line in fileinput.input():
    series.append( (n, float(line.strip()) ) )
    n += 1

# contiguous time points always have visibility
for n in range(0,len(series)-1):
    (ta, ya) = series[n]
    (tb, yb) = series[n+1]
    print "connect ", ta,tb

for a,b in combinations(series, 2):
    # two points, maybe connect
    (ta, ya) = a
    (tb, yb) = b

    # let's see all other points in the series
    for tc, yc in series:
        # other points, not a or b
        if tc != ta and tc != tb:
            # does c not obstruct?
            if yc < yb + (ya - yb) * ( (tb - tc) / (tb - ta) ):
                print "connect ", ta,tb




