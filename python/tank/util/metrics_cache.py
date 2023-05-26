# Copyright (c) 2023 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
We might want to log event before Toolkit is fully initialized.
For instance, when we authenticate to SGD

This module provide a cache that can be filled prior to Toolkit initilization.
Then empty when the Metric object is initialized...

we could log into environment but it's string only ... So better keep a proper Python object
Let's hide into a Python module.

For some reason, desktopstartup will fully unload tk-core between authentication and launch of desktop. So this is why our singleton does not work

"""


#import collections
import threading

# The module where we are going to store our cache...
import os

from . import metrics
from .. import platform


def _get_lock():
    lock = threading.Lock()
    while True:
        try:
            return os.__sgtk_pending_events_lock
        except AttributeError:
            os.__sgtk_pending_events_lock = threading.Lock()

def _get_instance():
    """
    Must acquire lock before calling this function
    This is why it's a private (_ prefix) method
    """

    # MAXIMUM_QUEUE_SIZE = 100
    #"""
    #Maximum queue size (arbitrary value) until oldest queued item is remove.
    #This is to prevent memory leak in case the engine isn't started.
    #"""
    # queue = collections.deque(maxlen=MAXIMUM_QUEUE_SIZE)

    if not hasattr(os, "__sgtk_pending_events"):
        os.__sgtk_pending_events = []

    return os.__sgtk_pending_events


def log(*args, **kwargs):
    """"
    Same as Metric.log... we just cache it.
    """

    if platform.current_engine():
        # Well, if there is an instance, we don't want to cache but send ...
        return metrics.EventMetric.log(*args, **kwargs)

    # TODO: threading lock mechanism does not look right here ....

    lock = _get_lock()
    lock.acquire()
    try:
        _get_instance().append((args, kwargs))
    finally:
        lock.release()


def consume():
    lock = _get_lock()
    lock.acquire()
    try:
        for item in _get_instance():
            metrics.EventMetric.log(*item[0], **item[1])

        # Cleanup because, after all, once tk-desktop starts, this becomes useless
        del os.__sgtk_pending_events
        del os.__sgtk_pending_events_lock
    finally:
        lock.release()
