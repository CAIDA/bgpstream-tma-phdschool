# Exercise 3: Investigate peer routing table sizes

The goal of this exercise is to build a distribution of per-peer routing table
sizes in order to understand the difference between "partial" and "full-feed"
peers. To do this, you should modify the script you wrote in Exercise 2 to count
the number of unique prefixes per-peer in a RIB dump, then plot a distribution.

### Steps

1. Modify your [script](https://github.com/CAIDA/bgpstream-tma-phdschool/blob/master/exercise-2-pybgpstream/exercise-2-updates-per-peer.complete.py) to process RIB (`ribs`) data instead of Updates
(`updates`), select only a single collector (use `route-views2` this time), and
select a time interval that includes a RIB dump (`2017-01-15 00:00 -> 01:00`).

1. Modify your statistics collection to count the number of unique prefixes each
peer announces (instead of number of updates).

1. Use the code snippet below to generate a CDF of peer routing table
sizes. You should see a "knee" at the right side of the graph that represents
the full-feed peers. What would be a good threshold for determining if a peer is
full-feed?

To minimize memory usage, you may assume that prefixes are not duplicated for a
given peer and simply count them, rather than building a set of prefixes for
each peer. Additionally, it takes my laptop around 5 minutes to process a RIB
dump from `route-views2`, so _you should add a short-circuit to your code during
testing (e.g., break out of the loop after processing 500k elems)_.


#### CDF Plotting Code

To use this you'll need `matplotlib` and `pandas`.
To install these, run:
```
sudo pip install matplotlib pandas
```

To count the prefixes per-peer, and plot a CDF:
```python
import collections
import matplotlib.pyplot as plt
import pandas
import _pybgpstream

# !!TODO: add bgpstream init and filter code here

# helper function that simplifies extracting elems from a stream
def elem_generator(_stream, limit=None):
    _rec = _pybgpstream.BGPRecord()
    _cnt = 0
    while _stream.get_next_record(_rec):
        while True:
            _elem = _rec.get_next_elem()
            if _elem is None:
                break
            yield (_rec, _elem)
            _cnt += 1
            if limit is not None and _cnt == limit:
                return

# process the records and elems
stats = collections.defaultdict(int)  # stats[peer_id] = pfx_cnt
for (rec, elem) in elem_generator(bs):
    if "prefix" in elem.fields:
        peer_id = "|".join([rec.collector, str(elem.peer_asn),
                            elem.peer_address])
        stats[peer_id] += 1

df = pandas.DataFrame(sorted(stats.values()), columns=["pfx_cnt"])
df["cdf"] = df["pfx_cnt"].cumsum()/df["pfx_cnt"].sum()*100
df.plot(x="pfx_cnt", y="cdf")
plt.show()
```

