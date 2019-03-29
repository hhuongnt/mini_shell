#!usr/bin/env python3
from os import getenv, chdir, environ, unsetenv, getcwd
from os.path import isfile, isdir


def break_commandline():
	"""
	Break command line down into components and contain in list.
	@ parameters:
	1. list[0]: command.
	2. list[1]: arguments.
	"""
	user_input = input()
	command_line = set(user_input.split(' '))
	return command_line


def back_to_home_directory():
	"""
	Change current working directory to home directory.
	"""
	home_dir = getenv("HOME")
	chdir(home_dir)


def is_string(argument):
	"""
	Check if argument is a string or a number.
	If string -> return True else return False.
	"""
	num = '123456789'
	for i in argument:
		if i not in num:
			return True
	return False


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
			print ("intek-sh$: cd: " + directory + ": Not a directory")

		# if argument is a directory
		elif isdir(directory):
			chdir(directory)

		# if argument not exists
		else:
			print ("intek-sh$: cd: " + directory + ": No such file or directory")


def execute_pwd(command_line):
	current_directory = getcwd()
	print (current_directory)


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
			environ[variable] = environment


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
	if len(command_line) > 2:
		print ('intek-sh$: exit: too many arguments')

	# execute command exit [exit_code]
	elif len(command_line) == 1:
		print ('exit')
		flag = True
	else:
		argument = command_line[1]

		# if argument is a string
		if is_string(argument):
			print ('intek-sh$: exit: ' + argument + ': numeric argument required')

		# if argument is [exit_code]: change flag -> True to end while loop
		else:
			print ('exit')
			flag = True
	return flag


def main():
	flag = False
	while flag == False:
		print ('intek-sh$ ', end='')
		command_line = break_commandline()
		if len(command_line) > 0:

			# code here pls
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
				print ('intek-sh$: ' + command + ': command not found')
		else:
			pass


main()
