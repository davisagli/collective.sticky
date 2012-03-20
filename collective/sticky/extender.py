from zope.interface import implements
from zope.component import adapts
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender
from archetypes.schemaextender.field import ExtensionField
from plone.indexer import indexer
from Products.Archetypes import atapi
from Products.ATContentTypes.interfaces import IATNewsItem
from collective.sticky.interfaces import IBrowserLayer


class CheckboxField(ExtensionField, atapi.BooleanField):
    pass


class StickySchemaExtender(object):
    implements(ISchemaExtender, IBrowserLayerAwareExtender)
    adapts(IATNewsItem)

    layer = IBrowserLayer

    _fields = [CheckboxField('sticky',
        schemata='categorization',
        widget=atapi.BooleanWidget(
            label='Should this page be "sticky" and appear at the top of sticky-aware collections?',
            ),
        default=False,
        )]

    def __init__(self, context):
        if context.portal_type != 'News Item':
            return
        self.context = context

    def getFields(self):
        return self._fields


@indexer(IATNewsItem)
def sticky(context):
    return context.getField('sticky').get(context)
