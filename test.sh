#!/usr/bin/env bash

# As of now, we are not able to run our test suite using `python3 -m unittest` as we're checking the stdout.
# We are not able to clear out stdout right after each individual test, resulting in stdout overlapping each individual test.
# This resulted in a False-negative in our test suite when being run in the same process.
# This bash script is created so that we can easily run our test individually.

python3 -m unittest -k test_parse_input_file_returns_a_list_of_events
python3 -m unittest -k test_event_handler_default
python3 -m unittest -k test_event_handler_when_no_car_parking_lot
python3 -m unittest -k test_event_handler_when_no_motorcycle_parking_lot
