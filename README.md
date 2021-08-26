# Automated Valet Car Parking Backend

## Assumptions

-   Timestamp inside `input.txt` are always arranged in a chronologically manner (top-down)
-   There will only be two types of events input, i.e. `Enter` or `Exit`

## Design

-   [Observer Pattern](https://en.wikipedia.org/wiki/Observer_pattern)
-   With this design pattern, can easily perform additional operations such as sending a notification upon Vehicle entry, sends a Slack message, send information to our monitoring system etc. Making the system more extensible.

---

# Hosted Demo

1. Go to https://replit.com/@JerryNg1/automated-valet-car-parking-backend
2. Hit the "Play/Run" button.
3. Observer the output
4. Update `input.txt` accordingly
5. Hit the "Play/Run" button again.
6. Repeat.

---

# Local

## Requirement

This project uses **Python 3.9**. You may install Python 3.9 on Ubuntu 16.04 using the steps below:

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

We use [poetry](https://python-poetry.org/docs/) to manage our dependencies.

Though, there isn't any third party dependencies required for the project to work properly. We merely use `pre-commit`, `flake8`, and `autopep8` to improve code quality.

```sh
poetry install
pre-commit install
```

## Usage

0. Make sure you have Python3.9 installed on your local machine (see [Requirement](#requirement)].
1. Clone this repository.
2. Optional: Update `input.txt` accordingly.
3. Run the `python3 main.py`
4. Output will be printed in your terminal.

    ```sh
    # Example output in your terminal using the default `input.txt`.

    > python3 main.py
    Accept MotorcycleLot1
    Accept CarLot1
    MotorcycleLot1 2
    Accept CarLot2
    Accept CarLot3
    Reject
    CarLot3 6
    ```

---

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

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
