# Exercise 1: BGPReader

BGPReader is a command-line tool that is installed as part of the BGPStream Core
package. It is useful for quick inspection of BGP data, and can be thought of as
a replacement for the `bgpdump` tool (in fact, it has an output mode that is
identical to that of bgpdump, so in some cases it can be used as a drop-in
replacement).

The goal of this exercise is to familiarize you with the BGPReader tool, as well
as highlighting the various data types (e.g. RIBs and Updates) and filtering
options provided by BGPStream.

See the
[BGPReader documentation](http://bgpstream.caida.org/docs/tools/bgpreader) for
detailed usage information and a description of the BGPReader output formats.

## Task 1: Find paths to a prefix of interest in a RIB table

For this task you should configure BGPReader to obtain RIB data from a single
collector (see https://bgpstream.caida.org/data for a list of collectors),
filtered to a single prefix of interest (e.g., that of your university).  This
can be accomplished with a single `bgpreader` command, and the output should
require no further filtering.

_Tip:_ Route Views collectors output a RIB every 2 hours whereas RIPE RIS
collectors output a RIB every 8 hours (both aligned to midnight). Also, RIB
dumps are made atomically, so you should specify a window of a few minutes
(e.g., 00:00 -> 00:05). Also, if you don't already have a favorite collector to
test with, you may want to use `route-views.sg`, which has only a few full-feed
peers and is thus fast to process data for.

## Task 2: Rank peers based on the number of updates observed in a 1 minute window

For this task you should use BGPReader to output the updates for all Route Views
and RIPE RIS collectors for a 1 minute window of your chosing, and then pipe the
output into standard unix tools (e.g., `sort`, `uniq`, etc.) to rank the
peers. Bonus points if you separate the ranking by update type (i.e.,
announcements and withdrawals).
