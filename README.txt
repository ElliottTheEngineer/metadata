Wrote a program in Python.
Scrapes the XML now playing data out of the test.txt file at this location: \\10.0.17.10\NowPlaying

It then sends that data to HDVmixer in the following way:

# IP address and port to send the data
server_ip = "10.0.1.200"
server_port = 782

# Send data to the specified IP and port
PERFORMER_SEND = f"PERFORMER= {artist}\n"
TITLE_SEND = f"TITLE= {title}\n"
