#!/usr/bin/env python3

import socket
import sys
import csv
import json
import argparse
import concurrent.futures
import tqdm
import logging
from dns import resolver, reversename

def setup_logging(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def resolve_ip(ip_address, dns_server=None, timeout=2, reverse=False):
    try:
        if reverse:
            addr = reversename.from_address(ip_address)
            if dns_server:
                custom_resolver = resolver.Resolver(configure=False)
                custom_resolver.nameservers = [dns_server]
                answers = custom_resolver.resolve(addr, 'PTR', lifetime=timeout)
            else:
                answers = resolver.resolve(addr, 'PTR', lifetime=timeout)
            return str(answers[0])
        else:
            if dns_server:
                socket.setdefaulttimeout(timeout)
                return socket.gethostbyaddr(ip_address)[0]
            else:
                return socket.gethostbyname_ex(ip_address)[0]
    except (socket.herror, socket.gaierror, resolver.NXDOMAIN, resolver.Timeout) as e:
        logging.debug(f"Failed to resolve {ip_address}: {str(e)}")
        return "Unknown"

def process_batch(batch, dns_server, timeout, reverse):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_ip = {executor.submit(resolve_ip, ip, dns_server, timeout, reverse): ip for ip in batch}
        for future in concurrent.futures.as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                hostname = future.result()
                results.append((ip, hostname))
            except Exception as exc:
                logging.error(f'{ip} generated an exception: {exc}')
    return results

def main(args):
    setup_logging(args.verbose)
    
    with open(args.input_file, 'r') as input_f:
        addresses = [line.strip() for line in input_f if line.strip()]

    results = []
    batch_size = args.batch_size
    for i in tqdm.tqdm(range(0, len(addresses), batch_size), desc="Processing batches"):
        batch = addresses[i:i+batch_size]
        results.extend(process_batch(batch, args.dns_server, args.timeout, args.reverse))

    if args.output_format == 'csv':
        with open(args.output_file, 'w', newline='') as output_f:
            writer = csv.writer(output_f)
            writer.writerow(['Address', 'Resolution'])
            writer.writerows(results)
    elif args.output_format == 'json':
        with open(args.output_file, 'w') as output_f:
            json.dump([{'address': ip, 'resolution': hostname} for ip, hostname in results], output_f, indent=2)
    else:  # plain text
        with open(args.output_file, 'w') as output_f:
            for ip, hostname in results:
                output_f.write(f"{ip}: {hostname}\n")

    logging.info(f"Results written to {args.output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resolve IP addresses or hostnames")
    parser.add_argument("input_file", help="Input file containing IP addresses or hostnames")
    parser.add_argument("output_file", help="Output file for results")
    parser.add_argument("--dns-server", help="Custom DNS server to use for lookups")
    parser.add_argument("--timeout", type=int, default=2, help="Timeout for each lookup in seconds")
    parser.add_argument("--batch-size", type=int, default=100, help="Number of addresses to process in each batch")
    parser.add_argument("--output-format", choices=['csv', 'json', 'txt'], default='csv', help="Output file format")
    parser.add_argument("--reverse", action="store_true", help="Perform reverse DNS lookup")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    
    args = parser.parse_args()
    main(args)
