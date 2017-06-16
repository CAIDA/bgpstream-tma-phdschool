# Exercise 4: Analyze community attributes

The goal of this exercise is to analyze the community attributes observed in a
RIB dump in order to understand @@.

While the community path attribute
([RFC1997](https://tools.ietf.org/html/rfc1997)) is defined simply as sequence
of 32-bit numbers, each value in the sequence is encoded by placing an ASN in
the first 2 octets, leaving semantics of the second 2 octets to be defined by
the AS itself. As such, PyBGPStream makes the 
[community path available](http://bgpstream.caida.org/docs/api/pybgpstream/_pybgpstream.html#_pybgpstream.BGPElem.fields)
as a sequence of `dict` objects, where each `dict` has the keys `asn` and
`value`.
 
## Steps

In this exercise, you will modify the script that you wrote in Exercise 3 to:

1. Count the number of _unique_ AS values seen in community attributes. How many
ASes do you observe setting at least one community value?.
1. Plot the distribution of per-AS community `value`s. This will require
building a per-AS set of observed community values.
1. Now try switching the collector to `route-views.XX`. What do you observe?
