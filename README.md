Docker part
1. Build docker image: docker build -t jirkako/flask_k8s_example:tag .  
The tag should be a new version of image. 

2. Push to docker registry: docker push jirkako/flask_k8s_example:6  

Kubernetes part
1. minikube start
2. Run minikube dashboard: minikube dashboard
3. Update image tag in k8s_deployment.yaml
4. Apply all services:  
kubectl apply -f k8s_deployment.yaml  
kubectl apply -f k8s_service.yaml  
kubectl apply -f pv.yaml  
kubectl apply -f pvc.yaml  

5. Play around with kubernetes  
Try:  
kubectl get pods  
kubectl get services  
kubectl get namespaces  
kubectl get pv  
kubectl get pvc  
debuggin in container: kubectl exec -it <pod> -- /bin/bash  
(exit from container ctrl+p then ctrl+q)  

6. Look at Flask app, expose with:  
minikube service my-service   
(see my-service in k8s_service.yaml)  

7. Test out self-healing, try killing a pod. Go to the /shutdown endpoint to kill it.  
8. Play with scaling:   
set different number of replicas in k8s_deployment (you have to re-apply)  
9. Test out the volume:  
Open Postman on your PC.  
Send a Post request in JSON format.   
Set the URL to service URL/data  
(service URL is printed out when service is exposed - step 5).  
Go to URL/show endopoint. You should see your data there.  
The data is saved in the app but also mirrored to a volume.    
Try restarting the pod (by killing it on /shutdown endpoint, or change number of replicas to 0 and then 1).  
The data should still be present.  