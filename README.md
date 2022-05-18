### Author
##### Brian Otieno
### My_Blog_Post
**  A web application that allows various users to submit a short   Blog_Post, also view random blogosts generated from random API.

#### Description
This application is developed to give users an opportunity to practice to say something meaningful if the user was ever given only one minute in life to say something. To see this site effectively user has to register first. If not registered, user can only see the Blog_posts from other users but if registered, user can add a category for the pitch or he can add a pitch in the existing category. User can also like/dislike or comment on the BLOG_Posts


*****


Running the Application
Creating the virtual environment

  $ python3.6 -m venv --without-pip virtual
  $ source virtual/bin/env
  $ curl https://bootstrap.pypa.io/get-pip.py | python
Installing Flask and other Modules

  $ see Requirements.txt
To run the application, in your terminal:

  $ chmod +x start.sh
  $ ./start.sh





*****





#### Specifications

Behaviour Driven Development display a list of categories

 ###### INPUT:"Show category button pressed" OUTPUT:"An area displaying all the existing categories" displays a link to see pitches of a particular category INPUT:"source link clicked" OUTPUT:"A page displaying all the pitches in a category" adds a new pitch INPUT:"Add new pitch button pressed" OUTPUT:"New pitch in a particular category added" registers user to the website INPUT:"A form containing required info of user is submitted" OUTPUT:"User is registered with a specific email and password" login user to the website INPUT:"User enter password and email address" OUTPUT:"User loggedin to the system" Technologies Used Python 3.6 Flask Framework HTML, CSS(Bootstap) & JavaScript(jQuery) PostgreSQL Pip*

 *** Setup Installations Requirements
To run the application, in your terminal:
Clone or download the Repository
Create a virtual environment
Read the requirements file and Install all the requirements. Or run pip3 install -r requirements.txt to automatically install all the requirements
Prepare environment variables -export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitching' -export SECRET_KEY='Your secret key'
Run chmod a+x start.sh
Run ./start.sh
Access the application through localhost:5000 Development Want to contribute? Great!
To fix a bug or enhance an existing module, follow these steps:

**** Fork the repo Create a new branch (git checkout -b improve-feature) Make the appropriate changes in the files Add changes to reflect the changes made Commit your changes (git commit -am 'Improve feature') Push to the branch (git push origin improve-feature) Create a Pull Request Known Bugs If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.

* License
MIT Copyright (c) 2022 Brian otieno
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

** About Flask application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

** Resources Readme Stars 0 stars Watchers 1 watching Forks 0 forks Releases No releases published Packages No packages published Languages HTML 57.7%

CSS 27.8%

Python 13.9%

Other 0.6%