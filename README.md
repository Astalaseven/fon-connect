fon-connect
===========

Connect easily to FON Belgacom Network!

## Installation

### Ubuntu

    sudo apt-get install git python-pip
    sudo pip install mechanize
    git clone https://github.com/Astalaseven/fon-connect.git

### ArchLinux

    sudo pacman -S git python2-pip     # or  yaourt -S git python2-pip
    sudo pip2 install mechanize
    git clone https://github.com/Astalaseven/fon-connect.git

## Usage

You need to enter your credentials:

    user_name = "user@belgacomfon.be"
    user_pass = "8_character_password"

Now you can use it with:

	cd fon-connect/ && python2 fon.py

Or you can put it in `/usr/bin`:

    sudo mv fon-connect/fon.py /usr/bin/fon

and launch it in a terminal through:

	~> fon
    Sending login...
    Connected to FON Network!