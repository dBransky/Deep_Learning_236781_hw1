r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**

1.
2.not true we should sample different subsets and mean our results 3.True, the test set cannot be used during 
cross-validation or else the test result will be biased, The test set must stay hidden the entire training process 
4.
"""

part1_q2 = r"""No, my friend's approach isn't justified, our friend is trying to tune a hyper-parameter. The 
appropriate way of tuning hyper parameter's is with a dedicated valid-set which must be different from the test-set. 
Tuning hyper parameter's using the test set is wrong, the test set cannot be used to train the model, it must stay 
hidden from the model or else it may result in unbiased accuracy result and fitting for the best result on the 
test-set """

# ==============
# Part 2 answers

part2_q1 = r""" Generally increasing K may improve generalization of unseen data, although in our 
specific problem-predicting a label for an image, increasing K might lead to unwanted behavior: If k is larger than 
the amount of samples of the same class we will be predicting out label upon neighbors that are surely wrong. If k is 
as large as the data-set itself our result will always be the most common class. 
"""

part2_q2 = r"""1. Using the train-set as a validation set as well is a bad method, since each sample's distance from 
itself is 0. so when trying to evaluate our model/hyper-parameter we will always get a a neighbor with distance 0 
that has the ground truth label of our sample. which means that the best k will always be 1, and therefore gives no 
additional information on our model/hyper-parameter. An additional flaw to this approach is basing out 
hyper-parameter/model upon out training set, which may result in over-fitting. 2.The test-set must stay hidden from 
the model so that our accuracy evaluation is unbiased. This may also result in over-fitting of the training set 
itself, as our model is based upon getting better results on the accuracy set. Also k fold tries to randomize our 
data so our model/hyper-parameter will be evaluated upon unseen data as much as possible, this cannot be achieved when 
validating on the test-set 
"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
The exact value of the margin $\Delta between the scores is meaningless because the weights may 
change (shrink or stretch) over the distance. The scores and their differences are affected by the magnitude of the 
weight, bigger values increase the differences while smaller values decrease the differences In addition the lambda 
scalar may increase of decrease changes in $\Delta so when both are chosen makes the selection of $\Delta arbitrary 
"""

part3_q2 = r"""
1.As we can seen in the pictures above the model is learning the commonly bright pixels of each label, 
so actually it is leaning how each number is commonly written. As we can see in the classification errors, 
the model mistook 5 for 6 since its bottom part resembles that of a circle like 6. The svm model is looking for the 
optimal differentiator between classes, that's why we can that the errors are more ambiguous written numbers. 
2. Both models are similar in the way that they both predict a sample's label with an earlier given set of labelled data. 
however these models are different, Knn labels the sample based on the image that in most similar to it. While the 
linear classifier labels the sample based on the assumption that the data can indeed be split into different types, 
then based on the best differentiation of the data, labels our image into it's unique group. 
"""

part3_q3 = r"""
1.Based upon the graph and our result i would say our learning rate is quite good, if it was low then 
our results would be poor since the model didnt have "time" to reach it's optimal point. If the learning rate was to 
high we would see more fluctuations in the loss graph caused by taking a step to large. 
2.Based on the graph of training and the overall results i'd say we are slightly over-fitting the training set we get an 
accuracy result of 89.1% on the test set while almost 95% on the test set, which means are model has learnt the test set 
in particular, and is therefore getting lower results on unseen data. 
 

"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
