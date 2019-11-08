from task import Task
from queue import Queue
from event import Event
import sys
import re

def main():
	q = Queue()

	print("Available commands.\n" + 
		"'add e' to add an Event.\n" +
		"'add t' to add a Task\n" +
		"'show' to show all jobs.\n" + 
		"'todo' to print first job.\n"+
		"'r' to remove.\n" +
		"'q' to quit.")
	
	job = input("Enter: ")
	while job != 'q':

		#get rid of any unwanted spaces
		job = job.lower().strip()

		if job == 'todo':
			#print the first job
			q.todo()

		elif job == 'r':
			#remove the job with a confirmation
			done = input("Do you want to remove first job? (y/n): ")
			if done == "y":
				q.dequeue()

		elif job == 'add e':
			#go to add event
			addEvent(q)

		elif job == 'add t':
			#go to add task
			addTask(q)

		elif job == 'show':
			#print out all the jobs to be done
			q.showAll()

		else:
			print("That is not a command.")

		#repeat until quit
		job = input("Enter: ")

def addTask(q):

	#Task has a date, start time, duration, and list of assigned people.
	newTask = Task(input("Task Name: "), input("Date: "), input("Start Time: "),
		input("Duration: "), re.findall(r"[\w']+",input("People assigned to task: ")))
	q.enqueue(newTask)

def addEvent(q):

	#Event has a date, start time, and location
	newEvent = Event(input("Event Name: "), input("Date: "), input("Start Time: "),
		input("location: "))
	q.enqueue(newEvent)


if __name__ == '__main__':
	main()