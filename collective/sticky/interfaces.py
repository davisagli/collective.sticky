from zope.interface import Interface


class IBrowserLayer(Interface):
    """Marker for the request applied within sites with this product installed."""

