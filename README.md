# nm21

## Exploring functional currents across brain regions during choice behaviour

https://colab.research.google.com/drive/1KmwFNJHOxzffTq0twazwbu-nfH8Qe4ED?usp=sharing

*Proposal*

In the context of a learned stimulus response task, animals may respond in unpredictable ways. In the Steinmetz wheel turning task, animals are shown gratings and must turn a wheel left or right to report the grating with the greater contrast. Mice learn to perform this task with high accuracy but often make mistakes or turn the wheel when there is no instructional stimulus (error trials). Multiple regions are implicated in choice behavior, though the temporal dynamics of information flow across these structures or how this relates to behaviour is yet to be determined.

To address this, we plan to model the temporal dynamics of the neural activity across the task using a multi-region RNN approach (CURBD). In this model each artificial neuron in the network is trained to reproduce the spiking activity of a corresponding biological neuron, as measured by a similarity metric. To ensure that the model is valid, we will measure how well the functional connectivity of the model resembles known biological connectivity and correlation.

From this, we obtain a connectivity matrix from which we can infer directional currents between  and into decision regions. This approach allows us to explore how the strength and timing of interactions between these regions drives behavior in the discrimination task and how these interactions differ between success and error trials.
