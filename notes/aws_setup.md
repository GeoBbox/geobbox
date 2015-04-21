# geobbox box setup

## In console

Setup micro instance

Setup S3 bucket

## Setup of EC2 instance

Login:
`ssh -i geobbox.pem ubuntu@52.6.36.180`

`
sudo apt-get install git
git clone git@github.com:GeoBbox/geobbox.git
sudo apt-get install python3-setuptools
sudo easy_install3 pip
sudo pip install virtualenv
sudo pip install virtualenvwrapper
`

Setup virtualenv
`
touch ~/.bash_aliases
vim ~/.bash_aliases
`

Add the following to bash_aliases.
`
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/geobbox/geobbox
source /usr/local/bin/virtualenvwrapper.sh
`

Then source the bashrc file to make sure that settings are loaded.
bashrc loads bash_aliases, which is why we source bashrc.
`
source ~/.bashrc
`

If you get error, then run the following...
`
sudo pip install virtualenvwrapper
`
else, just continue.

Set up virtualenv using python3. If python3 doesn't exist, then use the command (which python3) to identify the path.
`
mkvirtualenv geobbox --python=/usr/bin/python3
cd ~/geobbox/geobbox/code/
add2virtualenv .
`


