# Triton
### Running `python 3.7.4`
Goal is to have all our code and datastores to in one single place for easy data analysis and tracking price evloution of different asset classes.

- `client` directory is where we get data from the different providers.
- `config` is where we hold the creds for connecting to the data providers
- `logs` is directory where we save our logs for debugging
- `industries` is dir that holds yaml files of "Company Name": "Stock Ticker" info.

### Setup
Clone this repo: `git clone https://github.com/Maxime93/triton.git`. This will create a new `triton` directory. `cd python`.

Install pyenv (python version management) to make sure we are all running the same python versions and dependencies: https://github.com/pyenv/pyenv#homebrew-on-macos (install with homebrew). `brew install pyenv`.

Then install python 3.7.4: `pyenv install 3.7.4`
Then install pyenv-virtualenv: `brew install pyenv-virtualenv`
Then create your triton virtualenv: `pyenv virtualenv 2.7.10 my-virtual-env-2.7.10`

You now have a virtual environement where you can run our python 3.7 code on!

Run `pyenv activate triton` and run `pip -r install requirements.txt` (if this is your first time).

Now run `python AlpacaPrices.py -q AAPL`, if you don't get an error you are good to go!

#### Workflow

[TODO]