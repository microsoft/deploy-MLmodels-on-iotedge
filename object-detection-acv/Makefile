.ONESHELL:
SHELL=/bin/bash

define PROJECT_HELP_MSG
Makefile for testing notebooks
Make sure you have edited the dev_env_template files and renamed it to .dev_env
All the variables loaded in this makefile must come from the .dev_env file

Usage:
	make test					run all notebooks
	make clean					delete env and remove files
endef
export PROJECT_HELP_MSG
env_location=.dev_env
PWD:=$(shell pwd)
include ${env_location}


help:
	echo "$$PROJECT_HELP_MSG" | less


test: setup test-notebook1 test-notebook2 test-notebook3 test-notebook4 test-notebook5 test-notebook6
	@echo All Notebooks Passed

setup:
	conda env create -f environment.yml
ifndef TENANT_ID
	@echo starting interactive login
	az login -o table
else
	@echo using service principal login
	az login -t ${TENANT_ID} --service-principal -u ${SP_USERNAME} --password ${SP_PASSWORD}
endif


test-notebook1:
	source activate deployment_env
	@echo Testing 01_AzureSetup.ipynb
	papermill 01_AzureSetup.ipynb out_01_AzureSetup.ipynb \
		--log-output \
		--no-progress-bar \
		-k python3 \
		-p subscription_id ${SUBSCRIPTION_ID} \
		-p resource_group ${RESOURCE_GROUP} \
		-p resource_region ${RESOURCE_REGION} \
		-p iot_hub_name ${IOT_HUB_NAME} \
		-p device_id ${DEVICE_ID} \
		-p acr_name ${ACR_NAME} 

test-notebook2:
	source activate deployment_env
	@echo 02_IoTEdgeConfig.ipynb
	papermill 02_IoTEdgeConfig.ipynb out_02_IoTEdgeConfig.ipynb \
		--log-output \
		--no-progress-bar \
		-k python3

test-notebook3:
	source activate deployment_env
	@echo 03_BuildRegisterImage.ipynb
	papermill 03_BuildRegisterImage.ipynb out_03_BuildRegisterImage.ipynb \
		--log-output \
		--no-progress-bar \
		-k python3 \
		-p image1_name ${IMAGE1_NAME} \
		-p image2_name ${IMAGE2_NAME}

test-notebook4:
	source activate deployment_env
	@echo Testing 04_DeployOnIOTedge.ipynb
	papermill 04_DeployOnIOTedge.ipynb out_04_DeployOnIOTedge.ipynb \
		--log-output \
		--no-progress-bar \
		-k python3 \
		-p module1_name ${MODULE1_NAME} \
		-p module2_name ${MODULE2_NAME}

test-notebook5:
	source activate deployment_env
	@echo 05_TestPeopleDetectionModule.ipynb
	papermill 05_TestPeopleDetectionModule.ipynb out_05_TestPeopleDetectionModule.ipynb \
		--log-output \
		--no-progress-bar \
		-k python3 

test-notebook6:
	source activate deployment_env
	@echo 06_TearDown.ipynb
	papermill 06_TearDown.ipynb out_06_TearDown.ipynb \
		--log-output \
		--no-progress-bar \
		-k python3 


test-notebook-debug1:
	source activate deployment_env
	@echo debug_01_DeployPeopleDetectionModuleIOTedge.ipynb
	export PYTHONPATH=${PWD}:${PYTHONPATH}
	cd debug
	papermill debug_01_DeployPeopleDetectionModuleIOTedge.ipynb out_debug_01_DeployPeopleDetectionModuleIOTedge.ipynb \
		--log-output \
		--no-progress-bar \
		-k python3 \
		-p module2_name ${MODULE2_NAME}

remove-notebook:
	rm -f out*.ipynb

clean: remove-notebook
	conda remove --name deployment_aml -y --all
	rm -rf aml_config
	rm -rf __pycache__
	rm -rf .ipynb_checkpoints
	rm *.jpg
	rm -rf azureml-models
	rm driver.py img_env.yml model_resnet_weights.h5

notebook:
	source activate deployment_env
	jupyter notebook --ip=0.0.0.0 --no-browser




