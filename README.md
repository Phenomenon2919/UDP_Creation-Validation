# UDP Creation and Validation
## UDP Creation
Given the following details:
1) Source IP
2) Source port
3) Destination IP
4) Destination port
5) Data to be transmitted
output the hexadecimal representation of of the UDP segment.

### Execution Syntax
$ python udp_create.py __SourceIPAddress__ __SourcePort__ __DestinationIPAddress__ __DestinationPort__ __DataInHexadecimalForm__

### Output
Hexidecimal hash Value
example: 115c270f000d3cae3132333435

## UDP Parsing and Validation

Given the hexadecimal representation of a segment, source IP and destination IP, validate it (using length field and checksum). If the segment is valid, output the following in this exact order:
1) Source port
2) Destination port
3) Length
4) Checksum
5) SHA256 hash of the segment data

else output “Invalid UDP segment”.

### Execution Syntax
$ python udp_parse.py __DataTransmitted__ __SourceIPAddress__ __DestinationIPAddress__

### Output

4444
9999
12
0xee3c
9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08