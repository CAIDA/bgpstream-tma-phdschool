# Exercise 3: Investigate peer routing table sizes

The goal of this exercise is to build a distribution of per-peer routing table
sizes in order to understand the difference between "partial" and "full-feed"
peers. To do this, you should modify the script you wrote in Exercise 2 to 
count the number of unique prefixes per-peer in a RIB dump, then plot a
distribution. You should see a "knee" in the graph that divides the partial
peers from the full-feed peers.

### Steps

1. Modify your script to process RIB (`ribs`) data instead of Updates 
(`updates`), select only a single collector (`route-views.sg`), and select a
time interval that includes a RIB dump (`2017-01-15 00:00 -> 01:00`).
1. Modify your statistics collection to count the number of unique
prefixes each peer announces (instead of number of updates).
1. Use your preferred plotting tool to generate a distribution of peer routing
table sizes
