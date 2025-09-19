FROM python:latest
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
# Add environment variables
# ENV SENDER_EMAIL=""
# ENV RECEIVER_EMAIL=""
# ENV APP_PASSWORD=""
CMD ["python","main.py"]