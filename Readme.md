# Classify images in Keras


I was thinking about what I could classify to train a LeNet, and I came
to the idea that I could classify if a picture contains weed or not.

If you don't like the way I comment, or the way I write the code,
readme and so on, just look for another LeNet repository, there are
plenty of them. I don't give a fu** about what do you think, some people
like the way I do it, other people doesn't. I'm writing this for Dee and
for those who wanna learn in another way than at the university.

So, for those who just want to read the code and get a basic idea about
how images classifiers work:

### Installing things

I use python3.6

Then, I've a virtualenv (`virtualenv -p python3 venv`)

After that: `pip install -r requirements.txt`

If ya don't get this brah, then I wouldn't recommend ya to start with
Convolutional Networks ^^

### Downloading images from google

Inside the `download_images.py` script, you'll find an script in the
comments.

1- Search for some pictures on Google (e.g. "weed")

2- Scroll down to get more pictures in the html

3- Open the browser console

4- Write the JS script I put on `download_images.py` (first I than
Enter, then II and so on)

5- At the end you should have a url.txt file in your Downloads folder.

### Training your model

As you can notice, I'm not giving a pre-trained model because if I do
it, you'll say your friends "hey, I've a program that can say if a pic
contains weed or not" and yeah that's true, but it would be better if
you say "hey, I've a program that can say if a pic contains weed or not,
and I trained it by myself!"


To train the model, you need at least two folders in "images"


I'm tired of writing...

#### train:

python train_network.py --dataset images --model {name_of_your_future_model}


#### test:

python test_network.py --model {your_trained_model} --image examples/plant1.jpg


there would be a picture called "plot.png" so you can see how good it trained.

THIS PROJECT IS A MOCK-UP!!!!!! so, don't expect a great accuracy.

For improving accuracy:

- More Weed Pictures and better dataset in general
- Use an `early_stop_criterion` for overfitting
- Use Googlenet instead of LeNet

