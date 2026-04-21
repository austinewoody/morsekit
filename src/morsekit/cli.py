from __future__ import annotations

import argparse
from .morse import encode, decode


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="morsekit",
        description="Encode and decode Morse code"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    encode_parser = subparsers.add_parser("encode", help="Encode text to Morse code")
    encode_parser.add_argument("text", help="Text to encode")

    decode_parser = subparsers.add_parser("decode", help="Decode Morse code to text")
    decode_parser.add_argument("text", help="Morse code to decode")

    args = parser.parse_args()

    if args.command == "encode":
        print(encode(args.text))
    elif args.command == "decode":
        print(decode(args.text))


if __name__ == "__main__":
    main()