#!/usr/bin/python3
#
#
#
#
# Tengyue Zheng (June 2019) email: tengyue.zheng@addenbrookes.nhs.uk

#python libraries
import datetime
import sys
import os
import subprocess
import pprint as pp
import timeit

"""Create a OOP python class program for booking a room"""

# create count for each class to keep track of the number of users, admin and rooms
room_count = 0
user_count = 0
admin_count = 0
booking_count = 0

# create a dictionary for each class where info is stored
user_info = {}
admin_info = {}
room_info = {}
booking_info = {}

class User(object):

	"""
	A user who wish to book a room

	Attributes:
		username
		password
		name:
	Methods:
		register
		login
		new_username
		new_password
		new_name
	"""

	def __init__(self, username, password, name):

		"""Return a new User object."""

		self.username = username
		self.password = password
		self.name = name
		user_info[self.username] = {}
		user_info[self.username]["name"] = self.name
		user_info[self.username]["password"] = self.password
		user_count += 1

	def login(self):

		"""A user must login before booking a room"""
		print ("Please enter your login detail.")
		new_username = input("enter your username: ")
		new_password = input("enter your password: ")

		if new_username in user_info.keys() and new_password == user_info[new_username]:
			print ("login successful")
			user_info["last_login_time"] = datetime.datetime.now()
			return True
		else:
			print ("username or password incorrect")
			return False

	def register(self):

		"""A user must register before booking a room"""

		print("Registering new user")
		self.new_username()
		self.new_name()
		self.new_password()

	def new_username(self):

		"""A user can change their username after they login"""

		new_username = input("enter your username[e.g.johnsmith1:")

		if new_username in user_info.keys():
			print ("username already exist, try another username")
			return False

		else:
			user_info[new_username] = user_info[self.username]
			print ("username entered successfully")
			return True

	def new_password(self):

		"""A user can change their password after they login"""

		new_password = input("new password:")

		if new_password in user_info[self.username]["password"]:
			print ("password unchanged")
		else:
			user_info[self.username]["password"] = new_password
			print ("password changed")



	def new_name(self):

		"""A user can change their name after they login"""

		new_name = input("enter your full name [e.g.john_smith, please use _ between first and last name]:")
		
		if new_name in user_info[self.username]["name"]:
			print ("name already exist, try another name")
			self.new_name()
		
		else:
			user_info[self.username]["name"] = new_name
			print ("new name entered successfully")

	def displayinfo(self, username):		

		"""A user can view their user info after login"""

		pp.pprint (user_info[username])

class Admin(User):

	"""
	An administrator to manage the users, rooms, and bookings

	Attributes:
		username
		password
		name:
	Methods:
		register
		login
		new_username
		new_password
		new_name
		remove_user
		edit_user
		add_user
		remove_booking
		edit_booking
		add_booking
	"""

	def __init__(self, username, password, name, remove_user, edit_user, add_user, remove_booking, edit_booking, add_booking):
		User.__init__(self, username, password, name)
		self.remove_user = remove_user
		self.edit_user = edit_user
		self.add_user = add_user
		admin_count += 1

class Room(object):

	"""
	A room that can be booked by either user or administrator

	Attributes:
		room
		status
		capacity
		equipment
		location
	Methods:
		set_capacity
		set_equipment
		set_location
		set_status
	"""

	def __init__(self):
		self.room = {}
		self.status = None
		self.capacity = int()
		self.equipment = None
		self.location = None
		room += 1

	def set_capacity(self, room):

		"""A user or administrator can set the room capacity"""

		if room in room_info["room"]
			new_capacity = input("set room capacity [e.g.10]: ")

			if new_capacity.isdigit():
				self.capacity = new_capacity
				room_info["room"]["capacity"] = new_capacity
			else:
				print ("room capacity should be a number")
				break
		else:
			print ("room name not found")
			break

	def set_equipment(self, room):

		"""A user or administrator can set the equipment in the room"""

		if room in room_info["room"]:
			new_equipment = input("enter name of equipment: ")
			room_info["room"]["equipment"] = new_equipment
		else:
			print ("room name not found")
			break			

	def set_location(self, room):

		"""A user or administrator can set the location of the room"""

		if room in room_info["room"]:
			new_location = input("enter room location: ")
			room_info["room"]["location"] = new_location
		else:
			print ("room name not found")
			break			

	def set_status(self):

		"""A user or administrator can set the status of the room"""

		if room in room_info["room"]:
			new_status = input("enter new room status [free/occupied]: ")
			room_info["room"]["status"] = new_status
		else:
			print ("room name not found")

	def displayinfo(self):

		"""A user/administrator can view room info"""

		pp.pprint (room_info[username])

class Booking(User, Admin, Room):

	"""
	A booking that can be made by either a user or administrator after they have logged in

	Attributes:
		room
		status
		capacity
		equipment
		location
		date
		time

	Methods:
		set_date
		set_time
		set_duration
		remove_booking
		edit_booking
	"""

	def __init__(self, room, status, capacity, equipment, location, date, time, duration):
		Room.__init__(self, room, status, capacity, equipment, location)
		self.date = []
		self.time = []
		self.duration = []
		booking_count += 1

	def set_date(self, room):
		
		"""set a date for the meeting"""
		print ("please enter the room you would like to book")

		if self.room in booking_info["room"]:

			new_date = input("Enter a date for the meeting [YYYY-MM-DD]: ")

		if "-" in new_date and len(new_date.split("-")) == 3:
			
			day = int(new_date.split("/")[0])
			month = int(new_date.split("/")[1])
			year = int(new_date.split("/")[2])
			
			if day > 0 and month > 0 and year > 0:
				booking_info["room"][self.room]["date"] = new_date
				print ("booking date set")
			else:
				print ("date entered contain negative numbers")
		else:
			print ("check format of date entered")

		return booking_info

	def set_time(self, room):

		"""set a time for the meeting"""

		if self.room in booking_info["room"]:

			new_time = input("Enter start time for the meeting [e.g.HH:MM, please use 24hour format]: ")

		if ":" in new_date and len(new_time.split(":")) == 2:

			hour = int(new_date.split(":")[0])
			minute = int(new_date.split(":")[1])

			if 0 <= hour <= 23 and 0 <= minute < 60:
				booking_info["room"][self.room]["time"] = new_time
				print ("booking time set")
			else:
				print ("hours and minutes entered incorrect")
		else:
			print ("check format of time entered")

	def set_duration(self, room):

		"""set duration of meeting"""

		if self.room in booking_info["room"]:
			new_dur = input("Enter meeting duration in mins (e.g.30 or 60): ")

		if new_dur.isdigit():
			last_meet_time = booking_info["room"][self.room]["time"][-1]
			new_minute = int(last_meet_time.split(":")[-1]) + new_dur

			if new_minute > 59:
				minute = new_minute % 60
				hour = last_meet_time.split(":")[0] + int(new_minute / 60)
				if hour > 24:
					hour -= 24
				else:
					pass
			else:

			booking_info["room"][self.room]["duration"]:
			print ("booking duration set")

	"""
	def remove_booking()
	def edit_booking()
	"""

# function taken from https://gist.github.com/garrettdreyfus/8153571
def yes_or_no(question):

	reply = str(input(question+' (y/n): ')).lower().strip()
	if reply[:1] = 'y':
		return True
	else:
		reply[:1] = 'n':
		return False


if __name__ == "__main__":

	testuser = User(zhengt, abcde, tengyuezheng)
	print (User.displayinfo(zhengt))

	#Room.set_equipment(room1)
	#Booking.set_date(room1)