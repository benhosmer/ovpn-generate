ovpn-generate
=============

A python script that generates an .ovpn file after building client keys.

You can build client keys with OpenVPN:

    . /etc/openvpn/easy-rsa/2.0/vars
    . /etc/openvpn/easy-rsa/2.0/build-key client

You can remove client access:

    . /etc/openvpn/easy-rsa/2.0/vars
    . /etc/openvpn/easy-rsa/2.0/revoke-full client

After generating new client keys, you can read them all at once and
populate the .ovpn file:

    # python ovpn-gen client 123.456.78.90 1194

A client.ovpn file will then be created. Distribute this to your user
and they can connect to the VPN server.

[Tunnelblick](https://code.google.com/p/tunnelblick/) is an OS X client that
users can use to connect.

Windows and Linux users also have client programs that they can use too.

