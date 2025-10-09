# Introduction to the use case

This is an implementation of the book "Deep Learning with PyTorch" (Eli Stevens, Luca Antiga, and Thomas Viehmann). https://github.com/deep-learning-with-pytorch/dlwpt-code/tree/master

Our goal is to give you the tools to deal with situations where things aren’t working. In order to present these ideas and techniques, we’ve chosen automatic detection of malignant tumors in the lungs using only a CT scan of a patient’s chest as input.

We will focus on the technical challenges of accelerating training through caching large exotic input files, implementing GPU parallel computing, and ensuring the Python application is production-ready.



### Data source: The LUNA Grand Challenge

The CT scans we were just looking at come from the LUNA (Lung Nodule Analysis) Grand Challenge. The LUNA Grand Challenge (https://luna16.grand-challenge .org/Description) is the combination of an open dataset with high-quality labels of patient CT scans (many with lung nodules) and a public ranking of classifiers against the data.


### Deployment overview:

<img width="1130" height="798" alt="image" src="https://github.com/user-attachments/assets/3e61d657-b256-47d1-934c-124341b81299" />
