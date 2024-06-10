# Using tensorflow/tensorflow:latest Container
FROM tensorflow/tensorflow:latest

# Adjusting the Working Directory
WORKDIR /app

# Importing the Required Libraries
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copying the Project Files
COPY . /app

# Starting Point Command Line
CMD ["python", "/app/trial_tf_app.py"]