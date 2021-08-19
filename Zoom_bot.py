import subprocess  # USE TO OPEN ZOOM APPLICATION
import pyautogui   # HELPS TO AUTOMATE MOUSE MOVEMENT AND TYPING 
import time
import pandas as pd   # TO TAKE THE INPUT FROM THE CSV FILE AND USE IT IN THE PROGRAM
from datetime import datetime

def sign_in(meetingid, pswd):
    #Opens up the zoom app
    #change the path specific to your computer
    
    #If on windows use below line for opening zoom
    #subprocess.call('C:\\myprogram.exe')
    
    #If on mac / Linux use below line for opening zoom
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])

    time.sleep(10)   # AFTER OPENING THE APP 10 SEC WAIT FOR NEXT STEP
    
    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')     # IT WILL LOCATE THE CENTER OF THE BUTTON AND WIIL GIVE US THE X AND Y COORDINATES
    pyautogui.moveTo(join_btn)   # MOVE THE CURSOR ON THAT COORDINATES
    pyautogui.click()          # CLICK THE BUTTON

    # Type the meeting ID
    meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id_button.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meetingid)   # WRITES THE MEETING ID

    # Disables both the camera and the mic
    media_btn = pyautogui.locateAllOnScreen('media_btn.png')   # LOCATE ALL THE BUTTONS ON THE SCREEN LIKE THE MEDIA BUTTON AND WE WILL GET A LIST
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)

    # Hits the join button
    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    
    time.sleep(5)
    #Types the password and hits enter
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')   # PRESSES THE ENTER KEY

# Reading the file
df = pd.read_csv('timings.csv')    # READ THE CSV FILE USING PANDAS

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")   # CURRENT TIME IN HOURS AND MINUTES AND IT IS GOING TO BE IN FORM OF THE STRING
    if now in str(df['timings']):    # IF CURRENT TIME IS SAME AS TIMINGS GIVEN IN CSV

       row = df.loc[df['timings'] == now]   # LOC IS USED TO ITERATE THROUGH THE DATAFRAME TO GET THE SPECIFIC SPOT
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in(m_id, m_pswd)
       time.sleep(40)
       print('signed in')