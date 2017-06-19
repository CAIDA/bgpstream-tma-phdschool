#!/usr/bin/env python

import collections
import _pybgpstream

TYPE_NAMES = {
    "A": "Announcements",
    "W": "Withdrawals",
    "S": "State Messages",
}

bs = _pybgpstream.BGPStream()
rec = _pybgpstream.BGPRecord()

bs.add_filter('record-type', 'updates')
bs.add_filter('project', 'routeviews')
bs.add_filter('project', 'ris')
bs.add_interval_filter(1483228800, 1483228860)

bs.start()

# stats[upd-type][collector-peer] = update_cnt
stats = collections.defaultdict(lambda: collections.defaultdict(int))

while bs.get_next_record(rec):
    if rec.status == "valid":
        elem = rec.get_next_elem()
        while elem:
            peer_id = "%s|%s" % (rec.collector, elem.peer_asn)
            stats[elem.type][peer_id] += 1
            elem = rec.get_next_elem()

for el_type in TYPE_NAMES:
    print "# of %s per-peer" % TYPE_NAMES[el_type]
    for peer_id in sorted(stats[el_type], key=stats[el_type].get, reverse=True):
        print "  %d\t%s" % (stats[el_type][peer_id], peer_id)

