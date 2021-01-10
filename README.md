# Sudhaksha_maxo

![ADHAYAYAN](https://user-images.githubusercontent.com/72095693/104127815-38e42480-538a-11eb-8676-70c7c67b9a1a.png)  

# About Project

For the SCL maxo hackathon submission of team Sudhaksha
So we are creating a app which will have features of conducting online live classes with a timetable (the factulty member who has logged in can eenter the class details and the students will be notified at the mentioned timings) and also the faculty member will have facility to post the recorded versions of their classes ..we will be adding a few basic videos ...at present we will create a few classrooms related to programming with few basic videos n if the users want they can add further recorded classes or reference videos as per their convenience..also there will be additional features like quizzes, assignments (to be assigned by the respective faculty users) and tracking attendance..if anyone wants to create a new classroom related to a particular domain we will be dropping our official mail id which will have a feature of authentication of the mail requests received for creating classes n replying with a particular password if found correct..there will also be a seperate section for career guidance.

## Built with
![ppp](https://user-images.githubusercontent.com/72095693/104133034-0f85c180-53a7-11eb-9c69-a474c76e16a7.png)
![images](https://user-images.githubusercontent.com/72095693/104130654-e9a4f080-5397-11eb-82d9-ee1abfb34d6d.png)
- HTML
- CSS
- JAVASCRIPT
- [BOOTSTRAP](https://getbootstrap.com/)
- [PYTHON](https://www.python.org/)
- [DJANGO](https://www.djangoproject.com/)

***
**Getting Started**
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
## Instalation
4. Checkout to a development branch
     ```git
    git status
    git pull
    git branch
    git checkout -b <your-branch-here>
    ```
   
5. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a super user.
    In Django, if you want to access admin page, you need to create an account with staff status first.
    ```djangotemplate
    python manage.py createsuperuser
    ```
   Then select your username and password. You can bypass a common password for development purposes.
   
7. Run the server on localhost:
    ```bash
    python manage.py runserver
    ```
## Contributing
- Fork the Project
- Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
- Commit your Changes (`git commit -m 'Add some AmazingFeature`)
- Push to the Branch (`git push origin feature/AmazingFeature`)
- Open a Pull Request