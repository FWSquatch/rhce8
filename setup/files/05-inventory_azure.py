#!/usr/bin/env python

'''
This is a FAKE SCRIPT that is just being used to show what a dynamic inventory script might return.
'''

import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print (json.dumps(self.inventory))

    # Example inventory for testing.
    def example_inventory(self):
        return {
            'aws': {
                'hosts': ['192.168.88.101', '192.168.88.102'],
                'vars': {
                    'ansible_ssh_user': 'vagrant',
                    'ansible_ssh_private_key_file':
                        '~/.ssh/id_rsa',
                    'example_variable': 'value'
                }
            },
            '_meta': {
                'hostvars': {
                    '192.168.88.101': {
                        "ansible_fqdn": "node1.rhce.lab",
                        "ansible_hostname": "node1",
                        'favorite_jelly_bean': 'pink'
                    },
                    '192.168.88.102': {
                        "ansible_fqdn": "node2.rhce.lab",
                        "ansible_hostname": "node2",
                        'favorite_jelly_bean': 'green'
                    }
                }
            }
        }

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()
