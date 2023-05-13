# pull official base image
FROM python:3.9.13

# set work directory
WORKDIR /usr/src/audit

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependecies
RUN apt-get update \
	&& apt-get install -y postgresql gcc python3-dev musl-dev netcat

# copy project
COPY . .

# install dependecies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy entrypoint.sh
RUN sed -i 's/\r$//g' /usr/src/audit/entrypoint.sh
RUN chmod +x /usr/src/audit/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/audit/entrypoint.sh"]