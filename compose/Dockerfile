FROM drones_requirements

# copy project
COPY . /usr/src/app

EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]

