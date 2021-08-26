# Automated Valet Car Parking Backend

## Assumptions

-   Timestamp inside `input.txt` are always arranged in a chronologically manner (top-down)
-   There will only be two types of events input, i.e. `Enter` or `Exit`

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

1. Update `input.txt` accordingly.
2. Run the `python3 main.py`

---

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change

## Setup Pre-commit Hooks

Before you begin your development work, make sure you have installed [pre-commit hooks](https://pre-commit.com/index.html#installation).

Some example useful invocations:

-   `pre-commit install`: Default invocation. Installs the pre-commit script alongside any existing git hooks.
-   `pre-commit install --install-hooks --overwrite`: Idempotently replaces existing git hook scripts with pre-commit, and also installs hook environments

## Steps

1. Fork this
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
