# python_flask_app
This project demonstrates the use of dockerisation of python flask application,building and  pushing the docker image is not done manaually but automated pipeline script using jenkins tool provisioed  on an ec2 instance within aws infrastructure.
Once the docker image has been pushed into Dockerhub, it is then deployed using kubernetes either minikube or aws eks with the help of the deplopyment.yaml file and service.yaml created within the kubernetes directory
