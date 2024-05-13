
## What is this repo for?
This repo is the Coursepedia project that can present your course history and recommend your future courses for NYU Shanghai CS students.

The contributors are [Yongyu Liu](https://github.com/YongyuLiu03), [Haocheng Yang](https://github.com/Harry-Yang0518), and [Yuxuan Xia](https://github.com/NovTi)

## How to run the software
Follow these steps to run the project

## Backend 
1. install dependencies
``` 
pip install django-cors-headers Django djangorestframework psycopg
```

2. Database setup (Make sure you have PostgreSQL installed)

```bash
createdb your_database_name
```
    
4. Modify database settings in backend/se_project/settings.py


5. Run migrations and start the Django development server:

```bash
cd backend
python manage.py migrate
python manage.py runserver
```

## Frontend

Before you begin, make sure you have Node.js and npm installed on your machine. You can download and install them from [here](https://nodejs.org/).


```bash
cd frontend
npm install
npm start
```

## Run test cases

Go to [Test README](backend/test/README.md) for detail instruction to run tests


## Tip for usage

Refer to [issue 12](https://github.com/YongyuLiu03/SEproject/issues/12#issuecomment-2107356155) for the instruction to get the course history source code.


## Links

- [Group Project Folder](https://drive.google.com/drive/folders/1bN0Qwhw-A0KcsbxDqG4MjQsyJCyuXpMK?usp=sharing)
- [Weekly Meeting Logs](https://docs.google.com/document/d/15pVdvmcztm7i7RDhoF95CvmVSybGwcfDFcdfjAZPFGc/edit?usp=sharing)
- [SNOW (Functionality-Add)](https://github.com/YongyuLiu03/Snow)
