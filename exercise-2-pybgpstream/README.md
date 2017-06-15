# Exercise 2: PyBGPStream

PyBGPStream is Python package that provides bindings to the libBGPStream
library, allowing Python scripts to configure and read a stream of BGP
measurement data.

The goal of this exercise to to familiarize you with the PyBGPStream API, which
will be used in all subsequent exercises.

See the PyBGPStream
[API documentation](http://bgpstream.caida.org/docs/api/pybgpstream/_pybgpstream.html)
and [tutorial](http://bgpstream.caida.org/docs/tutorials/pybgpstream) for usage
information.

## Rank peers based on the number of updates observed in 1 minute window

This task is identical to
[Task 2 of the BGPReader exercise](/exercise-1-bgpreader/README.md),
except you will use PyBGPStream and standard Python features to extract and
post-process the BGP data rather than using command line tools.

In the BGPReader task, you configured BGPStream by specifying command-line
arguments. PyBGPStream supports all the same filtering options as BGPReader,
but these filters are applied programmatically using method calls.

### Steps

1. Use the 
[code](http://bgpstream.caida.org/bundles/caidabgpstreamwebhomepage/docs/tutorials/code/pybgpstream-print.py)
in the 
[PyBGPStream tutorial](http://bgpstream.caida.org/docs/tutorials/pybgpstream)
as a starting point.
1. Configure BGPStream to include only _update_ data for a _1 minute window_
using the
[filter methods](http://bgpstream.caida.org/docs/api/pybgpstream/_pybgpstream.html#_pybgpstream.BGPStream.add_filter).
1. Modify the inner `while` loop (that iterates over Elems) to build a data
structure that tracks the number of elems from each peer (remember to use
`collector|peer-AS|peer-IP` as the ID of a peer).
1. After processing the data from BGPStream output a ranking of peer update 
volume (from most to least) either to `stdout` or to a file.
1. _(Bonus)_ Separate the statistics by elem type
(Annoucements, Withdrawal, and State Messages).
