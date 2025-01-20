<h3 align=center>Vue3 + Django + Docker Template</h3>
<p align=center>
  <span>Template for building an app using Vue 3, Django, and Docker.</span>
  <br>
  <br>
  <img alt="Vue" src="https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D">
  <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)">
  <img alt="Postgres" src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">
</p>

<p align="center">
  <a href="#prerequisites">Prerequisites</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#command-snippets">Command Snippets</a>
</p>

## Prerequisites
1. [uv](https://docs.astral.sh/uv/)
2. [pnpm](https://pnpm.io/)
3. [Docker](https://www.docker.com/)
4. Unix or Linux OS

## Installation
```console
# clone repo
git@github.com:mfwaltzfordebby/vue-django-docker-template.git

# change directory
cd vue-django-docker-template 

# setup backend .env 
cp backend/.env.example backend/.env

# rename template django app
mv backend/template_app backend/<app_name>

# install new app 
replace `template_app` with the new `<app_name>` in the `INSTALLED_APPS` list inside the Django `settings.py`.
```

## Command Snippets
```console
# build containers
make dev-run

# lint codes BE
make lint-backend

# lint codes FE
make lint-frontend
```
