from PyQt4.QtGui import QPen
from PyQt4.Qt import Qt
from sloth.items import RectItem, PointItem

class CustomRectItem(RectItem):
    def __init__(self, *args, **kwargs):
        RectItem.__init__(self, *args, **kwargs)

        # set drawing pen to red with width 2
        self.setPen(QPen(Qt.red, 2))

class CustomPointItem(PointItem):
    def __init__(self, *args, **kwargs):
        PointItem.__init__(self, *args, **kwargs)
        self.setRadius(6)
        # set drawing pen to red with width 2
        self.setPen(QPen(Qt.red, 4))

LABELS = (
    {
        'attributes': {
            'class':      'Person',
         },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     CustomRectItem,
        'hotkey':   'p',
        'text':     'Person',
    },
    {
        'attributes': {
            'class':    'Left Hand',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   'h',
        'text':     'Left Hand',
    },
    {
        'attributes': {
            'class':    'Left Elbow',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   'e',
        'text':     'Left Elbow',
    },
    {
        'attributes': {
            'class':    'Left Shoulder',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   's',
        'text':     'Left Shoulder',
    },
    {
        'attributes': {
            'class':    'Right Hand',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   'z',
        'text':     'Right Hand',
    },
    {
        'attributes': {
            'class':    'Right Elbow',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   'x',
        'text':     'Right Elbow',
    },
    {
        'attributes': {
            'class':    'Right Shoulder',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   'c',
        'text':     'Right Shoulder',
    },
    {
        'attributes': {
            'class':    'Head',
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   'o',
        'text':     'Head',
    },
  


     {
        'attributes': {
            'class':      'Arms crossed',
         },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   'a',
        'text':     'Arms crossed',
    },
     {
        'attributes': {
            'class':      'Both Arms on Table',
         },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   't',
        'text':     'Both Arms on Table',
    },
     {
        'attributes': {
            'class':      'Both Arms on Body',
         },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   'b',
        'text':     'Both Arms on Body',
    },
     {
        'attributes': {
            'class':      'One Arm on Body',
         },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   'm',
        'text':     'One Arm on Body',
    },
     {
        'attributes': {
            'class':      'One Arm on Table',
         },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   'n',
        'text':     'One Arm on Table',
    },
{
        'attributes': {
            'class':      'Leaning forward',
         },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   ',',
        'text':     'Leaning forward',
    },
{
        'attributes': {
            'class':      'Leaning backward',
         },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   '.',
        'text':     'Leaning backward',
    },
{
        'attributes': {
            'class':      'Upright',
         },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     CustomPointItem,
        'hotkey':   '/',
        'text':     'Upright',
    },
     
)
