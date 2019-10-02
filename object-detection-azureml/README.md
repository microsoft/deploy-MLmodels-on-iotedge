# People Detection on Azure IoT Edge with AzureML

In this tutorial, we introduce how to deploy a people detection service on Azure IoT Edge using Azure Machine Learning (AzureML) service. We deploy a pre-trained MaskRCNN (Pytorch) object detection model to the edge device. When the image data is generated from a process pipeline and fed into the edge device, the deployed model can make predictions right on the edge device without accessing to the cloud. 

Azure IoT Edge enables user to deploy and manage business logic on the edge in the form of `modules`. Any business logic, including trained machine learning model, need to be built into a docker image. When deployed, each running docker container is called a `module`. In this workflow, we deploy one module - the `people-detector-service` module on IoT Edge. The model file and other required driver files will be generated when running [031_RegisterModel.ipynb](./031_RegisterModel.ipynb) and [032_DevelopModelDriver.ipynb](032_DevelopModelDriver.ipynb) notebooks.

We perform following steps for the deployment.

- Step 1: Create Azure resources including IoT Hub, IoT Edge identity, AzureML workspace, etc.
- Step 2: Provision and Configure IoT Edge Device.
- Step 3: Develop an ML model, register it in Azure Container Service (ACR) and build it into a docker image through AzureML. This docker image will be used to create a docker container (module) running on the edge device. 
- Step 4: Deploy the ML module on IoT Edge Device.
- Step 5: Test the `people-detector-service` Module.
- Step 6: Tear down Azure resources and clean up the edge device.


To get started with the tutorial, please proceed with following steps **in sequential order**.

 * [Prerequisites](#prerequisites)
 * [Steps](#steps)
 * [Cleaning up](#cleanup)

<a id='prerequisites'></a>
## Prerequisites
1. Linux (x64) with GPU enabled.
2. [Anaconda Python](https://www.anaconda.com/download)
3. [Docker](https://docs.docker.com/v17.12/install/linux/docker-ee/ubuntu) installed.
4. [Azure account](https://azure.microsoft.com).

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
   source activate deployment_aml
   ```
5. Register the created conda environment to appear as a kernel in the Jupyter notebooks.
```python -m ipykernel install --user --name deployment_aml --display-name "Python (deployment_aml)"
```
5. Login to Azure:
   ```
   az login
   ```
6. If you have more than one Azure subscription, select it:
   ```
   az account set --subscription <Your Azure Subscription>
   ```
7. Start the Jupyter notebook server in the virtual environment:
   ```
   jupyter notebook
   ```
8. Select correct kernel: set the kernel to be `Python [conda env: deployment_aml]`(or `Python 3` if that option does not show).

9. After following the setup instructions above, run the Jupyter notebooks in order starting with the first notebook [01_AzureSetup.ipynb](./01_AzureSetup.ipynb).

<a id='cleanup'></a>
## Cleaning up
To remove the conda environment created see [here](https://conda.io/projects/continuumio-conda/en/latest/commands/remove.html). The [last Jupyter notebook](./06_TearDown.ipynb)  also gives details on deleting Azure resources associated with this repository.


## Reference
- [Azure IoT Edge](https://docs.microsoft.com/en-us/azure/iot-edge/how-iot-edge-works)
- [Understand Azure IoT Edge modules](https://docs.microsoft.com/en-us/azure/iot-edge/iot-edge-modules)
- [Azure Machine Learning service](https://docs.microsoft.com/en-us/azure/machine-learning/service/overview-what-is-azure-ml)

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
