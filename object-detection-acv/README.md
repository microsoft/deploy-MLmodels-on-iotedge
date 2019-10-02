# People Detection on Azure IoT Edge with Azure Custom Vision

In this tutorial, we introduce how to deploy a people detection service on Azure IoT Edge with Azure Custom Vision (ACV) service.

In this example, we deploy a pre-trained object detection model to the edge device. When the image data is generated from a process pipeline and fed into the edge device, the deployed model can make predictions right on the edge device without accessing to the cloud. 

Azure IoT Edge enables user to deploy and manage business logic on the edge in the form of `modules`. Any business logic, including trained machine learning model, need to be built into a docker image. When deployed, each running docker container is called a `module`. In this workflow, we deploy two modules on IoT Edge. These two modules are `ImageCaptureOD`, `PeopleDetectionService`, the source code of whichcan be found at [./modules](./modules). `PeopleDetectionService` contains a trained model together with other driver files exported from [ACV service] (https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/home). User only need to provide a set of tagged custom images and the ACV service will train the object detection model in the backend. When satisfied with the model performance, user can export the trained model into a preferred format and deploy it at user's choice. In this workflow, we export the trained model from ACV service and unzip it into `PeopleDetectionService` directory. `ImageCaptureOD` is a module that accepts a video footage as input, breakdown video into frames, send each frame to `PeopleDetectionService` module, receive output from `PeopleDetectionService` module, annotated each frame, display annotated frames as a video footagle in the web browser. This module is modified based on this [sample tutorial](https://azure.microsoft.com/en-us/resources/samples/custom-vision-service-iot-edge-raspberry-pi/). When deployed, `PeopleDetectionService` module takes a video frame supplied from from `ImageCaptureOD` module and output the predicted objects with their prediction probability and bounding box corrodinates.


We perform following steps for the deployment.

- Step 1: Create Azure resources including IoT Hub, IoT Edge identity, Azure Container Registry (ACR), etc.
- Step 2: Provision and Configure IoT Edge Device.
- Step 3: Build and register two docker images in ACR. These images will be used to create two docker containers (modules) running on the edge device. 
- Step 4: Deploy two modules on IoT Edge Device.
- Step 5: Test the people-detector-service Module.
- Step 6: Tear down Azure resources and clean up edge device.


To get started with the tutorial, please proceed with following steps **in sequential order**.

 * [Prerequisites](#prerequisites)
 * [Steps](#steps)
 * [Cleaning up](#cleanup)

<a id='prerequisites'></a>
## Prerequisites
1. Linux (x64) 
2. [Anaconda Python](https://www.anaconda.com/download)
3. [Docker](https://docs.docker.com/v17.12/install/linux/docker-ee/ubuntu) installed
4. [Azure account](https://azure.microsoft.com)

The tutorial was developed on an [Azure Ubuntu
DSVM](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro),
which addresses the first three prerequisites.

<a id='steps'></a>
## Steps
Please follow these steps to set up your environment and run notebooks.  They setup the notebooks to use Docker and Azure seamlessly.

1. Add your user to the docker group: 
   ```
   sudo usermod -aG docker $USER
   newgrp docker
   ```
   To verify whether you have correct configuration, try executing `docker ps` command. You should not get `permission denied` errors.

2. Navigate to the repo's directory

3. Create the Python virtual environment using the environment.yml:
   ```
   conda env create -f environment.yml
   ```
4. Activate the virtual environment:
   ```
   source activate deployment_env
   ```
5. Register the created conda environment to appear as a kernel in the Jupyter notebooks.
```python -m ipykernel install --user --name deployment_env --display-name "Python (deployment_env)"
```
6. Login to Azure:
   ```
   az login
   ```
7. If you have more than one Azure subscription, select it:
   ```
   az account set --subscription <Your Azure Subscription>
   ```
8. Start the Jupyter notebook server in the virtual environment:
   ```
   jupyter notebook
   ```
9. Select correct kernel: set the kernel to be `Python [conda env: deployment_env]`(or `Python 3` if that option does not show).

10. After following the setup instructions above, run the Jupyter notebooks in order starting with the first notebook [01_AzureSetup.ipynb](./01_AzureSetup.ipynb).

<a id='cleanup'></a>
## Cleaning up
To remove the conda environment created see [here](https://conda.io/projects/continuumio-conda/en/latest/commands/remove.html). The [last Jupyter notebook](./06_TearDown.ipynb)  also gives details on deleting Azure resources associated with this repository.


## Reference
- [Azure IoT Edge](https://docs.microsoft.com/en-us/azure/iot-edge/how-iot-edge-works)
- [Understand Azure IoT Edge modules](https://docs.microsoft.com/en-us/azure/iot-edge/iot-edge-modules)
- [Sample - Custom Vision + Azure IoT Edge](https://azure.microsoft.com/en-us/resources/samples/custom-vision-service-iot-edge-raspberry-pi/)
- [Azure Custom Vision service](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/home)

# Contributing
This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repositories using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
