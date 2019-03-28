#!usr/bin/env python3
from os import getenv, chdir, environ, unsetenv
from os.path import isfile, isdir


def break_commandline():
	"""
	Break command line down into components and contain in list
	@ parameters:
	1. list[0]: command
	2. list[1]: arguments
	"""
	user_input = input()
	command_line = user_input.split(' ')
	return command_line


def back_to_home_directory():
	"""
	Change current working directory to home directory
	"""
	home_dir = getenv("HOME")
	chdir(home_dir)


def execute_cd(command_line):
	"""
	Built-ins command 'cd'
	cd [directory]
	"""

	# if command line is only 'cd'
	if len(command_line) == 1:
		back_to_home_directory()

	# execute command cd [directory]
	else:
		directory = command_line[1]

		# if arguments is a file
		if isfile(directory):
			print ("cd: " + directory + ": Not a directory")

		# if argument is a directory
		elif isdir(directory):
			chdir(directory)

		# if argument not exists
		else:
			print ("cd: " + directory + ": No such file or directory")


def execute_printenv(command_line):
	"""
	Built-ins command 'printenv'
	printenv [variable]
	"""

	# if no variable is input
	if len(command_line) == 1:
		for key in environ:
			print (key + '=' + environ[key])

	# execute command printenv [variable]
	else:
		variable = command_line[1]
		variable_env = getenv(variable)

		# if the environment of variable is not set
		if variable_env == None:
			pass

		# print variable environment
		else:
			print (variable_env)


def execute_export(command_line):
	"""
	Built-ins command 'export'
	export [variable=environment]
	"""

	# if no variable is input
	if len(command_line) == 1:
		pass

	# execute command export [variable=environment]
	else:
		argument = command_line[1].split('=')

		# if environment is not input to variable
		if len(argument) == 1:
			pass

		# set the environment for variable
		else:
			variable = argument[0]
			environment = argument[1]
			eviron[variable] = environment


def execute_unset(command_line):
	"""
	Built-ins command 'unset'
	unset [variable]
	"""

	# if no variable is input
	if len(command_line) == 1:
		pass

	# execute command unset [variable]
	else:
		try:
			variable = command_line[1]
			del environ[variable]
		except KeyError:
			pass


def execute_exit(command_line, flag):
	"""
	Built-ins command 'exit'
	exit [exit_code]
	"""

	# if too many arguments input
	if len(command_line) > 3:
		print ('bash: exit: too many arguments')

	# execute command exit [exit_code]
	else:
		argument = command_line[1]

		# if argument is a string
		if type(argument) == str:
			print ('bash: exit: argument is a string')

		# exit the bash shell
		else:
			flag = True
	return flag

def main():
	
while 1:
	command_line = break_commandline()
	execute_unset(command_line)
