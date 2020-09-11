import json
import os
import inspect
import re

from .formatters import get_pre_formatters, get_post_formatters, Formatters
from core.rules import get_common_formatters

formatters = [
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['addressLine1'],
            'target': ['addressLine1']
        }
    },
    {
        'default': lambda: 'US',
        'validator': lambda field: '',
        'keys': {
            'source': ['country'],
            'target': ['country']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['employeeCity'],
            'target': ['employeeCity']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['employeeEmailAddress'],
            'target': ['employeeEmailAddress']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['employeeID'],
            'target': ['employeeID']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['firstName'],
            'target': ['firstName']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['lastName'],
            'target': ['lastName']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['mobilePhoneNumber'],
            'target': ['mobilePhoneNumber']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['state'],
            'target': ['state']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['zipCode'],
            'target': ['zipCode']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['business_phone'],
            'target': ['business_phone']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['business_phone_extension'],
            'target': ['business_phone_extension']
        }
    },
    {
        'default': lambda: True,
        'validator': lambda field: '',
        'keys': {
            'source': ['is_active'],
            'target': ['is_active']
        }
    },
    {
        'default': lambda: True,
        'validator': lambda field: '',
        'keys': {
            'source': ['is_employee'],
            'target': ['is_employee']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['vendor_id'],
            'target': ['vendor_id']
        }
    },
]

pre_formatters = get_pre_formatters() + []
post_formatters = get_post_formatters() + []
