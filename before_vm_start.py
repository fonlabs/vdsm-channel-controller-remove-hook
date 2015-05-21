#!/usr/bin/python2
from __future__ import unicode_literals

import sys
import os
import hooking

def filter_nodes(domxml):
    dev_elem = domxml.getElementsByTagName('devices')[0]
    if not dev_elem:
        return
    # Delete the channels
    # getElementsByTagName returns recursive, not just childs
    channels =  [elem for elem in dev_elem.getElementsByTagName('channel') if elem in dev_elem.childNodes]
    for device in channels:
        if device.getAttribute('mode'):
            return
        dev_elem.removeChild(device)
    # Delete the serial controller
    controllers =  [elem for elem in dev_elem.getElementsByTagName('controller') if elem in dev_elem.childNodes]
    for device in controllers:
        if device.getAttribute('type') == 'virtio-serial':
            dev_elem.removeChild(device)


if os.environ.get('channel_remove', 'False').strip().lower() == "false":
    sys.exit(0)

try:
    domxml = hooking.read_domxml()
    filter_nodes(domxml)
    hooking.write_domxml(domxml)
except Exception as e:
    sys.stderr.write("Unexpected error on channel removal\n")
    sys.exit(2)
