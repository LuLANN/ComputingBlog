title: Brief Intro to the AI behind Self Driving Cars
subtitle: How can cars navigate themselves in a complex environment?
date: 2018-11-15
author: Lucy An

_Note_: This post is a summary of the discussion about the
how self driving cars work and how they can be implemented ... 

### What is Reinforcement Learning?
----
Reinforcement learning is the trial and error process of the computer teaching _itself_ how to complete a certain task. Unlike other neural networks, progression from failure to success is dependant **entirely** on rewards. A reward is an action-reaction event where a decision is made and its aftermaths is observed and obtained by the AI to further its understanding of the task in question. 

There are two main objects in reinforcement learning:

* The Environment
* The Agent


### 1.The Environment
----

The "environment" is usually the set of states that the "agent" can influence to gain rewards by conducting various "actions".
In this case, the environment would be the physical simulation of the lanes, and grass, and other cars.

### 2. The Agent
----

This "agent" does **not** refer to the secret agents that you see in action movies, nor does it refer to the oxidizing/reducing agent that you learning in your chemistry class. An agent in reinforcement learning is something that can interact with its environment by making various actions to **maximize** its reward. The main property of an agent is to have a **state**, which indicates its attributes within an environment. For example, in our simulation, the agent is the car. An action it can make is when to turn at a specific angle, and it's states could be its current speed, displacement, or acceleration. 

![Image](https://www.kdnuggets.com/images/reinforcement-learning-fig1-700.jpg)

### Training the AI
----

In our driverless car simulation, the car needs to first **crash** multiple times to learn to drive on the road. The car receives more points the longer it stays "alive". and with enough trials, the AI will be so good that it will never crash in the **same** environment.

How quickly an AI is able to successfully complete a task is dependant on its features. Insufficient features will cause the AI to be lacking of crucial information for success , while **an excessive amount** will cause the rate of progression to be extremely slow since the AI will be unsure of what data to use or ignore. For example, in order to navigate a car through a series of roads, the AI must gather information such as the displacement between its initial position and that of the nearest turn. If not, the car will surely crash. Furthermore, if the car had an abundance of data it would take extra time to sort out the necesary from the unnecessary.

### Distinct Characteristics of Reinforcement Learning 
----

Besides being dependant on rewards, Reinforcement Learning is also different from traditional neural networks in terms of its network structure. The key difference is that a traditional neural network has the same number of neurons per layer whereas Reinforcement Learning is made up of a network that has multiple neurons in the previous layer, which sends a common neuron to its next layer. This difference in structure allows for faster processing speed.
