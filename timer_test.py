from multiprocessing import Pool
import time
from threading import Thread

"""
def f(x, result):
    result.append(x*x)

if __name__ == '__main__':
    result = []
    t = threading.Thread(target=f, args=(10, result))
    t.start()
    t.join()
    print(result[0])  # Get the result when it's ready"""
"""
run = [True]
def back_end_timer(result, run):
	time.sleep(1)
	result.append(1)
	run.append(True)

def timer_running(run):
	if __name__ == '__main__':
		result = []
		func = Thread(target=back_end_timer, args=(result, run))
		func.start()
		func.join()
		print(result)

def timer_start(run):
	run = [run[-1]]
	if run[-1]:
		run.append(False)
		timer_running(run)

while True:
	timer_start(run)
"""

def back_end_timer(result, run):
	time.sleep(1)
	result.append(1)
	run.append(True)

def timer_running(run):
	if __name__ == '__main__':
		result = []
		func = Thread(target=back_end_timer, args=(result, run))
		func.start()
		func.join()
		return True

class Timer:
	def __init__(self):
		self.run = [True]
		self.start = 0

	def timer_start(self):
		self.run = [self.run[-1]]
		if self.run[-1]:
			self.run.append(False)
			if timer_running(self.run):
				self.start += 1
				return self.start

	def timer_end(self):
		self.run.append(False)

"""
def back_end_timer():
    time.sleep(1)
    return True


with Pool(1) as p: # only 1 task can be run at a time
	if p.apply_async(back_end_timer).get():
		print("True")
"""

"""
def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(1) as p:
        result = p.apply_async(f, (10,))  # Run function f in a separate process
        print(result.get(timeout=1))  # Get the result when it's ready
"""

"""
def clock(step):
	if __name__ == "__main__":
		Process(target=back_end_clock, args=(step, var)).start()
		Process(target=check).start()

def check():
	global answer
	while True:
		time.sleep(1)
		print(answer)
"""