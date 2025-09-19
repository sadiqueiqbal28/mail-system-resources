FROM python:latest
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
CMD ["python","main.py"]
# Add ENV with your values
#ENV SENDER_EMAIL=""
#ENV RECEIVER_EMAIL=""
#ENV APP_PASSWORD=""

# App password should be of the same account of the sender's email

# To build the image after  adding the values
# Build: (To build the image)
# docker build -t <docker-repo-name>/<name-of-app> .
# Run: (To run the container)
# docker run -d --name <container-name> 