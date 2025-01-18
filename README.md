# Facial Attendance System


## Introduction

The Facial Attendance project aims to build a system capable of recording and storing
the attendance of users/clients by recognizing their faces. In any working environment,
attendance is essential as it provides information about whether a user was present on
a given day or not. This information can be very useful in situations like determining
the number of working days for users to calculate their estimated monthly salary, among
other purposes.

## Technology Used

- Frontend:HTML, CSS, JavaScript, Bootstrap
- Backend: Django
- Database:MySQL
- Python Libraries: DeepFace, sklearn-metrics (cosine similarity)

## System Design

### Django Templates

- home.html:This contains the home page of the website. A navigation bar is placed
    at the top of the home page providing options to access the page for registration
    of new users and viewing the list of already registered users. In the center of the
    home page lies a hyperlinked image that redirects users to a submission page where
    an image is uploaded to match the user’s image present in the database.
- newuser.html: This page contains a form which is used to insert data into the
    database for new user registration. The form contains fields such as:
       - userid
       - username
       - userphoneno
       - userimage


- usercity
- userzipcode

```
Upon submission, it generates an SQL query and uses the form’s values to create a
new entry in the database.
```
- viewprofiles.html: This page displays all the registered users along with their
    total attendance count. It accesses the stored database to fetch and present the
    required data.

### SQL Database Schema

The database is created with the following attributes:

- user id:CharField(maxlength=10)
- user name:CharField(maxlength=100)
- user img:ImageField(uploadto=’userimages’)
- user email:EmailField()
- user city:CharField(maxlength=50)
- user phoneno:CharField(maxlength=100)
- user zipcode:IntegerField()
- user AttendanceCount:IntegerField(default=0, blank=True)

## Overall Working

The working of the Facial Attendance System is as follows:

1. The user is presented with two options on the home page:
    - Register as a new user.
    - Record attendance for an existing user.
2. If registering a new user:

```
2.1. The user fills out a form with the following fields:
```
- Name, phone number, city, zip code, and image.
2.2. Upon submission, the system saves the data and the face embedding in the
database.
3. If recording attendance:

```
3.1. The user uploads an image.
3.2. The system extracts face embeddings using the DeepFace library.
3.3. It compares the embeddings with the stored embeddings in the database.
3.4. If the cosine similarity is greater than 0.2, the attendance count for the matched
user is incremented by 1.
3.5. If no match is found, the system notifies the user that they are not registered.
```

## Flowchart

The flowchart below illustrates the working of the system:

## Conclusion

The Facial Attendance System offers an efficient and automated solution for attendance
tracking in a workplace environment. By leveraging facial recognition technology and in-
tegrating it into a Django-based web application, the project ensures accurate attendance
recording while providing a user-friendly interface.


