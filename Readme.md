# Uptime Kuma Client README

## Description

The Uptime Kuma Client is a simple and intuitive GUI application for monitoring the online status of a specified IP address or domain. It also enables pushing notifications to a specified URL when the status changes. This tool is particularly useful for keeping track of server uptime and downtime.

## Features

- Monitor the online status of a specified IP address or domain.
- Automatically push notifications to a specified URL upon status change.
- Display the time of the last status change (online/offline).
- Save and load configuration settings.

## Requirements

- Python 3.x
- `tkinter` for the GUI.
- `requests` for HTTP requests.
- `subprocess` for executing system commands.
- `threading` for parallel processing.
- `datetime` and `time` for time handling.
- `json` for configuration file handling.
- `socket` for default IP retrieval.

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required Python modules:
   ```
   pip install requests
   ```
3. Clone or download this repository to your local machine.

## Usage

1. Run the script:
   ```
   python uptime_kuma_client.py
   ```
2. Enter the IP/Domain you want to monitor in the "IP/Domain" field.
3. Enter the URL for push notifications in the "Push URL" field.
4. Click "Save" to start monitoring.

## GUI Overview

- The application will display the current online/offline status with corresponding images.
- It shows the timestamp of when the monitored IP/Domain was first online and the time since it went offline.
- The configuration (IP/Domain and URL) can be saved for future use.

## Configuration File

The application saves the configuration in a `config.json` file. This file includes:
- `ip_address`: The IP or domain to monitor.
- `url`: The URL to push notifications to.

## Contributing

Contributions to the Uptime Kuma Client are welcome. Please open an issue or pull request on the repository.

## License

This project is open-sourced under the [MIT License](LICENSE).

## Author

Built with ❤️ by rdnsx

---
