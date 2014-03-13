This document will show you how to first use the lunarshift webapp. This information is copied from the Assembla pages of Team 110. For a version with images and displays please visit the assembla software documentation. https://www.assembla.com/spaces/cis422w14_team6_p2/wiki/Software_Documentation

Open your favorite browser and navigate to our page at http://lunarshift.herokuapp.com/

=========================
LunarShift's User's Guide 
=========================

---------------------
System Requirements:
---------------------

LunarShift is designed so there is no installation needed. It is simply run on a website. Thus, the user must have access to the internet. LunarShift is currently only supported fully on Google Chrome, so installation for Google Chrome is specified below if it is not already installed on your machine.

=========================
1. Getting Started
=========================

------------------------------------------
1.1 Open chrome web browser application.
------------------------------------------

Chrome: only web browser to fully support LunarShift.
If you do not have chrome installed then you will need to install it.

---------------------	 
1.1.2 Install Chrome
---------------------

Open a web brower and type 'https://www.google.com/intl/en/chrome/browser/' in the url bar. 

Click the 'Download Chrome' button on that page.
        
Accept the terms and conditions on the popup window. 
        
Open the googlechrome.dmg with the default mounter, and select 'OK'.
        
The dmg file will drag the chrome icon into the applications folder. 
        
Launch google chrome web browser application. Now you are ready to log into LunarShift.
        
----------------------------------
1.2 Visit the LunarShift website. 
----------------------------------

Type "http://lunarshift.herokuapp.com/" in the browser bar.

=========================
2. Using LunarShift
=========================

----------------------------------
2.1 Login to LunarShift
----------------------------------

The user can logo by inputing their credentials into the login page. The username will be the email address that the employer has set up for the user. The password will be one that the user has chosen when their account was created.After entering correct credentials, click 'Submit'. If the user decides they do not want to proceed after entering credentials, click 'Cancel'. This will leave the user at the login page.

Ex.
USERNAME: AstroPig
PASSWORD: oink2345

---------------------
2.1.1 Manager login: 
---------------------

After credentials have been verified, if they match admin permissions it'll lead to the Admin page.        

------------------------   
2.1.1.1 View schedule
------------------------

At the admin page the user can view the current schedule by selecting the tab "Schedule" at the top of the navigation bar. The user must select the day from the calendar slider to display the employees scheduled for that day, along with the time interval that the employee is working, and the total number of hours they work.
       
-------------------------            
2.1.1.2 Build a schedule
-------------------------

At the admin page, the manager will navigate to the "Employees" tab from the navigation bar to begin building a schedule. This will instruct the user how to build a schedule as well as add and remove employees to and from the schedule.

This page will list the employees, their email address, whether they have submitted their availability: Thumbs up icon indicated the employee has submitted their availability; Thumbs down icon  indicates that the employee has not submitted their availability.

To build a schedule the user must first set the hours that need to be covered. 
    
See section 2.1.1.2.1 Set hours that need to be covered.
    
The user will then need to add employees to the schedule.
See section 2.1.1.2.2 Add/ Remove employees from schedule.
 
After all desired employees are selected for the next month's schedule, the user can click "Build Schedule" and LunarShift will automatically calculate a schedule based on "the fairest algorithm in all the land" algorithm (defined in the SRS  section 8.1 under definitions), this schedule will be displayed when you then navigate to the "Schedule" tab. 
        
---------------------------------------------             
2.1.1.2.1 Set hours that need to be covered
---------------------------------------------

At the admin page, the manger can set the hours that need to be covered for the next months schedule by navigating to the 'Availability' tab. 

The manager can select 'Add Day' ie (Monday - Sunday) and use the blue slider bar to adjust the times that need to be covered for the day.  If at any time the user does not want a certain day or shift on the schedule, the can click 'Delete' at the top right of the day's table, and that day/shift will be removed. 

----------------------------------------------
2.1.1.2.2 Add/ Remove employees from schedule
----------------------------------------------

At the admin page, the manger can add and remove employees from the schedule by navigating to the 'Employees' tab. 

Thumbs up icon indicated the employee has submitted their availability; Thumbs down icon  indicates that the employee has not submitted their availability. If an employee's Schedule check box is not 'checked' when the schedule is built, then that employee will not be added to the next month's schedule. 

----------------------------------------
2.1.1.3 Deactivate/Activate an employee
----------------------------------------


At the admin page, the manger can activate/deactivate an employee by navigating to the "Employees" tab. The current employees will be listed on this page. 

To activate an employee to LunarShift, the manager will select "Activate Employee". This will cause a pop up window to appear where the user will fill in the new users credentials. --INPUT PICTURE-- The user will select "Submit" after all the credentials are entered and then the new user will appear in the list of employees. 
       
To deactivate an employee the manager will click "Deactivate". The manager will be prompted with a message to verify they want to deactivate that employee from LunarShift, the manager will select "Yes" to deactivate the employee or "No" to cancel the deactivation. The employee once deactivated will be removed from the list of employees and no longer able to access to LunarShift.

-------------------------
2.1.2    Employee login:
-------------------------

After credentials have been verified, if they match employee permissions it'll lead to the Employee page.

------------------------------
2.1.2.1 View current schedule
------------------------------

At the employee page the user can view the current schedule.      

----------------------------
2.1.2.2 Set available hours
----------------------------

At the employee page the user can set available hours. This is done by typing in the hours in the text boxes under the day that the user is available to work. After all available hours have been entered the user can leave this page and their information will be updated.

 
=========================
3. FAQ
=========================

-----------------------------
3.1 Questions for Admin Use: 
-----------------------------

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
3.1.1 What if the employee hasn't set their schedule yet, what will it display?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

On the "Employees" page, it will display a list of employees. If an employee hasn't submitted their availability for the month, then it will display a thumbs down icon. If the employee doesn't submit their availability by the time the manager builds the schedule, they will not be on the schedule.

++++++++++++++++++++++++++++++++    
3.2 Questions for Employee Use:
++++++++++++++++++++++++++++++++

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3.2.1 How do I create my login info?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The manager will create login information (ie username/password) for you and supply you with the credentials before you can login.

+++++++++++++++++++++++
3.3 General Questions:
+++++++++++++++++++++++

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3.3.1 How do I contact LunarShift?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At the top of the LunarShift webpage there is a tab called 'Contact'. Select 'Contact' and it will display LunarShifts contact information.  Including: contact help-desk phone number; contact by email address; contact my mail address.
