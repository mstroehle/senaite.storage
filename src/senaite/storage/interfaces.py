# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.STORAGE
#
# Copyright 2019 by it's authors.

from bika.lims.interfaces import IBikaLIMS
from senaite.lims.interfaces import ISenaiteLIMS
from zope.interface import Interface


class ISenaiteStorageLayer(IBikaLIMS, ISenaiteLIMS):
    """Zope 3 browser Layer interface specific for senaite.storage
    This interface is referred in profiles/default/browserlayer.xml.
    All views and viewlets register against this layer will appear in the site
    only when the add-on installer has been run.
    """


class ISenaiteStorageCatalog(Interface):
    """Marker interface for senaite_storage_catalog CatalogTool
    """


class IStorageRootFolder(Interface):
    """Marker interface for Storage's root folders
    """


class IStorageFacility(Interface):
    """Marker interface for objects that represent a physical location or place
    where one or more storage containers are located. (room, department, etc.)
    """


class IStorageLayoutContainer(Interface):
    """Marker interface for objects that act as containers, either of other
    containers or other type of objects such as samples. All these objects have
    layout field in common in which the positions where the stored elements are
    defined.
    """


class IStorageContainer(Interface):
    """Marker interface for objects that represent an storage container designed
    for the storage of one or more than one elements inside, typically other
    containers. E.g: fridge, rack, shelf, floating rack, tube rack, box, etc.
    """


class IStorageSamplesContainer(IStorageContainer):
    """Marker interface for objects that represent a type of storage container
    designed for the storage of multiple samples (storage box, tube rack, etc.)
    """
