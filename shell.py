#!usr/bin/env python3
from os import getenv, chdir, environ, unsetenv, getcwd
from os.path import isfile, isdir, abspath
from path_expansions import handle_tilde_expansion

def break_commandline():
	"""
	Break command line down into components and contain in list.
	@ parameters:
	1. list[0]: command.
	2. list[1]: arguments.
	"""
	user_input = input()
	command_line = user_input.split()
	return command_line


def back_to_home_directory():
	"""
	Change current working directory to home directory.
	"""
	home_dir = getenv("HOME")
	if home_dir is None:
		print('intek-sh$: cd: HOME not set')
	else:
		chdir(home_dir)


def update_pwd(directory):
	current_directory = getcwd()
	environ['OLDPWD'] = current_directory
	environ['PWD'] = directory


def execute_cd(command_line):
	"""
	Built-ins command 'cd'
	cd [directory]
	"""

	try:

		# if command line is only 'cd'
		if len(command_line) == 1:
			update_pwd(getenv("HOME"))
			back_to_home_directory()

		# execute command cd [directory]
		else:
			directory = command_line[1]
			directory = handle_tilde_expansion(directory)

			# if arguments is a file
			if isfile(directory):
				print ("intek-sh$: cd: " + directory + ": Not a directory")

			# if argument is a directory
			elif isdir(directory):
				update_pwd(abspath(directory))
				chdir(directory)

			# if argument not exists
			else:
				print ("intek-sh$: cd: " + directory + ": No such file or directory")
	except EOFError:
		pass

def execute_pwd(command_line):
	try:
		current_directory = getcwd()
		print(current_directory)
	except EOFError:
		pass


def execute_printenv(command_line):
	"""
	Built-ins command 'printenv'
	printenv [variable]
	"""

	try:

		# if no variable is input
		if len(command_line) == 1:
			for key in environ:
				print(key + '=' + environ[key])

		# execute command printenv [variable]
		else:
			variable = command_line[1]
			variable_env = getenv(variable)

			# if the environment of variable is not set
			if variable_env is None:
				pass

			# print variable environment
			else:
				print(variable_env)
	except EOFError:
		pass


def execute_export(command_line):
	"""
	Built-ins command 'export'
	export [variable=environment]
	"""

	try:

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
				environ[variable] = environment
	except EOFError:
		pass


def execute_unset(command_line):
	"""
	Built-ins command 'unset'
	unset [variable]
	"""

	try:

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
	except EOFError:
		pass


def execute_exit(command_line, flag):
	"""
	Built-ins command 'exit'
	exit [exit_code]
	"""

	try:

		# if too many arguments input
		if len(command_line) > 2:
			print ('intek-sh$: exit: too many arguments')

		# if no exit_code is input
		elif len(command_line) == 1:
			print ('exit')
			flag = False

		# exit with exit_code
		else:
			argument = command_line[1]

			# if argument is a numeric string
			if argument.isdigit():
				print('exit')

			# if argument is a string
			else:
				print('intek-sh$: exit: ' + argument + ': numeric argument required')
			flag = False
		return flag
	except EOFError:
		pass


def main():
	flag = True
	while flag:
		print('intek-sh$ ', end='')
		command_line = break_commandline()
		if len(command_line) > 0:
			command = command_line[0]
			if command == 'pwd':
				execute_pwd(command_line)
			elif command == 'cd':
				execute_cd(command_line)
			elif command == 'printenv':
				execute_printenv(command_line)
			elif command == 'export':
				execute_export(command_line)
			elif command == 'unset':
				execute_unset(command_line)
			elif command == 'exit':
				flag = execute_exit(command_line, flag)
			else:
				print('intek-sh$: ' + command + ': command not found')
		else:
			pass


main()
