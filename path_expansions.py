# from shell import back_to_home_directory
from os import getenv, path


def handle_tilde_expansion(dest_path):
	"""
	Handle the tilde expansion cases
	Return the right destination path after handling the cases
	"""

    # handle tilde expansion
	if dest_path[0] == '~':
		home_dir = getenv("HOME")

		# if destination path is '~'
		if len(dest_path) == 1:
			dest_path = home_dir
			return dest_path

		# destination path is set
		else:
			dest_path = dest_path[1:]

			# if destination path is '+'
			if dest_path[0] == '+':
				dest_path = getenv("PWD")
				return dest_path

			# if destination path is '-'
			elif dest_path[0] == '-':
				dest_path = getenv("OLDPWD")
				return dest_path

			# return the final directory after handling tilde expansion
			else:
				if dest_path[0] == '/':
					dest_path = home_dir + dest_path
					return dest_path
				return '~' + dest_path

    # command input not a tilde expansion
	return dest_path


def create_dict(command_line, dict):
	if '=' in command_line:
		for i in range(len(command_line)):
			if command_line[i] == '=':
				break
		key = command_line[:i]
		value = command_line[i+1:]
		dict[key] = value
		return dict
	else:
		pass


def handle_parameter_expansion(dest_path, dict):
	if dest_path[0] == '$':

		# if expression is empty
		if len(dest_path) == 1:
			return '$'

		# handle expression
		else:

			# handle braces '{}'
			if dest_path[1] == '{':
				var = ''

				# trace the variable in the braces
				for char in dest_path[2:]:
					if char == '}':
						break
					var += char

				# if variable is already set
				if var in dict.keys():
					return dict[var]

				# if variable is not set
				return ''

			# without braces '{}'
			else:
				dest_path = dest_path[1:]

				# if variable is already set
				if dest_path in dict.keys():
					return dict[dest_path]

				# if variable is not set
				else:
					return ''
	else:
		return ''


def main():
	dict = {}
	while 1:
		command_line = input()
		if command_line[0] != '$':
			dict = create_dict(command_line, dict)
		else:
			print(handle_parameter_expansion(command_line, dict))
main()
