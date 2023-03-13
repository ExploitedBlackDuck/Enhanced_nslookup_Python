# automated-nslookup

This Python script reads IP addresses from a file, uses the socket module to attempt to resolve the IP addresses to hostnames, and writes the results to another file.

The script first specifies the name of the source file and the output file, which should be customized to match the filenames and paths of the actual files being used. It then opens the source file in read mode and the output file in append mode, using the with statement to ensure that the files are properly closed when the code block is finished executing.

Next, the script reads all of the IP addresses in the source file using the readlines() method, which returns a list of strings containing each line of the file. The script then loops over each IP address in the list, stripping off any newline characters that may be present using the strip() method.

Inside the loop, the script attempts to resolve the IP address to a hostname using the gethostbyaddr() method of the socket module. If the resolution is successful, the script prints the IP address and the resolved hostname to the console and writes them to the output file in comma-separated format. If the resolution is not successful, the script writes the IP address and the string "Unknown" to the output file and prints an error message to the console.

Note that the script may take some time to execute, especially if many IP addresses are being resolved, and may generate errors or produce unexpected results if the input file contains malformed or invalid IP addresses.
