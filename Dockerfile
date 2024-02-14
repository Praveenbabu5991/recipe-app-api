# FROM python:3.9-alpine3.13
# LABEL maintainer="londonappdeveloper.com"

# RUN apk --no-cache add \
#     build-base \
#     libffi-dev \
#     openssl-dev \
#     libc-dev \
#     linux-headers \
#     libressl-dev \
#     musl-dev \
#     libressl

# RUN pip install --upgrade pip
# ENV PYTHONUNBUFFERED 1

# COPY ./requirements.txt /requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
# COPY ./app /app


# WORKDIR /app
# EXPOSE 8000


# ARG DEV=false


# ENV PATH="/py/bin:$PATH"

FROM python:3.9-alpine3.13
LABEL maintainer="londonappdeveloper.com"

RUN apk add --no-cache gfortran  # Add this line

RUN apk add --no-cache \
    build-base \
    python3-dev \
    openblas-dev \
    libexecinfo-dev \
    gcc \
    gfortran \
    musl-dev \
    linux-headers


RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


RUN pip install --no-cache-dir numpy
RUN pip install --no-cache-dir scipy==1.11.4
RUN pip install --no-cache-dir Pillow

# COPY ./app /app

# WORKDIR /app
WORKDIR /app
COPY . .
#COPY ./services /app/services


EXPOSE 8000

ARG DEV=false
ENV PATH="/py/bin:$PATH"
