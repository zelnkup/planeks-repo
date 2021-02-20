# docker compose up

Build an online service for generating CSV files with fake(dummy) data using Python and Django:

Any user can log in to the system with username and password.
You can use generic views provided by Django to implement
these features. Registering new users via the admin interface is
enough. Note, you do not need to implement a user profile
interface to support password change.
Any logged-in user can create any number of data schemas to
create datasets with fake data.
Each such data schema has a name and the list of columns with
names and specified data types.
You need to implement different types of data (at least 5
different types):
Full name (a combination of first name and last name)
Job
Email
Domain name
Phone number
Company name
Text (with specified range for a number of sentences)
Integer (with specified range)
Address
Date
Users can build the data schema with any number of columns
with any type described above. Some types support extra
arguments (like a range), others not.
Each column also has its own name (which will be a column
header in the CSV file) and order (just a number to manage
column order).
After creating the schema, the user should be able to input the
number of records he/she needs to generate and press the
“Generate data” button.
After pressing the button, the system must use Celery to
generate CSV file of specified structure, corresponding fake data
and save the result in the file somewhere in the “media”
directory.The interface should show a colored label of generation status
for each dataset (processing/ready).
Add a “Download” button for datasets available for download.
Completed application should be deployed to Heroku and be
available online (HTTPS should be supported). Please, create a
test user and provide us with the credentials.
The source code should be committed to the repository on
GitHub, Bitbucket, or GitLab.
