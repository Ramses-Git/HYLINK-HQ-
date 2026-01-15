import time
import random

def function_mainmenu():
    print("""
MAIN MENU
ENTER PR TO OPEN PUBLIC RECORDS
ENTER CA TO OPEN CAMERAS
ENTER PP TO OPEN PROJECT PROTON
ENTER R TO OPEN [REDACTED]
""")
    
    action = input()
    return action
    
def function_publicrecords():
    print("""
    PUBLIC RECORDS
    HYLINK opened on the 13th of January 2026. It's goals are to [REDACTED] people with mental skills and oddities, to [REDACTED] [REDACTED] DNA samples for scientific research.
    DON'T TRUST THEM
    THEY TOOK MY BROTHER
    I DON'T KNOW WHAT THEY'RE DOING WITH HIM
    PLEASE HELP ME
    PLEASE HELP ME
    PLEASE HELP ME
    PLEASE HELP ME
    PLE- [The rest of this dialogue has been cut off for privacy reasons.]

    PRESS X TO GO BACK TO MAIN MENU.
    """)

def function_cameras():
    print("""OUTSIDE_CAMERA_01 [ANGLE LB]: NO OBJECTS RECORDED
OUTSIDE_CAMERA_02 [ANGLE LF]: NO OBJECTS RECORDED
OUTSIDE_CAMERA_03 [ANGLE RB]: RECORDED OBJECT, 3 METERS FROM SIDE WALL, LIKELY SMALL ANIMAL
OUTSIDE_CAMERA_04 [ANGLE RF]: NO OBJECTS RECORDED
INSIDE_CAMERA_01 [CAFETERIA]: RECORDED OBJECT, LIKELY 2 PEOPLE
INSIDE_CAMERA_02 [LEFT WING HALLWAY]: NO OBJECTS RECORDED
INSIDE_CAMERA_03 [OFFICES]: RECORDED OBJECT, LIKELY 6 PEOPLE
INSIDE_CAMERA_04 [TESTING HALLS]: {DISABLED. ONLY AUDIO.}

PRESS X TO GO BACK TO THE MAIN MENU
""")

def function_projectproton():
    print("""
    PROJECT PROTON
    Our new project to improve the scientific knowledge about mental skills and oddities.
    The DEVELOPERS have been working diligently on better DNA-[REDACTED] software.
    The rest of Project Proton will be revealed at a later date.
            
    [PROJECT PROTON IS STILL UNDER DEVELOPMENT.]
    
    PRESS X TO GO BACK TO THE MAIN MENU      
              """)

def function_redacted():
    print("""
    This is the truth about HYLINK HQ.
    Please, read all of this and don't forget it.
    I know they might try to take this down, but I hope the protection I set up against their dev team will stand for the time being.
    I'm being watched. By HYLINK employees. They don't want me to tell you this.
    Right, I forgot to introduce myself. I'm Cylo. Cylo Matthews.
    HYLINK took my brother, Jacob, to the HYLINK HQ building.
    They took him because he has really good vision.
    They took him to test on him. To extract his DNA for their own benefit.
    They don't want this information to be shared.
    I'll probably get in a lot of trouble.
    But I honestly don't even care.
    Oh god. There's something outside my house. They're banging on my door.
    If this is my last post, do not try to find me. Just try to collapse the HYLINK system.
    Please, free my brother. I'll try to help even if it's the last thing I do.
    They broke down my door. Please, help me. Free Jacob and collapse HYLINK, before it's
    
    PRESS X TO GO BACK TO THE MAIN MENU
              """)

PasswordCorrect = False
while not PasswordCorrect:
    password = input("WELCOME TO THE HYLINK HQ TERMINAL. PLEASE ENTER YOUR GIVEN PASSWORD.             ")

    if password == "HLHQ_01":
        PasswordCorrect = True
    else:
        print("PASSWORD IS INCORRECT.")
    for a in range(50):
        print("...")
        time.sleep(random.randint(1, 10)/75)

for a in range(10):
    print("...")
    time.sleep(random.randint(1, 10)/75)

for Percent in range(100):
    print("STARTUP:", str(Percent)+"%")
    time.sleep(random.randint(1, 10)/75)

for a in range(100):
    print("...")
    time.sleep(random.randint(1, 10)/90)

print("STARTUP: 100%")
#Dev Note 1: Someone needs to update this terminal...
print("...")

time.sleep(5)
print("BOOT SUCCESSFUL. WELCOME, HL_01.")
print("...")
time.sleep(2)
print("ENTER X TO OPEN MAIN MENU.")


while True:
    action = ""
    gotintoapp = True

    if input() == ("X"):
        action = function_mainmenu()
        
    if action == ("PR"):
            function_publicrecords()
    elif action == ("CA"):
            function_cameras()
    elif action == ("PP"):
        function_projectproton()
    elif action == ("R"):
        function_redacted()
    else:
        gotintoapp = False
        print("UNELIGIBLE INPUT. PRESS X TO RETURN.")   
    if gotintoapp:
        loop = True
        while loop:
            action2 = input()
            if action2 == ("X"):
                print("ENTER X AGAIN TO RETURN.")
                loop = False