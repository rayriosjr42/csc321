homework2

# 1 
# def get_interfaces():
    """Return a list of all the interfaces on this host

    Args: None

    Returns: (list) List of interfaces for this host
    """
# 192.168.178.140 is the ip configuration 

# 2
# def get_mac(interface: str):
    """For the given interface string, return the MAC address as a
    string

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (str) MAC address
    """
# 00-15-5D-38-01-00 , is the mac adress

# 3
# def get_ips(interface: str):
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 address objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('192.168.65.48'),
       'v6': ipaddress.IPv6Address('fe80::14e1:8686:e720:57a')}
    """
# ipv4 address- 192.168.178.140
# ipv6 local address- fe80::916c:b59d:c1b0:f26f%18

# 4
# def get_netmask(interface: str):
    """For the given interface string, return a dictionary with the
    IPv4 and IPv6 netmask objects (as IPv4/v6Address objects) for that
    interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('255.255.255.0'),
       'v6': ipaddress.IPv6Address('ffff:ffff:ffff:ffff::')}
    """
# ipv4 subnet mask- 255.255.240.0
# ipv6 subnet mask- n/a (no network access)

# 5
# def get_network(interface: str):
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 network objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Network('192.168.65.0/24'),
       'v6': ipaddress.IPv6Network('fe80::/64')}
    """
# ipv4 network- 192.168.176.1
# ipv6 network- n/a (no network access)