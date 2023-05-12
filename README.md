# IoT-camera-project
Buffer and scripts to operate IoT, executed in raspberry pi shell whilst cameras are controlled by ESP32 micro processors

Generally speaking, this repository builds a software application to manage a raspberry PI's installation that centralizes pictures taken by ESP32 micro processors. This specific piece of hardware communicates with the ESPs through LAN and exports the information to cloud storage (primarily S3).

## Requirements

- Python >= 3.9.2
- Linux OS

## Installation

To install this application at the local raspberry, simply run the build script from the project's root directory:

```bash
sh ./.build/build.sh
```

## Running the application

To install this application at the local raspberry, simply run the run script from the project's root directory:

```bash
sh ./run.sh
```

## Caution
Note that every PR that will be delivered to the raspberry PCs must be delivered by CI/CD procedure only after making sure that queue-photo directory is completely empty.