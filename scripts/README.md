# `> Image_manipulation`
Python script that's mostly used for image manipulation

| Python version | Support status                               |
| -------------- | -------------------------------------------- |
| 3.13           | ❌ Best effort if the dependency is ready    |
| 3.12           | ✅ Supported                                 |
| 3.11           | ✅ Supported                                 |
| 3.10           | ✅ Supported                                 |
| 3.9            | ✅ Supported                                 |
| 3.8            | ⚙️ Best effort                               |
| =<3.7          | ❌ Not Supported                             |

## `> Image // Contributing`

Thanks for consider contributing.
> [!IMPORTANT]  
> This guide assume that you already installed Python 3.9 or higher and pytest.

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

Here are some tip when contributing:
* All commits must follows the [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) guidelines.
* [Signing commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) are **required**.
* This repository follows slight variation of [Google's Python style](https://google.github.io/styleguide/pyguide.html) guide **but not strictly enforced**.
