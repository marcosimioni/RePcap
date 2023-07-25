# RePcap
Little helper utility to manipulate existing pcap files.

# Usage

Replace MAC addresses in a given pcap with:

```
python main.py -i input.pcap --mac 00:11:22:33:44:55 99:88:77:66:55:44 --output output.pcap
```

Source and Destination MAC address fields of every packet will be inspected, and `00:11:22:33:44:55` will be replaced with `99:88:77:66:55:44`.

Replace IP addresses in a given pcap with:

```
 python main.py -i input.pcap --ip 192.168.1.1 10.1.2.3 --output output.pcap       
```

Source and Destination IP address fields of every packet will be inspected, and `192.168.1.1` will be replaced with `10.1.2.3`.
