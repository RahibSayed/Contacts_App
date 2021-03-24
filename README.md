# Contacts_App
 This is documentation for running this application, it is a contacts website that allows a user to add, delete, update and search for contacts by name. I created this app using Vue js for the front end, Python for the API and the data stored in a SQL database.

# Pre-Requisites
 Python 3.9.2 

 <a href='https://python.org/downloads'>Download Python</a> 

 Node.js 14.16.0 

 <a href='https://nodejs.org/en/download'>Download Node js</a>
 
 Postman (optional to run API independently)
 
  <a href='https://www.postman.com/downloads/'>Download Postman</a>
 
 # Run Project
 Download the zip file and extract or use Git to download the project.
 Git command:
 
 git clone https://github.com/RahibSayed/Contacts_App.git

 Once downloaded and extracted, locate the project directory named ‘Contacts_App-main' and open this directory in Command Prompt 

 To install the Api go to the ‘Contacts_App-main/Api’ directory and run these python commands in the following order:
 
 py -m pip install pipenv 

 py -m pipenv install 

 py -m pipenv shell 

 py app.py
 
 To run the front end, open the ‘Contacts_App-main/Vue_App/contact-page’ directory in a new Command Prompt and run these commands: 

 npm install 

 npm run serve 

 Follow the 'Local' URL  provided once you have the app running to open the Vue app. Copy the URL into a web browser this should display a Contacts page in the browser.
 # Application functionality
 You can add a contact by clicking on the ‘Add Contact’ button which opens a form, fill in the form with your ‘Name’, ‘Phone number’ and ‘Email’ and submit the form by clicking  the ‘Save Contact’ button. The form can also be closed by pressing the red 'Close' button 

 Once you have created a contact it will appear on the page, the new contact will be added to the end of the list. You can search for the contact by entering the contacts name or characters that are included in the contacts' name. Search an empty field to retrieve all contacts.

 To delete a contact, click the red ‘x’ button. A popup box will confirm if you want to delete the contact select 'OK' and it will be removed from the list of contacts. 

 Clicking on the green pen on a contact will open a form that shows the current contact information in editable fields. Edit the contact by changing the text in the fields. To save the changes click on the ‘Update Contact’ once you have made the necessary changes. The green pencil button can be clicked again to close the form.
 
 # Api 
 In the Contacts_App-main folder there is a file named 'Contacts.postman_collection.json', this can be imported to Postman for further information to run the API indepedently with example API calls.
 
 # Unit test
 Open the 'Contacts_App\Unit_tests' directory in Command Prompt and run:
 py test_api.py
 
