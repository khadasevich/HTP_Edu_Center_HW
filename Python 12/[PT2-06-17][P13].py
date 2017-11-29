#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for creation password less ssh session"""

import paramiko
import os
import subprocess
import json
from paramiko import client


class SshConnection(object):
    """Class for new connection"""
    client = None

    def __init__(self,
                 host=None,
                 user_name=None,
                 machine_port=None):
        print("Connecting to server.")
        self.host = host
        self.user_name = user_name
        self.machine_port = machine_port
        self.public_key_file = os.path.expanduser('~/.ssh/id_rsa.pub')
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(hostname=self.host,
                            username=self.user_name,
                            key_filename=self.public_key_file,
                            port=self.machine_port,
                            allow_agent=False,
                            look_for_keys=False)

    def send_command(self, command):
        """Sending commands to virtual machine"""
        if self.client:
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print data when available
                if stdout.channel.recv_ready():
                    all_data = stdout.channel.recv(1024)
                    prev_data = b"1"
                    while prev_data:
                        prev_data = stdout.channel.recv(1024)
                        all_data += prev_data
                    print(str(all_data))
        else:
            print("Connection not opened.")


class KeyDeploy(object):
    """This class deploys new key on virtual machine"""

    def __init__(self,
                 host=None,
                 user_name=None,
                 user_password=None,
                 machine_port=None,
                 public_key=None):
        """Constructor"""
        self.host = host
        self.user_name = user_name
        self.user_password = user_password
        self.machine_port = machine_port
        self.public_key = public_key
        self.public_key_file = os.path.expanduser('~/.ssh/id_rsa.pub')

    def deploy_key(self):
        """Deploys public key to remote machine"""
        with open(self.public_key_file) as key_file:
            self.public_key = key_file.readline()
        deploy_client = paramiko.SSHClient()
        deploy_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        deploy_client.connect(hostname=self.host,
                              username=self.user_name,
                              password=self.user_password,
                              port=self.machine_port,
                              allow_agent=False,
                              look_for_keys=False)
        deploy_client.exec_command('mkdir -p ~/.ssh/')
        deploy_client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % self.public_key)
        deploy_client.exec_command('chmod 644 ~/.ssh/authorized_keys')
        deploy_client.exec_command('chmod 700 ~/.ssh/')
        deploy_client.close()


class Configurator(object):
    """Class which opens configuration file and reads parameters"""

    def __init__(self,
                 host=None,
                 user_name=None,
                 user_password=None,
                 machine_port=None,
                 js=None):
        """Constructor of configuration parameters"""
        self.host = host
        self.user_name = user_name
        self.user_password = user_password
        self.machine_port = machine_port
        self.js = js

    def opening_con_file(self):
        """Reads configuration file"""
        with open('config_file.txt') as configure:
            self.js = json.load(configure)
            for key in self.js:
                conf_file = self.js[key]
                self.extract_data(conf_file)

    def extract_data(self, dictionary):
        """Extracts results of json"""
        self.host = dictionary['host']
        self.user_name = dictionary['auth_data']['user']
        self.user_password = dictionary['auth_data']['secret']
        self.machine_port = dictionary['auth_data']['port']
        key_deploy = KeyDeploy(self.host,
                               self.user_name,
                               self.user_password,
                               self.machine_port)
        key_deploy.deploy_key()


class KeysGenerator(object):
    """Creates new keys for connection"""

    def __init__(self):
        """Constructor of new connection"""
        self.public_key_file = os.path.expanduser('~/.ssh/id_rsa.pub')

    def keys_generation(self):
        """Creates pair of keys for connection"""
        if os.path.exists(self.public_key_file) is False or os.stat(self.public_key_file).st_size == 0:
            process = subprocess.Popen('ssh-keygen')
            process.wait()
        else:
            print ("The pair of keys is already created.")


class KeyRemover(object):
    """This class allows to remove keys from virtual machine"""

    def __init__(self,
                 host=None,
                 user_name=None,
                 user_password=None,
                 machine_port=None,
                 js=None):
        """Constructor of configuration parameters"""
        self.host = host
        self.user_name = user_name
        self.user_password = user_password
        self.machine_port = machine_port
        self.js = js

    def opening_con_file(self):
        """Reads configuration file"""
        with open('config_file.txt') as configure:
            self.js = json.load(configure)
            for key in self.js:
                conf_file = self.js[key]
                self.extract_data(conf_file)

    def extract_data(self, dictionary):
        """Extracts results of json"""
        self.host = dictionary['host']
        self.user_name = dictionary['auth_data']['user']
        self.user_password = dictionary['auth_data']['secret']
        self.machine_port = dictionary['auth_data']['port']
        self.removing_created_keys()

    def removing_created_keys(self):
        """Removes created keys"""
        removing_client = paramiko.SSHClient()
        removing_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        removing_client.connect(hostname=self.host,
                                username=self.user_name,
                                password=self.user_password,
                                port=self.machine_port,
                                allow_agent=False,
                                look_for_keys=False)
        removing_client.exec_command('rm ~/.ssh/authorized_keys')
        removing_client.close()


class BackUp(object):
    """This class allows to save keys"""

    def __init__(self,
                 recovered_key=None,
                 public_key=None):
        """Constructor"""
        self.recovered_key = recovered_key
        self.public_key_file = os.path.expanduser('~/.ssh/id_rsa.pub')
        self.public_key = public_key

    def back_up(self):
        """Back-up of removed keys"""
        with open(self.public_key_file) as public:
            self.public_key = public.readline()
        configuration_reset = Configurator()
        configuration_reset.opening_con_file()


if __name__ == '__main__':
    keys_generator = KeysGenerator()
    keys_generator.keys_generation()
    configuration = Configurator()
    configuration.opening_con_file()
    ssh = SshConnection(configuration.host,
                        configuration.user_name,
                        configuration.machine_port)
    ssh.send_command("mkdir testfolder")
