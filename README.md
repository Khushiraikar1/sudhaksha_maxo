# Sudhaksha_maxo

![ADHAYAYAN](https://user-images.githubusercontent.com/72095693/104127815-38e42480-538a-11eb-8676-70c7c67b9a1a.png)  

## CONTENTS
1. [About Project](https://github.com/Khushiraikar1/sudhaksha_maxo#about-project)
   - [ Built with](https://github.com/Khushiraikar1/sudhaksha_maxo#built-with)
2. [ Getting Started](https://github.com/Khushiraikar1/sudhaksha_maxo/blob/main/README.md#getting-started)
   - [Prerequisites](https://github.com/Khushiraikar1/sudhaksha_maxo#prerequisites)
   - [Installation](https://github.com/Khushiraikar1/sudhaksha_maxo#installation)
3. [Contribution](https://github.com/Khushiraikar1/sudhaksha_maxo/blob/main/README.md#contribution)
  
    

# About Project

For the SCL maxo hackathon submission of team Sudhaksha
So we are creating a app which will have features of conducting online live classes with a timetable (the factulty member who has logged in can enter the class details and the students will be notified at the mentioned timings, can also provide link for their respective class sessions here) and also the faculty member will have facility to post the recorded versions of their classes,assignments, notes.We will be adding a few basic videos of some common courses
in the catalogue page.Also there will be additional features like quizzes, assignments (to be assigned by the respective faculty users) and tracking attendance.There are also features like online compilers too.If anyone wants to create a new classroom related to a particular domain they will receive the classcode to their respective mail ids given during logging in.We will also be dropping our official mail id which will be used to solve queries of the mail requests .There is also a seperate section for career guidance.
## Built with
![html5-js-css3-jquery-logo](https://user-images.githubusercontent.com/72095693/104134429-70b19300-53af-11eb-97d6-b69dbc6ff14a.png)
![boot](https://user-images.githubusercontent.com/72095693/104133473-d3a02b80-53a9-11eb-9be4-bcb41f25fb56.png)
![images](https://user-images.githubusercontent.com/72095693/104130654-e9a4f080-5397-11eb-82d9-ee1abfb34d6d.png)
- HTML
- CSS
- JAVASCRIPT
- [BOOTSTRAP](https://getbootstrap.com/)
- [PYTHON](https://www.python.org/)
- [DJANGO](https://www.djangoproject.com/)

***
## Getting Started
 ## Prerequisites 
1. Fork and Clone
   1.Fork the sudhaksha_maxo repo.
   2.Clone the repo in your computer
   
2. Create a Virtual Environment for the Project
In Windows
```
python -m venv venv

venv\Scripts\activate

```
In Ubuntu/MacOS/Linux
```
python -m virtualenv venv

source venv/bin/activate

```
If you are giving diffrent name for virtual environment `venv` then mention `.gitigonre` first

3. Install all the requirements
```
pip install -r requirements.txt

```
## Installation
4. Checkout the developed branch
```
git status
git pull
git branch
git checkout develop

```
5. Create a super user. In django if you want to access admin page you have to create an account first.
```
python manage.py createsuperuser
```
6. Runserver
```
python manage.py runserver

```
## Contribution
- Fork the Project
- Create your Feature Branch [`git checkout -b feature/AmazingFeature`]
- Commit your Changes [`git commit -m 'Add some AmazingFeature`]
- Push to the Branch [`git push origin feature/AmazingFeature`]
- Open a Pull Request
