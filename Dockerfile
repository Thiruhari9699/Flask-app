FROM python:3.10

# Install the required dependencies
RUN pip install flask redis

# Copy the application code to the container image
COPY . /app

# Set the working directory
WORKDIR /app

# Expose port 8080
EXPOSE 8080

# Command to start the application
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]
