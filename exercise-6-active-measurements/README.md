# Exercise 6: Triggering Active Measurements

As you saw in the previous exercise, BGPStream makes it easy to process BGP data
in a near-realtime fashion. Coupling this with on-demand active measurement
services (e.g., RIPE Atlas) allows one to trigger active measurements in
response to control plane events -- possibly capturing transient routing
phenomena.

In this exercise you will write a script to monitor BGP data for "interesting"
prefix announcements and execute a traceroute toward an IP address within the
announced prefix. While you would normally use a service like RIPE Atlas for
executing such traceroute measurements, to keep this exercise as simple as
possible, you can just use the `traceroute` command on your local machine.

## Steps

1. Use the "live" monitoring script that you wrote in Exercise 5.

1. Modify the code so that instead of outputting statistics each minute, it
selects one (arbitrary) prefix every 30 seconds. Compute the first usable IP
address within the prefix (e.g., `192.172.226.1` for `192.172.226.0/24`), and
`print` the prefix, AS path, and computed IP address to `stdout`. (See the note
below.)

1. Using the code snippet below, execute a traceroute to the selected IP
address, and `print` the returned results to `stdout`, along with the prefix,
target IP, and AS path.


_Note:_ In a real script you would likely trigger measurements based on events
that you are interested in. For example, an announcement from a specific origin
AS, or an announcement that creates a MOAS, etc.. However, to ensure we find
_something_ to traceroute, we'll just pick any announcement.


## Traceroute Code

The following will execute a traceroute to the given IP address by calling the
system `traceroute` command. This has been tested on macOS and Ubuntu 14.04. It
almost certainly won't work on Windows without at least some modification. **You
definitely must not use this code to do any real research!**

```python
def do_traceroute(target_ip, command="traceroute", args=None):
    # TODO!
    return ""
```
