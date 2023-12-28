Python XML Data Scraper and Sender

Overview
  This program is designed to scrape XML data from a test.txt file and send it to HDVmixer. It reads the "now playing" data from a specified location and transmits it to a server.

How it Works
  Data Scraping: The program scrapes the XML data from the test.txt file.
  Data Sending: It then sends the scraped data to HDVmixer by connecting to a specified IP address and port.

File Location
  The test.txt file is located at \\10.0.17.10\NowPlaying.

Sending Data
  The data is sent to the HDVmixer in the following format:

    Performer: PERFORMER= {artist}
    Title: TITLE= {title}

Configuration
  Server IP: 10.0.1.200
  Server Port: 782

Usage
  Ensure the test.txt file is accessible at the given network path.
  Run the Python script.
  Data will be automatically scraped and sent to the configured server.

Dependencies
  Python (version 3.x or later)
  Network access to both the source file and HDVmixer server

Note
  Ensure network permissions and firewall settings are configured to allow the script to access the network path and send data to the server.
