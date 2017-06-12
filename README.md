# BGPStream Lab, TMA PhD School 2017

## Lab Prerequisite: BGPStream and PyBGPStream
_Please ensure that you have BGPStream installed prior to attending the lab. Contact bgpstream-info@caida.org with any problems that encounter._

For this lab, you will need to have access to a machine with BGPStream and PyBGPStream installed. This could be on your laptop that you will have with you in the lab, or on a remote server that you will access e.g., via SSH.

The [BGPStream website](https://bgpstream.caida.org) has [install instructions](http://bgpstream.caida.org/docs/install) for a variety of operating systems.

## Exercises

The first two exercises are simple and designed to get you familiar with using
BGPStream, first from the command line (using
[bgpreader](http://bgpstream.caida.org/docs/tools/bgpreader)), and then
programatically from within Python (using
[PyBGPStream](http://bgpstream.caida.org/docs/api/pybgpstream)). If you have
already used BGPStream you may consider skipping these exercises.

 - Exercise 1: [Using BGPReader](https://github.com/CAIDA/bgpstream-tma-phdschool/blob/master/exercise-1-bgpreader/README.md)
 - Exercise 2: [Using PyBGPStream](https://github.com/CAIDA/bgpstream-tma-phdschool/blob/master/exercise-2-pybgpstream/README.md)

The remaining exercises are more complex and are designed to give you an idea of
how to use BGPStream as part of your research. Because we have limited time, you
should look quickly at the description for each exercise and start with the one
you find most interesting.

 - Exercise 3: [Building a "BGP Info" HTTP API using realtime BGP data](https://github.com/CAIDA/bgpstream-tma-phdschool/blob/master/exercise-3-bgp-info/README.md)
 - Exercise 4: [Triggering active probing based on BGP events](https://github.com/CAIDA/bgpstream-tma-phdschool/blob/master/exercise-4-active-probing/README.md)
 - Exercise 5: [Longitudinal data analysis using Apache Spark](https://github.com/CAIDA/bgpstream-tma-phdschool/blob/master/exercise-5-spark/README.md)
