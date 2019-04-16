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
			if dest_path == '+':
				dest_path = getenv("PWD")
				return dest_path

			# if destination path is '-'
			elif dest_path == '-':
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


def handle_parameter_expansion(dest_path):
	pass
