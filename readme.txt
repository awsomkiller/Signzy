#Introduction

This project is demonstration of Remote operation of any system, this project is capable to operate command on linux machine remotely.
There are two file name server.py and client.py, the server.py file must be deployed over the remote system that needs to be controlled and
the client.py must be deployed on the system that we are accessing from.
This project is written in python language and tested on the latest version.

#Setup Guide
    1.Need to install an external library name rsa
        Installation methods :
            1. Using PIP
                pip install rsa
            2. using Git(in env)
                'git clone https://github.com/sybrenstuvel/python-rsa.git'
                cd python-rsa
                poetry install

    2. Check for the available port in the system and if default port is free you can use that, else change the ports in both the files

    3. Run the server.py file on remote system and note the ip address of the network

    4. change the server's IP address named host in client.py

    5. Now run the client.py file in the accessible system.

    6. To exit type exit in the command line


# Note : This project do not return Ack and NO Ack as it returns the actual output on remote system
i.e.  if you type ls command
      it will print the entire directory

# Current issues : it do not support sudo command as it requires password and it doesn't support immediate to provide immediate respond
    This project will work fine with all one line commands