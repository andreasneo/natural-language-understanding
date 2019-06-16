# Recurrent Neural Network Language Model

My solution for coursework 1 of [Natural Language Understanding,Generation, and Machine Translation](http://www.drps.ed.ac.uk/18-19/dpt/cxinfr11157.htm) course at University of Edinburgh [School of Informatics](http://www.inf.ed.ac.uk).


* Implemented an RNN language model given the mathematical equations. 
* Trained and evaluated the model to learn the agreement rules between subject and predicate in a sentence.

The RNN model can be found in [code/rnn.py](https://github.com/AndreasNeokleous/natural-language-understanding/blob/master/coursework_1/code/rnn.py).
These functions were implemented following the RNN equations of cross-entory, output layer weights, error propagation, softmax, weight updates:
* predict -> predict an output sequence for a given input sequence
* acc_deltas -> accumulate update weights for the RNNs weight matrices, standard Back Propagation
* acc_deltas_bptt -> accumulate update weights for the RNNs weight matrices, using Back Propagation Through Time
* compute_loss -> compute the (cross entropy) loss between the desired output and predicted output for a given input sequence
* compute_mean_loss -> compute the average loss over all sequences in a corpus
* acc_deltas_np -> accumulate update weights for the RNNs weight matrices, standard Back Propagation -- for number predictions
* acc_deltas_bptt_np -> accumulate update weights for the RNNs weight matrices, using Back Propagation Through Time -- for number predictions
* compute_acc_np -> compute the accuracy prediction -- for number predictions
* compute_loss_np -> compute the loss between predictions y for x, and desired output d -- for number predictions
* compare_num_pred -> compute the probability between predictions


The repository is shared after granting permission from the course organizers.
