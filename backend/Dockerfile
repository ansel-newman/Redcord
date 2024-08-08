# Use the official Python 3.10.1 image from the Docker Hub
FROM python:3.10.1
WORKDIR /backend
COPY . /backend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Make port 5000 available to the world outside this container
EXPOSE 5000

ENV NAME World
CMD ["python", "app.py"]
