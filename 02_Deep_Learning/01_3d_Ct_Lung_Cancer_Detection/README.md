# Automatic detection of malignant tumors in the lungs using Computed Tomographies (CT scans)

This is an implementation of the book "Deep Learning with PyTorch" (Eli Stevens, Luca Antiga, and Thomas Viehmann). https://github.com/deep-learning-with-pytorch/dlwpt-code/tree/master

This project is an example of a production ready app. It involved technical challenges such as: accelerating training through caching large exotic input files, implementing GPU for parallel computing, and ensuring the models were learning the expected problem.

Check zipped jupyter notebook for usage and demo.

<img width="670" height="696" alt="image" src="https://github.com/user-attachments/assets/edc8d560-e02a-49ee-b2ea-cf6dcc338f51" />

### Data source: The LUNA Grand Challenge

The CT scans come from the LUNA (Lung Nodule Analysis) Grand Challenge. The LUNA Grand Challenge (https://luna16.grand-challenge .org/Description) is the combination of an open dataset with high-quality labels of patient CT scans (many with lung nodules) and a public ranking of classifiers against the data.

Download data: (110 GB when uncompressed): https://luna16.grand-challenge.org/


### Deployment overview:

<img width="1130" height="798" alt="image" src="https://github.com/user-attachments/assets/3e61d657-b256-47d1-934c-124341b81299" />


