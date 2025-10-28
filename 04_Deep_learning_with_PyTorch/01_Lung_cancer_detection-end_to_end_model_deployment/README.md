# Automatic detection of malignant tumors in the lungs using Computed Tomographies (CT scans)'

This is an updated and debugged implementation of the book "Deep Learning with PyTorch" (Eli Stevens, Luca Antiga, and Thomas Viehmann). https://github.com/deep-learning-with-pytorch/dlwpt-code/tree/master

Download data (110 GB when uncompressed): https://luna16.grand-challenge.org/

We will focus on the technical challenges of accelerating training through caching large exotic input files, implementing GPU parallel computing, and ensuring the Python application is production-ready.

If you clone this git, the app will work, just be aware of your memory/cpu/gpu resources.

<img width="670" height="696" alt="image" src="https://github.com/user-attachments/assets/edc8d560-e02a-49ee-b2ea-cf6dcc338f51" />

### Data source: The LUNA Grand Challenge

The CT scans come from the LUNA (Lung Nodule Analysis) Grand Challenge. The LUNA Grand Challenge (https://luna16.grand-challenge .org/Description) is the combination of an open dataset with high-quality labels of patient CT scans (many with lung nodules) and a public ranking of classifiers against the data.

### Deployment overview:

<img width="1130" height="798" alt="image" src="https://github.com/user-attachments/assets/3e61d657-b256-47d1-934c-124341b81299" />
