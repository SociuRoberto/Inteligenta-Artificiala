import pyautogui
import keyboard
import time

def youtube():
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_google.png', confidence=0.7) != None:
		camp_google=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_google.png', confidence=0.7)
		pyautogui.click(camp_google)
		time.sleep(3)
		pyautogui.write("https://temp-mail.org/en/")
		pyautogui.press('enter')
	else:
		print ("IMAGINEA NU SE AFLA PE ECRAN")
	time.sleep(10)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\email_generator.png', confidence=0.7) != None:
		camp_emailgenerator=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\email_generator.png', confidence=0.7)
		pyautogui.click(camp_emailgenerator)
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\new_tab.png', confidence=0.7) != None:
		camp_newtab=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\new_tab.png', confidence=0.7)
		pyautogui.click(camp_newtab)
		time.sleep(3)
		pyautogui.write("https://www.youtube.com/")
		pyautogui.press('enter')
	else:
		print ("IMAGINEA NU SE AFLA PE ECRAN")
	time.sleep(2)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\sign_in.png', confidence=0.7) != None:
				camp_signin=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\sign_in.png', confidence=0.7)
				pyautogui.click(camp_signin)
				time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\create_account.png', confidence=0.7) != None:
		camp_createaccount=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\create_account.png', confidence=0.7)
		pyautogui.click(camp_createaccount)
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\personal_use.png', confidence=0.7) != None:
		camp_personaluse=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\personal_use.png', confidence=0.7)
		pyautogui.click(camp_personaluse)
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\first_name.png', confidence=0.7) != None:
		camp_firstname=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\first_name.png', confidence=0.7)
		time.sleep(3)
		pyautogui.write("School1")
		time.sleep(2)
		pyautogui.press('tab')
		pyautogui.write("Project1")
		time.sleep(2)
		pyautogui.press('tab')
		pyautogui.keyDown('ctrl')
		pyautogui.press('v')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\new_tab.png', confidence=0.7) != None:
		camp_newtab=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\new_tab.png', confidence=0.7)
		pyautogui.click(camp_newtab)
		time.sleep(5)
		pyautogui.write("https://delinea.com/resources/password-generator-it-tool")
		pyautogui.press('enter')
		time.sleep(2)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\generate_password.png', confidence=0.7) != None:
		camp_generatepassword=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\generate_password.png', confidence=0.7)
		pyautogui.click(camp_generatepassword)
		time.sleep(2)
		pyautogui.keyDown('ctrl')
		pyautogui.press('c')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
		pyautogui.keyDown('ctrl')
		pyautogui.press('w')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\password.png', confidence=0.7) != None:
		camp_password=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\password.png', confidence=0.7)
		pyautogui.click(camp_password)
		time.sleep(3)
		pyautogui.keyDown('ctrl')
		pyautogui.press('v')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
		pyautogui.press('tab')
		time.sleep(2)
		pyautogui.keyDown('ctrl')
		pyautogui.press('v')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\next.png', confidence=0.7) != None:
		camp_next=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\next.png', confidence=0.7)
		pyautogui.click(camp_next)
		time.sleep(3)
		pyautogui.keyDown('ctrl')
		pyautogui.press('tab')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
		pyautogui.scroll(-300)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\verify_email.png', confidence=0.7) != None:
		camp_verifyemail=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\verify_email.png', confidence=0.7)
		pyautogui.click(camp_verifyemail)
		time.sleep(3)
		pyautogui.scroll(-750)
		time.sleep(2)
		pyautogui.moveTo(950, 750)
		pyautogui.doubleClick()
		time.sleep(2)
		pyautogui.keyDown('ctrl')
		pyautogui.press('c')
		pyautogui.press('w')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
		pyautogui.keyDown('ctrl')
		pyautogui.press('v')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\next.png', confidence=0.7) != None:
		camp_next=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\next.png', confidence=0.7)
		pyautogui.click(camp_next)
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\new_tab.png', confidence=0.7) != None:
		camp_newtab=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\new_tab.png', confidence=0.7)
		pyautogui.click(camp_newtab)
		time.sleep(2)
		pyautogui.write("https://randommer.io/Phone")
		pyautogui.press('enter')
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\fake_number.png', confidence=0.7) != None:
		camp_fakenumber=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\fake_number.png', confidence=0.7)
		pyautogui.click(camp_fakenumber)
		time.sleep(3)
		pyautogui.moveTo(950, 550)
		pyautogui.doubleClick()
		pyautogui.click()
		time.sleep(2)
		pyautogui.keyDown('ctrl')
		pyautogui.press('c')
		pyautogui.press('w')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
		pyautogui.moveTo(950, 550)
		pyautogui.click()
		pyautogui.keyDown('ctrl')
		pyautogui.press('v')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\next.png', confidence=0.7) != None:
		camp_next=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\next.png', confidence=0.7)
		pyautogui.click(camp_next)
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\new_tab.png', confidence=0.7) != None:
		camp_newtab=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\new_tab.png', confidence=0.7)
		pyautogui.click(camp_newtab)
		time.sleep(2)


def cautare_google():
	i=1
	x=600
	y=300
	z=-450
	pyautogui.write("https://www.youtube.com/c/ZonaitTvro")
	pyautogui.press('enter')
	time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_subscribe.png', confidence=0.7) != None:
		camp_subscribe=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_subscribe.png', confidence=0.7)
		pyautogui.click(camp_subscribe)
		time.sleep(3)
	if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7) != None:
		camp_video=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7)
		pyautogui.click(camp_video)
	time.sleep(2)
	while not keyboard.is_pressed('esc'):
		pyautogui.scroll(z)
		while (i>0):
			if (i%5==1):
				pyautogui.moveTo(x, y)
				time.sleep(2)
				pyautogui.click()
				time.sleep(2)
			else:
				pyautogui.scroll(z)
				time.sleep(2)
				pyautogui.moveTo(x, y)
				time.sleep(2)
				x=x+300
				time.sleep(2)
				pyautogui.click()
				time.sleep(2)
			if (i%5==0):
				x=600
				z=z-300
			if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\like.png', confidence=0.7) != None:
				camp_like=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\like.png', confidence=0.7)
				pyautogui.click(camp_like)
				time.sleep(3)
			if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_canal.png', confidence=0.7) != None:
				camp_canal=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_canal.png', confidence=0.7)
				pyautogui.click(camp_canal)
				time.sleep(3)
			if pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7) != None:
				camp_video=pyautogui.locateOnScreen(r'C:\Users\Liviu\Desktop\04-11-2022-Python\cautare_video.png', confidence=0.7)
				pyautogui.click(camp_video)
			i+=1

			
time.sleep(2)
youtube()
cautare_google()