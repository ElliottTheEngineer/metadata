import xml.etree.ElementTree as ET
import time
import socket
from datetime import datetime

# File path on the network machine
file_path = r"\\10.0.17.10\NowPlaying\test.txt"

# Path to store metadata in a local file
local_file_path = r"C:\ElliottLog\MetaData.txt"

# IP address and port to send the data
server_ip = "10.0.1.200"
server_port = 782

# Initialize variables to store previous data
previous_data = None

# Socket setup for sending data
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Continuous loop to keep checking for updates
while True:
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            xml_data = file.read().strip()  # Strip leading/trailing whitespace

        # Parse the XML data
        root = ET.fromstring(xml_data)

        # Access 'nowplaying' directly, assuming it's the root element
        nowplaying = root

        # Check if 'nowplaying' element is present
        if nowplaying is not None:
            # Extract 'artist' and 'title' from 'nowplaying' element
            artist = nowplaying.find("artist").text.strip()
            title = nowplaying.find("title").text.strip()

            # Create a tuple with the current data
            current_data = (artist, title)

            # Check if the data has changed since the last iteration
            if current_data != previous_data:
                # Get current date and time
                current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Append the extracted information with date and time to the local file
                with open(local_file_path, 'a') as output_file:
                    output_file.write(f"Date and Time: {current_datetime}\n")
                    output_file.write(f"Artist: {artist}\n")
                    output_file.write(f"Title: {title}\n")
                    output_file.write("\n")  # Add a new line for separation

                # Send data to the specified IP and port
                PERFORMER_SEND = f"PERFORMER= {artist}\n"
                TITLE_SEND = f"TITLE= {title}\n"
                s.sendto(PERFORMER_SEND.encode(), (server_ip, server_port))
                s.sendto(TITLE_SEND.encode(), (server_ip, server_port))

                # Update the previous data to the current data
                previous_data = current_data
        else:
            # Append error message to the local file if 'nowplaying' element is not found
            with open(local_file_path, 'a') as output_file:
                output_file.write("No 'nowplaying' element found in the XML.\n")
                output_file.write("\n")  # Add a new line for separation
    except FileNotFoundError:
        # Append error message to the local file if the file is not found
        with open(local_file_path, 'a') as output_file:
            output_file.write(f"Error: File not found at {file_path}\n")
            output_file.write("\n")  # Add a new line for separation
    except ET.ParseError as e:
        # Append error message to the local file if there's a parsing error
        with open(local_file_path, 'a') as output_file:
            output_file.write(f"Error parsing XML: {e}\n")
            output_file.write("\n")  # Add a new line for separation
    except Exception as e:
        # Append any unexpected error to the local file
        with open(local_file_path, 'a') as output_file:
            output_file.write(f"Unexpected error: {e}\n")
            output_file.write("\n")  # Add a new line for separation

    # Wait for 5 seconds before checking again
    time.sleep(5)
