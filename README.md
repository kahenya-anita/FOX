[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)

## FOXXL

- This is a blogging application written in Django REST framework

### Required Features

- Users can create an account and log in.
- Roles are 'MD' for moderator and 'WR' for writer
- Users can create a blog post.
- Users can view single blog posts.
- Users can view all blog posts.
- Users can update and delete the posts
- Users can click on a post and view more details.

### NB:

- The user can only edit, update or delete a blog post if he/she is the author.
- They have to be logged in to do this.

## Technologies & Languages

- **Postman** [https://www.postman.com/](url)
- **Python**
- **Django**
- **Django REST**

**Version control (Git)** [https://git-scm.com/](url)

# Installation and Setup

Clone the repository below

```
git clone
```

#### RUN USING

## 1) Local environment

```bash
$ Virtual Env- "python3 -m venv env"
$ Activating virtual - "source env/bin/activate"
$ requirements- "pip install -r requirements.txt"
$ runserver - "python3 manage.py runserver"
```

#### OR

### Serving the project from Docker

```bash
$ docker-compose build
$ docker-compose up
  or
$ docker-compose up -d (to run it in the background)
```

### Open postman and use the below endpoints.

## Endpoints Available

| Method | Endpoint            | Description                       | Roles       |
| ------ | ------------------- | --------------------------------- | ----------- |
| POST   | /auth/register      | sign up a user                    | users       |
| POST   | /auth/login         | login a users                     | users       |
| POST   | /blog/post          | Create a single blog post         | users/admin |
| GET    | /blog/posts         | get different posts               | Users       |
| GET    | /blog/posts/{un_id} | return a single blog post         | users       |
| PUT    | /blog/posts/{un_id} | update a specific blog post       | Users       |
| PATCH  | /blog/posts/{un_id} | partial update of a specific post | Users       |
| DELETE | /blog/posts/{un_id} | delete a specific blog post       | Admin/users |

### Author

Anita Kahenya

## [License](LICENSE)

MIT
