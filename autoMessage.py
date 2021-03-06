import time
import pyautogui

def switch_to_messages():
	pyautogui.hotkey('command', 'space')
	pyautogui.hotkey('command', 'space')
	time.sleep(3)
	pyautogui.write('Messages')
	time.sleep(3)
	pyautogui.press('enter')
	time.sleep(1)

def write_messages(name, text):
	pyautogui.hotkey('command', 'n')
	time.sleep(1)

	pyautogui.write(name)
	time.sleep(1)
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.press('enter')
	time.sleep(3)

	for line in text.splitlines():
		pyautogui.write(line)
		time.sleep(1)
		pyautogui.press('enter')
		time.sleep(1)

	time.sleep(1)

def main():
	pyautogui.FAILSAFE = True
	pyautogui.PAUSE = 0

	recipient = input("Who is the recipient? ")
	script = open(input("What is the message file? ")).read()

	switch_to_messages()
	write_messages(recipient, script)

if __name__ == '__main__':
	main()
