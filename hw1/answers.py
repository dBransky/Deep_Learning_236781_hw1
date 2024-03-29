r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
1.Not true, in-sample error is the error we get upon evaluating the accuracy of our model on the train 
set, therefore the in-sample error can be measured using only the train set. not the test set. 
2.Not true, first if the data is somehow arranged in a certain patten,for example our data has classes numbered 1,2....
if our data is arranged by classed then splitting the data without randomizing it will harm our model's accuracy on 
unseen data. second we must split our data so that there is enough samples to train our model and prevent over-fitting, 
if our train set is to small we may over-fit the training set, on the other hand if we split the test set to small 
then we wont be able to properly evaluate our model. that's why it is commonly advised to split the data in a 90/10,
80/20,70/30,60/40 ratio, these ratios may produce different results and may require validation. 
Splitting depends on our data, its arrangement and it's size 
3.True, the test set cannot be used during cross-validation or else the test result will be biased, The test set must 
stay hidden for the entire training process.
4.True, when preforming cross-validation we validate different models/hyper-parameters against the train set, inorder to
keep the results unbiased we split the training set into a train set and a validation set,
the validation set acts as a proxy of test set which is used to evaluate the model's generalization.
In other world we test the model/hyper-parameter's generalization with the validation set"""

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
The exact value of the margin $\Delta$ between the scores is meaningless because the weights may 
change (shrink or stretch) over the distance. The scores and their differences are affected by the magnitude of the 
weight, bigger values increase the differences while smaller values decrease the differences In addition the lambda 
scalar may increase of decrease changes in $\Delta$ so when both are chosen makes the selection of $\Delta$ arbitrary 
"""

part3_q2 = r"""
1.As we can seen in the pictures above the model is learning the commonly bright pixels of each label, 
so actually it is leaning how each number is commonly written. As we can see in the classification errors, 
the model mistook 5 for 6 since its bottom part resembles that of a circle like 6. The svm model is looking for the 
optimal differentiator between classes, that's why we can that the errors are more ambiguous written numbers. 
2. Both models are similar in the way that they both predict a sample's label with an earlier given set of labelled
data. 
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

part4_q1 = r"""The ideal plot is a unified horizontal line along Y=0 axis, in other words a perfect $y^{(i)} - \hat{ 
y}^{(i)}=0$ for each sample, we can see that after training our model we've received a more uniformed and closer to 0 
spread of the samples. We can also see that in the 5 best features plot there is a correlation between the $\hat{y}$ 
and the distance from zero, (somewhat of a curve) this isn't the case with the last plot, what brings us to believe 
that our model fits the data better than the top 5 correlation model. 


"""

part4_q2 = r"""
1. Yes it is still considered a linear regression, even though we've added non-linear features we are 
still solving a linear equation $Z=WX+b$
2. Yes we can fit any non linear function to our features, we can engineer 
our features as we like.
3.Adding non-linear features may allow us to be able to separate data better, 
data that cannot be linearly separated. since we are only adding features to our model the model will still search 
for linear separator but upon a higher dimension. So if we had D features and added D' non-linear features our 
hyperplane's dimension will be of (D+D'-1) instead to (D-1) """

part4_q3 = r"""1. Using np.logspace allows us to search for a hyper-parameter upon a logarithmic scale, which allows 
us to test a wider range of values with less samples.
2.We've folded our train data 3 times and for each fold tested every combination of degree(3),lambda(20) to sub total of
$20*3*3$ =180 times fitted.
 """

# ==============
