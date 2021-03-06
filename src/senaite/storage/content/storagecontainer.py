# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.STORAGE
#
# Copyright 2019 by it's authors.

from Products.Archetypes.Field import FloatField
from Products.Archetypes.Schema import Schema
from Products.Archetypes.atapi import registerType
from bika.lims import api
from bika.lims.browser.widgets.decimal import DecimalWidget
from senaite.storage import PRODUCT_NAME
from senaite.storage import senaiteMessageFactory as _
from senaite.storage.content.storagelayoutcontainer import \
    StorageLayoutContainer
from senaite.storage.content.storagelayoutcontainer import schema
from senaite.storage.interfaces import IStorageContainer
from zope.interface import implements

Temperature = FloatField(
    name = "Temperature",
    widget = DecimalWidget(
        label = _("Expected temperature"),
        description = _("Expected temperature of this container")
    )
)

schema = schema.copy() + Schema((
    Temperature,
))

class StorageContainer(StorageLayoutContainer):
    """Container for the storage of other storage containers
    """
    implements(IStorageContainer)
    schema = schema

    def is_object_allowed(self, object_brain_uid):
        """Returns whether the type of object can be stored or not in this
        container. This function returns true if the object is allowed, even
        if the container already contains the object
        """
        # Only children from this container are allowed
        obj = api.get_object(object_brain_uid)
        return api.get_uid(api.get_parent(obj)) == api.get_uid(self)

registerType(StorageContainer, PRODUCT_NAME)
