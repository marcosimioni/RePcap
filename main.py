# ReCap v1.0
#
import argparse
import sys

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='ReCap',
        description='Little helper utility to manipulate existing pcap files.')

    parser.add_argument(
        '-i',
        '--input',
        nargs=1,
        metavar='input_file',
        help='Input pcap file.',
    )

    parser.add_argument(
        '-o',
        '--output',
        nargs=1,
        metavar='output_file',
        help='Output pcap file.',
    )

    parser.add_argument(
        '--ip',
        nargs=2,
        metavar=('ip_orig', 'ip_repl'),
        help='Replace every ip_orig occurrence with ip_repl, regardless of it being src or dst.',
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

