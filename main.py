# ReCap v1.0
#
import argparse

from scapy.all import *
from scapy.layers.inet import IP
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
        '-ip',
        '--ip',
        nargs=2,
        help='Replace every ip_orig occurrence with ip_repl, regardless of it being src or dst.',
    )

    if DEBUG:
        from collections import namedtuple
        Args = namedtuple('Args', ['input', 'output', 'ip'])
        args = Args(input='input.pcap', output='output.pcap', ip=['192.168.1.100', '10.1.1.100'])
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

    print("Writing to {}...".format(args.output))
    wrpcap(args.output, packets)

    print("Job done!")

    sys.exit(0)

