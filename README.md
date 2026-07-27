# Fawry-N2-Assessment
# QuRadar

## Overview

The project is designed to demonstrate the use of core OOP principles in Python.

## OOP Concepts Used

* **Abstraction** – Implemented using an abstract `Rule` base class.
* **Inheritance** – Traffic rules inherit from the `Rule` class.
* **Polymorphism** – The radar processes all rules through the common `check()` interface.
* **Encapsulation** – Classes manage their own data and behavior.
* **Composition** – A `Fine` contains one or more `Violation` objects.

## Project Structure

```text
project/
│
├── main.py             # Runs the application
├── quant_radar.py      # QuRadar processing engine
├── rules               # Traffic rule implementations
├── models              # Data models (Observation, Violation, Fine)
└── README.md
```

## Running the Project

Run the application with:

```bash
python main.py
```

