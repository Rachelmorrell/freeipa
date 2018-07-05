#
# Copyright (C) 2018  FreeIPA Contributors see COPYING for license
#

ENTITY = 'selfservice'
PKEY = 'itest-selfservice-rule'
DATA = {
    'pkey': PKEY,
    'add': [
        ('textbox', 'aciname', PKEY),
        ('checkbox', 'attrs', 'audio'),
        ('checkbox', 'attrs', 'businesscategory'),
    ],
    'mod': [
        ('checkbox', 'attrs', 'businesscategory'),
    ],
}

PKEY1 = 'itest-selfservice-rule1'
DATA1 = {
    'pkey': PKEY1,
    'add': [
        ('textbox', 'aciname', PKEY1),
        ('checkbox', 'attrs', 'businesscategory'),
    ],
    'mod': [
        ('checkbox', 'attrs', 'businesscategory'),
        ('checkbox', 'attrs', 'departmentnumber'),
        ('checkbox', 'attrs', 'destinationindicator'),
    ],
}

DATA2 = [
    ('checkbox', 'attrs', 'businesscategory'),
    ('checkbox', 'attrs', 'departmentnumber'),
    ('checkbox', 'attrs', 'destinationindicator'),
]

DATA_ALL = {
    'pkey': PKEY,
    'add': [
        ('textbox', 'aciname', PKEY),
        ('checkbox', 'attrs', 'audio'),
        ('checkbox', 'attrs', 'businesscategory'),
        ('checkbox', 'attrs', 'carlicense'),
        ('checkbox', 'attrs', 'cn'),
        ('checkbox', 'attrs', 'departmentnumber'),
        ('checkbox', 'attrs', 'description'),
        ('checkbox', 'attrs', 'destinationindicator'),
        ('checkbox', 'attrs', 'displayname'),
        ('checkbox', 'attrs', 'employeenumber'),
        ('checkbox', 'attrs', 'employeetype'),
        ('checkbox', 'attrs', 'facsimiletelephonenumber'),
        ('checkbox', 'attrs', 'gecos'),
        ('checkbox', 'attrs', 'gidnumber'),
        ('checkbox', 'attrs', 'givenname'),
        ('checkbox', 'attrs', 'homedirectory'),
        ('checkbox', 'attrs', 'homephone'),
        ('checkbox', 'attrs', 'homepostaladdress'),
        ('checkbox', 'attrs', 'inetuserhttpurl'),
        ('checkbox', 'attrs', 'inetuserstatus'),
        ('checkbox', 'attrs', 'initials'),
        ('checkbox', 'attrs', 'internationalisdnnumber'),
        ('checkbox', 'attrs', 'ipacertmapdata'),
        ('checkbox', 'attrs', 'ipakrbauthzdata'),
        ('checkbox', 'attrs', 'ipasshpubkey'),
        ('checkbox', 'attrs', 'ipatokenradiusconfiglink'),
        ('checkbox', 'attrs', 'ipatokenradiususername'),
        ('checkbox', 'attrs', 'ipauniqueid'),
        ('checkbox', 'attrs', 'ipauserauthtype'),
        ('checkbox', 'attrs', 'jpegphoto'),
        ('checkbox', 'attrs', 'krballowedtodelegateto'),
        ('checkbox', 'attrs', 'krbcanonicalname'),
        ('checkbox', 'attrs', 'krbextradata'),
        ('checkbox', 'attrs', 'krblastadminunlock'),
        ('checkbox', 'attrs', 'krblastfailedauth'),
        ('checkbox', 'attrs', 'krblastpwdchange'),
        ('checkbox', 'attrs', 'krblastsuccessfulauth'),
        ('checkbox', 'attrs', 'krbloginfailedcount'),
        ('checkbox', 'attrs', 'krbmaxrenewableage'),
        ('checkbox', 'attrs', 'krbmaxticketlife'),
        ('checkbox', 'attrs', 'krbpasswordexpiration'),
        ('checkbox', 'attrs', 'krbprincipalaliases'),
        ('checkbox', 'attrs', 'krbprincipalauthind'),
        ('checkbox', 'attrs', 'krbprincipalexpiration'),
        ('checkbox', 'attrs', 'krbprincipalkey'),
        ('checkbox', 'attrs', 'krbprincipalname'),
        ('checkbox', 'attrs', 'krbprincipaltype'),
        ('checkbox', 'attrs', 'krbpwdhistory'),
        ('checkbox', 'attrs', 'krbpwdpolicyreference'),
        ('checkbox', 'attrs', 'krbticketflags'),
        ('checkbox', 'attrs', 'krbticketpolicyreference'),
        ('checkbox', 'attrs', 'krbupenabled'),
        ('checkbox', 'attrs', 'l'),
        ('checkbox', 'attrs', 'labeleduri'),
        ('checkbox', 'attrs', 'loginshell'),
        ('checkbox', 'attrs', 'mail'),
        ('checkbox', 'attrs', 'manager'),
        ('checkbox', 'attrs', 'memberof'),
        ('checkbox', 'attrs', 'mepmanagedentry'),
        ('checkbox', 'attrs', 'mobile'),
        ('checkbox', 'attrs', 'o'),
        ('checkbox', 'attrs', 'objectclass'),
        ('checkbox', 'attrs', 'ou'),
        ('checkbox', 'attrs', 'pager'),
        ('checkbox', 'attrs', 'photo'),
        ('checkbox', 'attrs', 'physicaldeliveryofficename'),
        ('checkbox', 'attrs', 'postaladdress'),
        ('checkbox', 'attrs', 'postalcode'),
        ('checkbox', 'attrs', 'postofficebox'),
        ('checkbox', 'attrs', 'preferreddeliverymethod'),
        ('checkbox', 'attrs', 'preferredlanguage'),
        ('checkbox', 'attrs', 'registeredaddress'),
        ('checkbox', 'attrs', 'roomnumber'),
        ('checkbox', 'attrs', 'secretary'),
        ('checkbox', 'attrs', 'seealso'),
        ('checkbox', 'attrs', 'sn'),
        ('checkbox', 'attrs', 'st'),
        ('checkbox', 'attrs', 'street'),
        ('checkbox', 'attrs', 'telephonenumber'),
        ('checkbox', 'attrs', 'teletexterminalidentifier'),
        ('checkbox', 'attrs', 'telexnumber'),
        ('checkbox', 'attrs', 'title'),
        ('checkbox', 'attrs', 'uid'),
        ('checkbox', 'attrs', 'uidnumber'),
        ('checkbox', 'attrs', 'usercertificate'),
        ('checkbox', 'attrs', 'userclass'),
        ('checkbox', 'attrs', 'userpassword'),
        ('checkbox', 'attrs', 'userpkcs12'),
        ('checkbox', 'attrs', 'usersmimecertificate'),
        ('checkbox', 'attrs', 'x121address'),
        ('checkbox', 'attrs', 'x500uniqueidentifier'),
    ],
}