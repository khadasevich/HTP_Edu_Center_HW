Write a module that will create a passwordless connection for a set of machines.

This means we need to generate an ssh key-pair and distribute it over all the machines supplied.

Mind the ability of automated clearing ssh key pairs from hosts. *Would be nice to have backup and restore functions.

The set of machine IPs should be taken from a config file nearby. Consider password and login are known in constants, or set in the config file.
