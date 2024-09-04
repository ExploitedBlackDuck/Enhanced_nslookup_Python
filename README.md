# Enhanced DNS Resolution Script

## Overview

This Python script performs DNS resolution for a list of IP addresses or hostnames. It supports both forward and reverse DNS lookups, concurrent processing for improved performance, and various output formats.

## Features

- Concurrent processing of DNS lookups
- Support for both forward and reverse DNS lookups
- Custom DNS server specification
- Configurable timeout for lookups
- Batch processing for large input files
- Multiple output formats (CSV, JSON, plain text)
- Progress bar for visual feedback
- Verbose logging option for debugging

## Prerequisites

- Python 3.6 or later
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository or download the script.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line with various options:

```bash
python dns_resolver.py input_file output_file [options]
```

### Arguments:

- `input_file`: Path to the input file containing IP addresses or hostnames (one per line)
- `output_file`: Path to the output file for results

### Options:

- `--dns-server DNS_SERVER`: Specify a custom DNS server for lookups
- `--timeout TIMEOUT`: Set the timeout for each lookup in seconds (default: 2)
- `--batch-size BATCH_SIZE`: Number of addresses to process in each batch (default: 100)
- `--output-format {csv,json,txt}`: Choose the output file format (default: csv)
- `--reverse`: Perform reverse DNS lookup (hostname to IP)
- `--verbose`: Enable verbose logging for debugging

### Example:

```bash
python dns_resolver.py addresses.txt results.json --dns-server 8.8.8.8 --timeout 3 --batch-size 200 --output-format json --reverse --verbose
```

## Input File Format

The input file should contain one IP address or hostname per line. For example:

```
192.168.1.1
google.com
10.0.0.1
example.org
```

## Output

The script will generate an output file in the specified format (CSV, JSON, or plain text) containing the results of the DNS lookups.

## Error Handling

- The script logs errors and continues processing if individual lookups fail.
- Use the `--verbose` option for detailed logging of errors and debugging information.

## Performance

The script uses concurrent processing to improve performance when dealing with a large number of entries. Adjust the `--batch-size` option to optimize for your system's capabilities.

## Contributing

Contributions to improve the script are welcome. Please submit a pull request or open an issue to discuss proposed changes.

## License

[Specify the license under which this script is distributed]
