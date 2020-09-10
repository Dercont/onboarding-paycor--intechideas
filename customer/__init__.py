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
            'target': ['address']
        }
    },
    {
        'default': lambda: 'US',
        'validator': lambda field: '',
        'keys': {
            'source': ['country'],
            'target': ['country_code']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['employeeCity'],
            'target': ['city']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['employeeEmailAddress'],
            'target': ['email_address']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['employeeID'],
            'target': ['employee_id']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['firstName'],
            'target': ['first_name']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['lastName'],
            'target': ['last_name']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['mobilePhoneNumber'],
            'target': ['mobile_phone']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['state'],
            'target': ['state_code']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': ['zipCode'],
            'target': ['zip']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': [''],
            'target': ['business_phone']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': [''],
            'target': ['business_phone_extension']
        }
    },
    {
        'default': lambda: True,
        'validator': lambda field: '',
        'keys': {
            'source': ['__is_active'],
            'target': ['is_active']
        }
    },
    {
        'default': lambda: True,
        'validator': lambda field: '',
        'keys': {
            'source': ['__is_employee'],
            'target': ['is_employee']
        }
    },
    {
        'default': lambda: '',
        'validator': lambda field: '',
        'keys': {
            'source': [''],
            'target': ['vendor_id']
        }
    },
]

pre_formatters = get_pre_formatters() + []
post_formatters = get_post_formatters() + []
