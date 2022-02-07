# import os
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import random

from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# os.environ['PATH'] += 'C:/Users/mural/Desktop/.vs/.vscode/python/selenium/chromedriver.exe'
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
logid = input('Enter usename: ')
pask = input('Enter password: ')
tech  = input('Enter test link: ')
driver.get('https://myprofile.technicalhub.io/login')
driver.implicitly_wait(20)
driver.maximize_window()
uname = driver.find_element(By.ID, 'username')
pas = driver.find_element(By.ID,'password')

uname.send_keys(logid)
pas.send_keys(pask)

login = driver.find_element(By.ID,'btn_login')
login.click()

op = driver.find_element(By.CSS_SELECTOR,'ul#nav-tabs-wrapper li:last-child')
op.click()

driver.implicitly_wait(20)

#tech = 'https://ajivika.technicalhub.io/course/view.php?id=224'

driver.get(tech)
driver.implicitly_wait(5)

# test = driver.find_element(By.ID,'module-5489')
# test.click()
# check = False
# elem = driver.find_elements(By.XPATH,"//*[@href]")
# for i in elem:
#     temp = i.get_attribute('href')
#     print(temp)
#     if "quiz" in str(temp):    
#         print()
#         print('------------------------ click on first link----------------')
#         print(temp)
#         print()
#         check = True
#         driver.get(temp)
#         break
# if check:
#     print("----------_____ entered ____------------------")

# driver.get('https://ajivika.technicalhub.io/mod/quiz/view.php?id=5489')
# driver.implicitly_wait(10)
# stop = True
# while stop:
#     try:
#         print('\nTrying to enter into test\n')
#         test = driver.find_element(By.XPATH,'//button[normalize-space()="Attempt quiz now"]')
#         print('\n\n test is running \n\n ')
#         print(test)
#         test.click()
#         sleep(1000)
#     except:
#         try:
#             nextQuiz = driver.find_element(By.ID,'next-activity-link')
#             print('\n\n enter into next test \n\n')
#             print(nextQuiz)
#             nextQuiz.click()
#             sleep(20)
#         except:
#             stop = False

# print('\n \n -----____ Process Completed _____-----')

links = []
elem = driver.find_elements(By.XPATH,"//*[@href]")
for i in elem:
    temp = i.get_attribute('href')
    if 'quiz' in temp:
        links.append(temp)
links = links[:]
for i in links:
    try:
        print('-------------------------------------------------------')
        print('\n Trying to open new test \n')
        driver.get(i)
        driver.implicitly_wait(10)
        print('\n link opened \n')
        try:
            print('\n trying to attempt test ')
            qt = driver.find_element(By.XPATH,'//button[normalize-space()="Attempt quiz now"]')
            print('\n starting test \n')
            qt.click()
            tb = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
            tb.click()
            print('\n \n test started \n \n ')
            try:
                k = 0
                while True:
                    # radio = driver.find_element(By.XPATH,'//*[@type="radio"][@value="0"]')
                    # radio.click()
                    # ans = driver.find_element(By.CSS_SELECTOR,'input[type="radio"][value="0"]')
                    # print(ans)
                    # ans.click()
                    # print('answered bit no ',k+1)
                    ans = driver.find_element(By.CLASS_NAME,'r0')
                    ans.click()
                    try:
                        np = driver.find_element(By.CSS_SELECTOR,"input[type='submit'][value='Next page']")
                        np.click()
                        k += 1
                    except:
                        fin = driver.find_element(By.CSS_SELECTOR,"input[type='submit'][value='Finish attempt ...']")
                        fin.click()

                        submit = driver.find_element(By.XPATH,'//button[normalize-space()="Submit all and finish"]')
                        submit.click()
                    
                        print('\n submited \n')
                        com = driver.find_element(By.CSS_SELECTOR,"input[type='button'][value='Submit all and finish']")
                        com.click()
                        print('\n test completed \n ')
                        break

            except:
                print('\n \n all bits completed or stopped at some point \n \n')
                
            #sleep(3)
        except:
            try:
                tb = driver.find_element(By.XPATH,'//button[normalize-space()="Continue the last attempt"]') 
                print('\n continue the last test \n')
                tb.click()
                print('\n \n test started \n \n ')
                try:
                    k = 0
                    while True:
                        # ans = driver.find_element(By.CSS_SELECTOR,"*[type='radio'][value='0']")
                        # ans.click()
                        # print('answered bit no ',k+1)
                        # sleep(1)

                        # ans = driver.find_element(By.CSS_SELECTOR,'input[type="radio"][value="1"]')
                        # print(ans)
                        # ans.click()

                        # radio = driver.find_element(By.CSS_SELECTOR,'input[type="radio"]')
                        # print(radio,'--------------------------------------sfds-f--sdf-sdf--sdf-s')
                        # radio.click()
                        # print('dfghdfcvghbgh')
                        # radio = driver.find_elements(By.XPATH,'//input[@type="radio"]')
                        # ids = []
                        # for i in radio:
                        #     id.append(i.get_attribute('id'))
                        # print(id)
                        #nid = ids[random.randrange(0,len(id))]
                        # ans = driver.find_element(By.ID,ids[0])
                        # ans.click()

                        ans = driver.find_element(By.CLASS_NAME,'r0')
                        ans.click()
                        try:
                            np = driver.find_element(By.CSS_SELECTOR,"input[type='submit'][value='Next page']")
                            np.click()
                            #k += 1
                        except:
                            fin = driver.find_element(By.CSS_SELECTOR,"input[type='submit'][value='Finish attempt ...']")
                            fin.click()

                            submit = driver.find_element(By.XPATH,'//button[normalize-space()="Submit all and finish"]')
                            submit.click()
                        
                            print('\n submited \n')
                            com = driver.find_element(By.CSS_SELECTOR,"input[type='button'][value='Submit all and finish']")
                            com.click()
                            print('\n test completed \n ')
                            break
                except:
                    print('\n \n all bits completed or stopped at some point \n \n')
                    break
                
            except:
                print('\nTest already completed or failed to start test\n')
                
                
        

    except:
        print('\n\n unexpected error occurred \n\n')
        break

print('\n \n -----____ Process Completed ____-----')
