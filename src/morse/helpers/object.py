from abc import ABCMeta, abstractmethod
import MorseTransformation

class MorseObjectClass(object):
	""" Basic Class for all 3D objects (components) used in the simulation.
		Provides common attributes. """

	# Make this an abstract class
	__metaclass__ = ABCMeta

	def __init__ (self, obj, parent=None):
		""" Constructor method. """
		# Fill in the data sent as parameters
		self.blender_obj = obj
		self.robot_parent = parent

		# Create an instance of the 3d transformation class
		self.position_3d = MorseTransformation.Transformation3d(obj)

		# Dictionary to store the data used by each component
		self.local_data = {}

		# Define lists of dynamically added functions
		self.input_functions = []
		self.output_functions = []
		self.modifier_functions = []
		self.del_functions = []


	def __del__(self):
		""" Destructor method. """
		print ("%s: I'm dying!!" % self.blender_obj.name)
		# Call specific functions added to this object
		for function in self.del_functions:
			function()

	def action(self):
		""" Call the action functions that have been added to the list. """
		# First the input functions
		for function in self.input_functions:
			function(self)

		# Call the regular action function of the component
		self.default_action()

		# Make a copy of the data before modifications
		self.send_data = self.local_data
		# Data modification functions
		for function in self.modifier_functions:
			self.send_data = function(self)

		# Lastly output functions
		for function in self.output_functions:
			function(self)


	def default_action():
		""" Abstract model for the default action that should be
			implemented by all subclasses of MorseObject_Class. """
		pass


	def print_data(self):
		""" Print the current position of the blender object. """
		for variable, data in self.local_data.items():
			res = variable + str(data) + " "
		print ("%s" % res)