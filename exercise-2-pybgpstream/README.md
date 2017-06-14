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

## Task 1: Rank peers based on the number of updates observed in 1 minute window

This task is identical to
[Task 2 of the BGPReader exercise](https://github.com/CAIDA/bgpstream-tma-phdschool/blob/master/exercise-1-bgpreader/README.md#task-2-rank-peers-based-on-the-number-of-updates-observed-in-a-1-minute-window),
except you will use PyBGPStream and standard Python features to extract and
post-process the BGP data rather than using command line tools.

As with the BGPReader task, you should configure BGPStream (using the
PyBGPStream API's
[filter methods](http://bgpstream.caida.org/docs/api/pybgpstream/_pybgpstream.html#_pybgpstream.BGPStream.add_filter))
selecting _update data_ for a _1 minute window_. You will then use a nested
while-loop structure like the one shown in the tutorial to iterate through all
Elems, populating a data structure with per-peer statistics. Once all elems have
been processed, print the statistics to `stdout` or to a file.

