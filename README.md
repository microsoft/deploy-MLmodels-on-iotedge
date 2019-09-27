---
page_type: sample
languages:
- csharp
products:
- dotnet
description: "Add 150 character max description"
urlFragment: "update-this-to-unique-url-stub"
---

# Official Microsoft Sample

<!-- 
Guidelines on README format: https://review.docs.microsoft.com/help/onboard/admin/samples/concepts/readme-template?branch=master

Guidance on onboarding samples to docs.microsoft.com/samples: https://review.docs.microsoft.com/help/onboard/admin/samples/process/onboarding?branch=master

Taxonomies for products and languages: https://review.docs.microsoft.com/new-hope/information-architecture/metadata/taxonomies?branch=master
-->
# Deploy Machine Learning Models on Azure IoT Edge

This repository contains examples and best practices for deploying machine learning models on Azure IoT Edge, provided as Jupyter notebooks. The examples detail our learnings on two key qustions: where the model is built and what is the IoT Edge device for deployment. 


The table below lists the recommender algorithms currently available in the repository. Notebooks are linked under the Environment column when different implementations are available.

| Task | Model Built Environment | IoT Edge Device | Description | 
| --- | --- | --- | --- |
| Object Detection | Azure Machine Learning | Ubuntu VM | Pytorch, pretrained MaskRCNN model | 
| Object Detection | Azure Custom Vision service | Ubuntu VM | Tensorflow, pretrained model, fine-tuned with 50 custom images| 
| Object Detection | Azure Custom Vision service | Data Box Edge (DBE) | Tensorflow, pretrained model, fine-tuned with 50 custom images | 



## Prerequisites

Outline the required components and tools that a user might need to have on their machine in order to run the sample. This can be anything from frameworks, SDKs, OS versions or IDE releases.

## Setup

Explain how to prepare the sample once the user clones or downloads the repository. The section should outline every step necessary to install dependencies and set up any settings (for example, API keys and output folders).

## Runnning the sample

Outline step-by-step instructions to execute the sample and see its output. Include steps for executing the sample from the IDE, starting specific services in the Azure portal or anything related to the overall launch of the code.

## Key concepts

Provide users with more context on the tools and services used in the sample. Explain some of the code that is being used and how services interact with each other.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
