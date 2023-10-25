
Python Flask App with Kubernetes Deployment

To run the app:

1. Build the Docker image:

```
docker build -t app .
```
Run the Docker image:

```
docker run -p 8080:8080 app
```
To push to the Repo:

```
docker push thiruhari9699/flaskapp01
```


2. Deploy the app to Kubernetes:

```
kubectl apply -f Deployment.yaml -f service.yaml
```

3. Get the IP address of the Service:

```
kubectl get service my-app-service
```

4. Access the app at the following URL:

```
http://<service-ip>:80/
```

To build the Helm chart:

```
helm package my-app
```

To deploy the Helm chart:

```
helm install my-app ./my-app
```

To access the app:

```
http://<service-ip>:80/
```

To uninstall the Helm chart:

```
helm uninstall my-app
```

To scale the app:

```
kubectl scale deployment my-app-deployment --replicas 3
```

To delete the app:

```
kubectl delete deployment my-app-deployment
kubectl delete service my-app-service
```

Dockerfile

```
FROM python:3.10

# Install the required dependencies
RUN pip install flask redis

# Copy the application code to the container image
COPY . /app

# Set the working directory
WORKDIR /app

# Expose port 5000
EXPOSE 8080

# Command to start the application
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]
```

deployment.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: thiruhari9699/flaskapp01:latest
        ports:
        - containerPort: 8080
```

service.yaml
```

apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080

```

