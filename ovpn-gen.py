#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Template
import sys
'''Generate an .ovpn file from a set of user keys
to be used with an ovpn client.
'''

try:
  username = sys.argv[1]
except:
  print 'Error: Supply a username!'
  sys.exit()

try:
  server = sys.argv[2]
except:
  print 'Error: Need an ip and port "12.34.56.78 1194"'
  sys.exit()
#'/etc/openvpn/easy-rsa'
ca = '/etc/openvpn/easy-rsa/keys/ca.crt'
usercert = '/etc/openvpn/easy-rsa/keys/' + username + '.crt'
userkey = '/etc/openvpn/easy-rsa/keys/' + username + '.key'
userovpn = username + '.ovpn'

with open('templates/ovpn.template') as ovpntemplate, \
        open(usercert) as certfile, \
        open(userkey) as keyfile, \
        open(ca) as cafile, \
        open(userovpn, 'w') as outfile:
  model = Template(ovpntemplate.read())
  certvalue = certfile.read()
  keyvalue = keyfile.read()
  cavalue = cafile.read()
  outfile.write(model.render(usercert=certvalue, userkey=keyvalue, cacert=cavalue, servername=server))
  print model.render(usercert=certvalue, userkey=keyvalue, cacert=cavalue, servername=server)
  print 'OVPN file generated:' + username + '.ovpn'

