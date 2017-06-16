# Exercise 4: Analyze community attributes

The goal of this exercise is to analyze the community attributes observed in a
RIB dump in order to gain experience with how communities are structured and how
they are observed by collectors.

While the community path attribute
([RFC1997](https://tools.ietf.org/html/rfc1997)) is defined simply as sequence
of 32-bit numbers, each value in the sequence is encoded by placing an ASN in
the first 2 octets, leaving semantics of the second 2 octets to be defined by
the AS itself. As such, PyBGPStream makes the 
[community path available](http://bgpstream.caida.org/docs/api/pybgpstream/_pybgpstream.html#_pybgpstream.BGPElem.fields)
as a sequence of `dict` objects, where each `dict` has the keys `asn` and
`value`.
 
## Tasks

In this exercise, you will modify the script that you wrote in Exercise 3 to:

1. Plot the CDF of unique ASes that set community attributes per peer (still
using `route-views2`). Consider only the `asn` field of the community as the
"key" in this case (i.e., build a per-peer set of `asn` values). Why do
different collectors see different numbers of ASes setting communities?

1. Count the overall number of _unique_ AS values seen in all community
attributes for all peers of `route-views.sg`. I.e., how many ASes do you observe
setting at least one community value?.

1. Plot the CDF of number of unique community `value`s per-community `asn`. This
will require building a per-AS set of observed community values.

