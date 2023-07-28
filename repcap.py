# ReCap v1.0
#
import argparse

from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether
from scapy.utils import PcapWriter

DEBUG = False
if DEBUG:
    print("!!! RUNNING IN DEBUG MODE !!!")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='ReCap',
        description='Little helper utility to manipulate existing pcap files.')

    parser.add_argument(
        '-i',
        '--input',
        help='Input pcap file.',
    )

    parser.add_argument(
        '-o',
        '--output',
        help='Output pcap file.',
    )

    parser.add_argument(
        '-mac',
        '--mac',
        nargs=2,
        help='Replace every mac_orig occurrence with mac_repl, regardless of it being src or dst.',
    )

    parser.add_argument(
        '-ip',
        '--ip',
        nargs=2,
        help='Replace every ip_orig occurrence with ip_repl, regardless of it being src or dst.',
    )

    if DEBUG:
        from collections import namedtuple
        Args = namedtuple('Args', ['input', 'output', 'ip', 'mac'])
        args = Args(input='input.pcap',
                    output='output.pcap',
                    ip=['192.168.1.100', '10.1.1.100'],
                    mac=['00:11:22:33:44:55', '11:22:33:44:55:66'])
    else:
        if len(sys.argv) == 1:
            parser.print_help(sys.stderr)
            sys.exit(1)

        args = parser.parse_args()
        print("Args:")
        print(args)

        if 'input' not in args:
            parser.print_help(sys.stderr)
            print("\nPlease specify an input file.\n", file=sys.stderr)
            sys.exit(1)

        if 'output' not in args:
            parser.print_help(sys.stderr)
            print("\nPlease specify an output file.\n", file=sys.stderr)
            sys.exit(1)

    if DEBUG:
        print(args)

    print("Reading {}...".format(args.input))

    packets = rdpcap(args.input)

    for p in packets:
        if DEBUG:
            print(p)

        if 'mac' in args and args.mac:
            # Replace source MAC, if it matches
            if DEBUG:
                print(p[Ether].src)
            if p[Ether].src == args.mac[0]:
                print("Found {} as source MAC, replacing with {}...".format(args.mac[0], args.mac[1]))
                p[Ether].src = args.mac[1]

            # Replace destination MAC, if it matches
            if DEBUG:
                print(p[Ether].dst)
            if p[Ether].dst == args.mac[0]:
                print("Found {} as destination MAC, replacing with {}...".format(args.mac[0], args.mac[1]))
                p[Ether].dst = args.mac[1]

        if 'ip' in args and args.ip:
            # Replace source IP, if it matches
            if DEBUG:
                print(p[IP].src)
            if p[IP].src == args.ip[0]:
                print("Found {} as source ip, replacing with {}...".format(args.ip[0], args.ip[1]))
                p[IP].src = args.ip[1]

            # Replace destination IP, if it matches
            if DEBUG:
                print(p[IP].dst)
            if p[IP].dst == args.ip[0]:
                print("Found {} as destination ip, replacing with {}...".format(args.ip[0], args.ip[1]))
                p[IP].dst = args.ip[1]

    print("Writing to {}...".format(args.output))
    wrpcap(args.output, packets)

    print("Job done!")

    sys.exit(0)

