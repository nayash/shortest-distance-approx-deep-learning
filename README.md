# shortest-distance-approx-deep-learning
Implementation of the paper "Shortest Path Distance Approximation using Deep learning Techniques"

#### Problem Statement
Using traditional methods(Dijkstra's Algo etc) for solving graph problems like shortest path distance is not scalable for very large graphs we see these days like social media graphs. This paper suggests a method to approximate shortest path distances using Deep Learning.

#### Proposed Solution
1. Get your graph data.
2. Use algorithm suggested in <b>Node2Vec</b> paper to find feature vector embeddings for your graph. I have used the implementation of Node2Vec algo provided by original authors of the paper.
3. Prepare your training/test dataset:
      a. Use Node2Vec to find feature embeddings for each of your graph nodes.
      b. Select a small number of landmark nodes (l) from all the nodes (n) of the graph, where l << n.
      c. For each landmark node (l1), find shortest distance between l1 and rest of the nodes of graph. This way you have l*(n-1) edge-distance pairs. 
      d. For each edge (pair of nodes) in your training data, combine the corresponding feature vectors of the nodes using any of suggested binary operations (avergage, concatenation etc).
4. Now you have feature embedding for each edge in your dataset and a corresponding distance. Train the neural net!

#### Results
Note: Even though the problem is formulated as a regression problem, I have used accuracy (a classification metric) to make the improvements in model performance more intuitive.

Baseline: Accuracy=50.57%, MSE=0.56, MAE=0.59
Best MLP (till now): Accuracy=76%, MSE=0.18, MAE=0.34

#### Files in the project
Main project files are <b>data_prep.ipynb</b> and <b>train.ipynb</b>. I have also included a "fun.ipynb" file which has some interesting observations from the project. Node2Vec implementation provided by authors was in python2, so I have converted and included the necessary files in python3 format. This time I have also included all the experiments and results that I captured in the tensorboard.

Graph data is downloaded with gratitude from:

<pre>
@inproceedings{nr,
      title = {The Network Data Repository with Interactive Graph Analytics and 
      Visualization},
      author={Ryan A. Rossi and Nesreen K. Ahmed},
      booktitle = {AAAI},
      url={http://networkrepository.com},
      year={2015}
  }
</pre>
