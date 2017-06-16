# Exercise 3: Investigate peer routing table sizes

The goal of this exercise is to build a distribution of per-peer routing table
sizes in order to understand the difference between "partial" and "full-feed"
peers. To do this, you should modify the script you wrote in Exercise 2 to count
the number of unique prefixes per-peer in a RIB dump, then plot a distribution.

### Steps

1. Modify your script to process RIB (`ribs`) data instead of Updates
(`updates`), select only a single collector (use `route-views2` this time), and
select a time interval that includes a RIB dump (`2017-01-15 00:00 -> 01:00`).
1. Modify your statistics collection to count the number of unique prefixes each
peer announces (instead of number of updates). 
1. Use your preferred plotting tool to generate a CDF of peer routing table
sizes. You should see a "knee" at the right side of the graph that represents
the full-feed peers. What would be a good threshold for determining if a peer is
full-feed?

To minimize memory usage, you may assume that prefixes are not duplicated for a
given peer and simply count them, rather than building a set of prefixes for
each peer. Additionally, it takes my laptop around 5 minutes to process a RIB
dump from `route-views2`, so _you should add a short-circuit to your code during
testing (e.g., break out of the loop after processing 500k elems)_.
