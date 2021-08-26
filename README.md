# Automated Valet Car Parking Backend

## Requirement

This project uses Python3.9. You may install Python3.9 on Ubuntu 16.04 using the steps below:

```sh
# 1. Update the apt package list
apt-get update

# 2. Refresh local apt keys from Ubuntu key server
apt-key adv --refresh-keys --keyserver keyserver.ubuntu.com

# 3. Install software-properties-common to be able to add 3rd party repositories to apt
apt-get -y install software-properties-common

# 4. Add deadsnakes repository to apt, then run update
add-apt-repository ppa:deadsnakes/ppa
apt get update

# 5. Now that apt is ready, install python3.9
apt-get -y install python3.9
```

## Installation (Optional)

This step is required only for local development to ensure code quality.

```sh
poetry install
pre-commit install
```

## Usage

```sh
python3 main.py
```
