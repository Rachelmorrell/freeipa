# Authors: John Dennis <jdennis@redhat.com>
#
# Copyright (C) 2007  Red Hat
# see file 'COPYING' for use and warranty information
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; version 2 only
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

import getpass
import re

from ipa.entity import Entity

__all__ = ['RadiusClient',
           'get_secret',
           'validate_ip_addr',
           'validate_secret',
           'validate_name',
           'validate_nastype',
           'validate_desc',
           ]

#------------------------------------------------------------------------------

dotted_octet_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)(/(\d+))?$")
dns_RE = re.compile(r"^[a-zA-Z][a-zA-Z.-]+$")
# secret, name, nastype all have 31 char max in freeRADIUS, max ip address len is 255
valid_secret_len = (1,31)
valid_name_len = (1,31)
valid_nastype_len = (1,31)
valid_ip_addr_len = (1,255)

valid_ip_addr_msg = "IP address must be either a DNS name or a dotted octet with optional mask"
valid_desc_msg = "Description must text string"

#------------------------------------------------------------------------------

class RadiusClient(Entity):

    def __init2__(self):
        pass
        

#------------------------------------------------------------------------------

def get_secret():
    valid = False
    while (not valid):
        secret = getpass.getpass("Enter Secret: ")
        confirm = getpass.getpass("Confirm Secret: ")
        if (secret != confirm):
            print "Secrets do not match"
            continue
        valid = True
    return secret

#------------------------------------------------------------------------------

def valid_ip_addr(text):

    # is it a dotted octet? If so there should be 4 integers seperated
    # by a dot and each integer should be between 0 and 255
    # there may be an optional mask preceded by a slash (e.g. 1.2.3.4/24)
    match = dotted_octet_RE.search(text)
    if match:
        # dotted octet notation
        i = 1
        while i <= 4:
            octet = int(match.group(i))
            if octet > 255: return False
            i += 1
        if match.group(5):
            mask = int(match.group(6))
            if mask <= 32:
                return True
            else:
                return False
        return True
    else:
        # DNS name, can contain letters, dot and hypen
        if dns_RE.search(text): return True
    return False

def validate_length(value, limits):
    length = len(value)
    if length < limits[0] or length > limits[1]:
        return False
    return True

def valid_length_msg(name, limits):
    return "%s length must be at least %d and not more than %d" % (name, limits[0], limits[1])

#------------------------------------------------------------------------------

def validate_ip_addr(ip_addr):
    if not validate_length(ip_addr, valid_ip_addr_len):
        print valid_length_msg('ip address', valid_ip_addr_len)
        return False
    if not valid_ip_addr(ip_addr):
        print valid_ip_addr_msg
        return False
    return True

def validate_secret(secret):
    if not validate_length(secret, valid_secret_len):
        print valid_length_msg('secret', valid_secret_len)
        return False
    return True

def validate_name(name):
    if not validate_length(name, valid_name_len):
        print valid_length_msg('name', valid_name_len)
        return False
    return True

def validate_nastype(nastype):
    if not validate_length(nastype, valid_nastype_len):
        print valid_length_msg('NAS Type', valid_nastype_len)
        return False
    return True

def validate_desc(desc):
    if ipavalidate.plain(desc, notEmpty=True) != 0:
        print valid_desc_msg
        return False
    return True

