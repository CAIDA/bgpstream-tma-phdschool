# Exercise 5: Path Sanitization & Realtime Processing

When analyzing AS path data from BGP measurements, it is often necessary to
perform sanitization of the hops in the path, in order to either remove features
that can skew statistics (e.g., prepending), or to identify (and potentially
filter) anomalous paths (e.g., with reserved ASNs, or AS sets).

In this exercise, you will learn to perform path sanitization, implement filters
not (yet) supported natively by BGPStream (i.e., origin ASN), and experiment
with near-realtime monitoring of BGP data.

## Steps

1. Continue using the same BGPStream configuration as in Exercise 4: RIB records
from `route-views2` between 00:00 and 01:00 on Jan 15th 2017.

1. Replace the community-processing code with code that splits the AS path into
hops -- you can split the string on the space character (see the note below).

1. Once you have a list of AS hops, process them to remove prepending (adjacent,
repeated ASNs).

1. Then, identify hops that are not a "simple" ASN. That is, those that are: AS
sets (`AS_SET`), AS sequences (`AS_SEQUENCE`), confederation sets
(`AS_CONFED_SET`), or confederation sequences (`AS_CONFED_SEQUENCE`).

1. Finally using
[IANA.SpecialAS](https://www.iana.org/assignments/iana-as-numbers-special-registry/iana-as-numbers-special-registry.xhtml)
as a guide, identify those hops that are "special-use" ASNs.

1. For each of the classes of sanitization that you have performed (prepending,
sets, confederation sets, confederation sequences, and special-use ASNs), count
the number of paths that each occurs in (a single path may have multiple
phenomena), and output a table to `stdout`.

1. Before you move to the next exercise, change your code to process `updates`
data, and output the statistics table for _every minute_ of BGP data processed.
Use `elem.time` to determine the "current" time (i.e., don't use your system
clock). Once you are satisfied that this works, remove the `collector` filter
(i.e., process data from all collectors), and change the time interval only have
a single (start) time, set to approximately 30 mins ago. This will put BGPStream
into "live" mode and your script will process updates as they are made
available. Leave this running for at least 10 mins as you work on the next
exercise and you should see your stats table continue to be output as more data
is processed.


_Note:_ While not common, it is theoretically possible to have a Confederation
Sequence hop ([RFC5065](https://tools.ietf.org/html/rfc5065)), the notation for
which is `(A B C)`, which would cause problems when we split the path string on
the space character. Given this, you must always check for the presence of `(`
in the AS path string, and if found, handle it appropriately.

add live step: after sanitization, look for something, then output something
look for a specific origin (i need to find one that is chatty)
look for specific prefix lengths?
