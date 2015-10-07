# instagram-clone
Instagram clone powered by Django 1.8.5. It works with python 3

Setup:   
pip3 install -r requirements.txt   
python3 manage.py migrate   
python3 manage.py runserver   

If error lib for image, please check here: http://pillow.readthedocs.org/en/3.0.x/installation.html   
   
Feature
* User registration/sign in/sign out
* Photo feeds as home page on user upload new photo
* Upload a new photo, each photo can have comments
* Follow a user by button follow in url /user/:id, it's not needed to send email, default user is followed yourself
* User profile page that shows user information as well as all his posted photos, user following, be followed
* Comments may have #hashtag - auto hightlight for search
* Search photos by #hashtag
* Crop photo and edit by recrop in profile
* Notification when a photo has new comment   
   
   
   
Screenshoot   

![alt tag](https://cloud.githubusercontent.com/assets/8637738/10350174/a7c450f0-6d6c-11e5-99ae-4f1ba7140a56.png)
![alt tag](https://cloud.githubusercontent.com/assets/8637738/10350227/f7d587b2-6d6c-11e5-89c1-168155da1ce2.png)
![alt tag](https://cloud.githubusercontent.com/assets/8637738/10350258/330b7d28-6d6d-11e5-876b-32fa09842b9b.png)
