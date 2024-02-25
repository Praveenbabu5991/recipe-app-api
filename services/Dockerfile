# # Stage 1: Build dependencies
# FROM python:3.9 AS builder

# # Set the working directory to /app
# WORKDIR /app

# # Copy the requirements file to /app
# COPY ./services/requirements.txt .

# # Install dependencies to /app
# RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Create the final image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to /app
COPY ./services/requirements.txt .

# Install dependencies to /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to /app
 COPY .. .


# Copy similarity_service.py into the container

# Expose any ports the app is running on
EXPOSE 8000


# Command to run on container start
# CMD ["python", "similarity_service.py"]
CMD ["sh", "-c", "python ./services/similarity_service.py && python ./services/messaging_service.py"]



