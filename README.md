# Triton

### TODO

| Feature | Description |
| --- | --- |
| Coinbase Client | Add Coinbase REST Client |
| Bistamp Client | Add Bitstamp REST Client |
| Quandl Client | Add Bitstamp REST Client: https://docs.quandl.com/docs/python-installation
| Email Alert Module | Make a function in Utils.py that takes list of emails and some text as inputs, and send the text to these email addresses as output
| Asset tracker | New script in the root folder takes as input the a client list (list of clients where you own some assets) gets all these clients, gets you current positions and computes your profits (price bought - current price)
| Industries | Make list of all relevant companies and their tickers in the appropriate files in the industries folder
| Industry tracker | New script that gets all tickers in industry dir, gets their prices, and compute aggregate price per industry. Time span should be a param, as well as time aggregation (minute, hour, day, week, month). Goal is to be able to study the variations of an industry over time.
| Price variation | New script in root dir that outputs top 20 tickers with highest price variation in the past 24h (timespan should be a param)
| Price volatility| New script in root dir that outputs top 20 tickers with highest price volatility in the past 24h (timespan should be a param - this could be in the same script as above)
| Tests | Write tests for all scripts and clients

### Running `python 3.7.4`
Goal is to have all our code and datastores to in one single place for easy data analysis and tracking price evloution of different asset classes.

- `client` directory is where we get data from the different providers.
- `config` is where we hold the creds for connecting to the data providers
- `logs` is directory where we save our logs for debugging
- `industries` is dir that holds yaml files of "Company Name": "Stock Ticker" info.

### Setup
Fork this repo: `git clone https://github.com/Maxime93/triton.git`, then clone it to your user. This will create a new `triton` repo for your user.
Clone your `triton` on you local machine.

Install pyenv (python version management) to make sure we are all running the same python versions and dependencies: https://github.com/pyenv/pyenv#homebrew-on-macos (install with homebrew). `brew install pyenv`. If you don't have homebrew, install it before: https://brew.sh

Then install python 3.7.4: `pyenv install 3.7.4`
Then install pyenv-virtualenv: `brew install pyenv-virtualenv`.
Once the is complete you need to copy paste the two lines below in your terminal profile
```
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
You only have to do the above once (refer to doc https://github.com/pyenv/pyenv-virtualenv)

Then create your triton virtualenv: `pyenv virtualenv 3.7.4 triton`. Now before running any triton script on your machine, make sure to `pyenv activate triton` which activates the virtual env.

First time setting up the virtualenv? You need to install all the necessary libraries as such: `pip install -r requirements.txt` (make sure you are in the triton repo).

You now have a virtual environement where you can run our triton python 3.7 code on!

You need to set up your config files in the `configs` dir. Every user had different trading account connection credentials that are never pushed online.
For Alpaca.yml, structure is the below:
```
Alpaca:
  Live:
    base_route: https://api.alpaca.markets
    api_key: <your-api-key>
    secret_key: <your-secret-key>
  Paper:
    base_route: https://paper-api.alpaca.markets
    api_key: <your-api-key>
    secret_key: <your-secret-key>
```
Refer to the `README.md` doc in configs dir to know how to format configs for the different clients!

Now run `python Demo.py -t AAPL`, if you don't get an error you are good to go!

### Workflow

This is the required workflow when making changes to code, or adding features to the library.
First thing: `git fetch upstream master` & `git rebase upstream/master` to make sure you have the latest code locally.

1. Make sure you have the correct remote repos set up:
`git remote -v` should output four lines:
--> Two origins, pointing to your fork
--> Two upstreams, pointing to https://github.com/Maxime93/triton.git
If you don't have the upstream: `git add upstream https://github.com/Maxime93/triton.git`

2. Create a new branch `git checkout -b newFeature`.
3. Code your implementation.
4. Once done (and tested), push you new branch tou your fork: `git push origin newFeature`
5. Submit a PR though to the upstream repo (Maxime93/triton) in the github Website.
6. Once PR is merged do `git fetch upstream master` then `git rebase upstream/master` then `git push origin master`