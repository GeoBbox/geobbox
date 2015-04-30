# geobbox box setup

## Pre-setup

Setup micro instance

### Create a security group

* Create a security group
* Add a rule to allow for port 22 - ssh to be opened up -- you will need this to log into the machine.
* Add this security group to the machine you have setup.

### Create a secret key

https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs

* Download and save.
* To use, you need to update permissions -- `chmod 400 mykey.pem`
* DO NOT CHECK IN :-O

### Create a user and download key

Here: https://console.aws.amazon.com/iam/home?#users

* DO NOT CHECK IN :-O
* This is used for S3 script


Setup S3 bucket

## Setup of EC2 instance

Login (note, we do not have a reserved IP address, so if the machine is stopped, you will need to go into the console to get the new IP address.)
```
ssh -i geobbox.pem ubuntu@52.4.89.249
```

Run the following commands...
```
sudo apt-get install git
mkdir geobbox
git clone https://github.com/GeoBbox/geobbox.git
sudo apt-get install python3-setuptools
sudo easy_install3 pip
sudo pip install virtualenv
sudo pip install virtualenvwrapper
```

Add virtualenv wrapper to your settings
```
touch ~/.bash_aliases
vim ~/.bash_aliases
```

Add the following to bash_aliases.
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/geobbox/geobbox
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

Then source the bashrc file to make sure that settings are loaded.
bashrc loads bash_aliases, which is why we source bashrc.
```
source ~/.bashrc
```

Set up virtualenv using python3. If python3 doesn't exist, then use the command (which python3) to identify the path.
```
mkvirtualenv geobbox --python=/usr/bin/python3
cd ~/geobbox/geobbox/code/
add2virtualenv .
```

Install requirements.
```
cd ~/geobbox/geobbox/code/
pip install -r requirements.txt
```

At this point, you should be able to run streamer.py.
```
cd ~/geobbox/geobbox/code/
python streaming.py
```

If you log in and you want to kick off the streaming script, you must activate the environment first. To do this, run the following BEFORE you run `python streaming.py`.
```
workon geobbox
```
