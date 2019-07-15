from isso.compat import text_type
try:
    import ipaddress
except ImportError:
    import ipaddr as ipaddress


def anonymize(remote_addr):
    """
    Anonymize IPv4 and IPv6 :param remote_addr: to /24 (zero'd)
    and /48 (zero'd).

    """
    if not isinstance(remote_addr, text_type) and isinstance(remote_addr, str):
        remote_addr = remote_addr.decode('ascii', 'ignore')
    try:
        ipv4 = ipaddress.IPv4Address(remote_addr)
        return u''.join(ipv4.exploded.rsplit('.', 1)[0]) + '.' + '0'
    except ipaddress.AddressValueError:
        try:
            ipv6 = ipaddress.IPv6Address(remote_addr)
            if ipv6.ipv4_mapped is not None:
                return anonymize(text_type(ipv6.ipv4_mapped))
            return u'' + ipv6.exploded.rsplit(':', 5)[0] + ':' + ':'.join(['0000'] * 5)
        except ipaddress.AddressValueError:
            return u'0.0.0.0'
