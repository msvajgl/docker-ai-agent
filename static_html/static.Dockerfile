FROM python:3.13.4-slim-bullseye

WORKDIR /app

# RUN mkdir -p /static_folder
COPY ./src .

# RUN echo "hello" > index.html 

# python -m http.server 8000
CMD ["python", "-m", "http.server", "8000"]

# docker run -it -p 3000:8000 pyapp