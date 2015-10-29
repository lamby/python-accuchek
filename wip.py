#!/usr/bin/env python

import usb.core
import usb.util

dev = usb.core.find(idVendor=0x173a, idProduct=0x21cc)

if dev is None:
    raise ValueError("Device not found")

print "Found %s %s (#%s)" % (
    dev.manufacturer,
    dev.product,
    dev.serial_number,
)

dev.set_configuration()

cfg = dev.get_active_configuration()

def out_endpoints(x):
    return usb.util.ENDPOINT_OUT == \
        usb.util.endpoint_direction(x.bEndpointAddress)

endpoint = usb.util.find_descriptor(cfg[(0,0)], custom_match=out_endpoints)

if endpoint is None:
    raise ValueError("Endpoint not found")

endpoint.write('OUT')

print endpoint.read(1000, 1000)
