# `> Holiday // Contributing`
Thanks you for your interest in contributing. Please check out the [Code of Conduct](CODE_OF_CONDUCT.md) before contributing, thank you!

> [!IMPORTANT]
> This guide assume that you already installed Python 3.6 or higher.
> It is highly recommended to use Python version equal to or higher than the [minimum supported Python version](https://www.python.org/downloads/).

Running the script:

1. Clone the repository: `git@github.com:validcube/validcube.git && cd scripts/holiday`
2. Run the script: `python3 holiday.py`

Developing the script:

1. Install the required dependencies for development: `pip3 install -r dev-requirements.txt`
2. Lint check: `ruff .`
3. Static Analysis: `mypy .`
4. Test the script: `pytest`

> [!WARNING]
> Ruff is a linter made using Rust, it's super fast and doesn't output anything if everything passes, don't fall for it!
