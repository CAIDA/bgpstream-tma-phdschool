# BGPStream Lab, TMA PhD School 2017

## Lab Prerequisite: BGPStream and PyBGPStream
_Please ensure that you have BGPStream installed prior to attending the
lab. Contact bgpstream-info@caida.org with any problems that you encounter._

For this lab, you will need to have access to a machine with BGPStream and
PyBGPStream installed. This could be on your laptop that you will have with you
in the lab, or on a remote server that you will access e.g., via SSH.

The [BGPStream website](https://bgpstream.caida.org) has
[install instructions](http://bgpstream.caida.org/docs/install) for a variety of
operating systems.

## Exercises

The first two exercises are simple and designed to get you familiar with using
BGPStream, first from the command line (using
[BGPReader](http://bgpstream.caida.org/docs/tools/bgpreader)), and then
programatically from within Python (using
[PyBGPStream](http://bgpstream.caida.org/docs/api/pybgpstream)).

 - Exercise 1: [Using BGPReader](exercise-1-bgpreader/README.md)
 - Exercise 2: [Using PyBGPStream](exercise-2-pybgpstream/README.md)

The remaining exercises all use PyBGPStream and build on the code you wrote in
Exercise 2.

 - Exercise 3: [Peer routing table sizes](exercise-3-routing-tables/README.md)
 - Exercise 4: [Communities](exercise-4-communities/README.md)
 - Exercise 5: [AS path sanitization](exercise-5-path-sanitization/README.md)
 - Exercise 6: [Triggering active measurements](exercise-6-active-measurements/)

## Troubleshooting

If you plan to run BGPStream on your laptop (or a machine with limited RAM), you
may want to run the following in your shell before running `bgpreader` or any
scripts that use PyBGPStream:
```
export LIBTRACEIO=nothreads
```
This will force BGPStream to use a single thread for reading BGP data, and will
use significantly less memory.

## Helpful Patterns

### Elem generator
You may find it more convenient to define a generator function that hides the
code to extract Records and Elems from the stream. The next version of
PyBGPStream will include an API similar to this.

First, define the generator function (you can use this code verbatim):
```python
def elem_generator(_stream):
    _rec = _pybgpstream.BGPRecord()
    while _stream.get_next_record(_rec):
        while True:
            _elem = _rec.get_next_elem()
            if _elem is None:
                return
            yield (_rec, _elem)
```

Then, instantiate the stream like normal and use the standard Python
`for ... in ...` syntax to iterate over records and elems in the stream:
```python
bs = _pybgpstream.BGPStream()
# configure the stream here
bs.start()

for (rec, elem) in elem_generator(bs):
    print "%s: %s" % (rec.collector, elem.peer_asn)
```
