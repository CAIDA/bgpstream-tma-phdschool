# Exercise 1: BGPReader

BGPReader is a command-line tool that is useful for quick inspection of BGP
data, and is installed as part of the BGPStream Core package. It dumps
information about Records and/or Elems to `stdout` in a parsable ASCII format.

The goal of this exercise is to familiarize you with the BGPReader tool, as well
as highlight the data types (RIBs and Updates) and filtering options provided by
BGPStream.

See the
[BGPReader documentation](http://bgpstream.caida.org/docs/tools/bgpreader) for
detailed usage information and a description of the BGPReader output formats.

## Task 1: Find paths to a prefix of interest in a RIB table

For this task you should configure BGPReader to obtain _RIB data_ from a _single
collector_, filtered to a _prefix that your university announces_.

In this exercise, for the sake of time, you should use the `route-views.sg`
collector as it has only a few full-feed peers, however in general you can find
a list of collectors at https://bgpstream.caida.org/data.

To identify a prefix that your university announces, you can use
http://bgp.he.net to search for your university (this service provides a bunch
of interesting information about ASes and prefixes).

Route Views collectors output a RIB every 2 hours whereas RIPE RIS collectors
output a RIB every 8 hours (both aligned to midnight). Also, RIB dumps are not
made atomically, so you should specify a window of a few minutes (e.g., 00:00 ->
00:05).

## Task 2: Rank peers based on the number of updates observed in a 1 minute window

For this task you should use BGPReader to output the updates for all Route Views
and RIPE RIS collectors for a 1 minute window of your chosing, and then pipe the
output into standard unix tools (e.g., `sort`, `uniq`, etc.) to rank the peer
ASes in terms of the number of updates seen from each. Bonus points if you
separate the ranking by update type (i.e., announcements and withdrawals).

Note, some ASes are peered with by multiple collectors, so you should also
consider the collector name part of the "key" for uniquely identifying a peer
(i.e., `collector|peer-AS`).
