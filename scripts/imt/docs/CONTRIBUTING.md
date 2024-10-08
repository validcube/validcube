# `> Image // Contributing`
Thanks you for your interest in contributing. Please check out the [Code of Conduct](CODE_OF_CONDUCT.md) before contributing, thank you!

> [!IMPORTANT]
> This guide assume that you already installed Python 3.9 or higher.

Running the script:

1. Clone the repository: `git@github.com:validcube/validcube.git && cd scripts`
2. Install the required dependencies: `pip3 install -r requirements.txt`
3. Run the script: `python3 convert_now.py`

Developing the script:

1. Move into scripts directory: `cd scripts`
2. Install the required dependencies for development: `pip3 install -r dev-requirements.txt`
3. Lint check: `ruff .`
4. Static Analysis: `mypy .`
5. Test the script: `pytest`

> [!WARNING]
> Ruff is a linter made using Rust, it's super fast and doesn't output anything if everything passes, don't fall for it!

## `/> Testing`
Testing fail? See [Testing documentation](Test.md).
