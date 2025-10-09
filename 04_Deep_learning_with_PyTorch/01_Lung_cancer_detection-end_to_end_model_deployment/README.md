# Introduction to the use case

This is an implementation fo the book "Deep Learning with PyTorch" (Eli Stevens, Luca Antiga, and Thomas Viehmann). https://github.com/deep-learning-with-pytorch/dlwpt-code/tree/master

Our goal is to give you the tools to deal with situations where things aren’t working. In order to present these ideas and techniques, we’ve chosen automatic detection of malignant tumors in the lungs using only a CT scan of a patient’s chest as input.

We’ll be focusing on the technical challenges rather than the human impact

Detecting lung cancer early has a huge impact on survival rate, but is difficult to do manually, especially in any comprehensive, whole-population sense. Currently, the work of reviewing the data must be performed by highly trained specialists, requires painstaking attention to detail, and it is dominated by cases where no cancer exists.

Automating this process is going to give us experience working in an uncooperative environment where we have to do more work from scratch, and there are fewer easy answers to problems that we might run into. Once you’re finished, you’ll be ready to start working on a real-world, unsolved problem of your own choosing.



### Our data source: The LUNA Grand Challenge

The CT scans we were just looking at come from the LUNA (LUng Nodule Analysis) Grand Challenge. The LUNA Grand Challenge (https://luna16.grand-challenge .org/Description) is the combination of an open dataset with high-quality labels of patient CT scans (many with lung nodules) and a public ranking of classifiers against the data.


### Deployment overview:

<img width="1130" height="798" alt="image" src="https://github.com/user-attachments/assets/3e61d657-b256-47d1-934c-124341b81299" />
