from math import sqrt, acos, pi

class Vector():
	"""Represents a Vector."""
	
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = coordinates
			self.dimension = len(self.coordinates)
		
		except ValueError:
			raise ValueError('The coordinates must not be empty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable')

	def __str__(self):
		"""Returns the string representation of this Vector."""
		return 'Vector: {}'.format(self.coordinates)

	def __eq__(self, v):
		"""Compare the coordinates of this vector with those of another vector."""
		return self.coordinates == v.coordinates

	def __add__(self, v):
		"""Returns a Vector that is the sum of two Vector objects."""
		if self.dimension == v.dimension:
			sum = tuple()
			for i in range(self.dimension):
				sum += (self.coordinates[i] + v.coordinates[i],)
			return Vector(sum)

		raise IndexError('The number of coordinates is not consistent')

	def __sub__(self, v):
		"""Returns a Vector that is the difference between two Vector objects."""
		if self.dimension == v.dimension:
			diff = tuple()
			for i in range(self.dimension):
				diff += (self.coordinates[i] - v.coordinates[i],)
			return Vector(diff)

		raise IndexError('The number of coordinates is not consistent')

	def __mul__(self, v):
		"""Calculate the cross product between two Vectors."""
		row1 = self.coordinates[1] * v.coordinates[2] - v.coordinates[1] * self.coordinates[2]

		row2 = -(self.coordinates[0] * v.coordinates[2] - v.coordinates[0] * self.coordinates[2])

		row3 = self.coordinates[0] * v.coordinates[1] - v.coordinates[0] * self.coordinates[1]

		return Vector((row1, row2, row3))

	def degrees_from_radians(self, radians):
		"""Convert radians to degrees."""
		return radians * 180 / pi

	def scaled_by(self, scalar):
		"""Returns a scalar multiple of this Vector."""
		return Vector(tuple([scalar * self.coordinates[i] for i in range(self.dimension)]))

	@property
	def magnitude(self):
		"""float: The magnitude of this Vector."""
		return sqrt(sum(self.coordinates[i]**2 for i in range(self.dimension)))
		
	@property
	def normalized(self):
		"""Vector: The unit Vector."""
		return Vector(tuple([(1/self.magnitude) * self.coordinates[i] for i in range(self.dimension)]))

	def dot(self, v):
		"""Calculate the dot product between two Vectors."""
		return sum([self.coordinates[i] * v.coordinates[i] for i in range(self.dimension)])

	def angle_between(self, v, degrees=True):
		"""Calculate the angle between two Vectors."""
		theta_in_radians = acos(self.dot(v) / (self.magnitude * v.magnitude))
		if degrees:
			return degrees_from_radians(theta_in_radians)

		return theta_in_radians

	def is_orthogonal_to(self, v):
		"""Returns True if the Vectors are orthogonal."""
		try:
			return self.angle_between(v) == 90.

		except ZeroDivisionError:
			return True

	def is_parallel_to(self, v):
		"""Returns True if the Vectors are parallel."""
		try:
			return self.angle_between(v) == 0. or self.angle_between(v) == 180.

		except ZeroDivisionError:
			return True

	def projected_onto_basis(self, basis):
		"""Returns a projection of the Vector onto the basis Vector."""
		basis_unit = basis.normalized
		return basis_unit.scaled_by(self.dot(basis_unit))

	def orthogonal_to_basis(self, basis):
		"""Returns a Vector that is orthogonal to the basis Vector."""
		return self - self.projected_onto_basis(basis)

	def area_of_parallelogram_with(self, v):
		"""Returns the area of a parallelogram that spans two Vectors."""
		return (self*v).magnitude

	def area_of_triangle_with(self, v):
		"""Returns the area of a triangle that spans two Vectors."""
		return .5*self.area_of_parallelogram(v)


