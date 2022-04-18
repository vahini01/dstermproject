# dstermproject
Distributed ML

Setting up Ray Cluster in Google Cloud Engine

1. Install the Python dependency

$ pip install -U "ray[default]" google-api-python-client 

2. Set the GOOGLE_APPLICATION_CREDENTIALS environment variable 
https://cloud.google.com/docs/authentication/getting-started#create-service-account-console 
(Install the gcloud API and create a service account)

3. Set the cluster instructions in .yaml files

$ ray up -y config.yaml

5. Copy the files to cluster

$scp path_to_source_file server:path_to_destination_file

7. Start the cluster

$ ray attach /Users/vahini/Documents/spring2022/ds/raysgd/final_work/node8/node8.yaml

8. Start the Ray

$ray start --address='10.128.0.21:6379'

9. Use ray.init(address='auto') before backend

10. Run the code using the below command

$ time python filename.py

11. shutdown the cluster

$ray down -y config.yaml
