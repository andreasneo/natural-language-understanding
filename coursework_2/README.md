#  Neural Machine Translation
My solution for cousework 2 of [Natural Language Understanding,Generation, and Machine Translation](http://www.drps.ed.ac.uk/18-19/dpt/cxinfr11157.htm) course at University of Edinburgh [School of Informatics](http://www.inf.ed.ac.uk).

* Explored the given translation model, which is a bidirectional LSTM with attention, by adding comments and adding more encoder/decoder layers. 
* Augmented  the base code by implementing a lexical model as defined by [Nguyen and Chiang (2017) in section 4](https://arxiv.org/pdf/1710.01329.pdf) 
* Examined the effects of the above modifications on dev-set perplexity, BLEU score, training loss and attention alignments.  

The base code for coursework 2 can be found at https://github.com/demelin/nmt_toolkit.

The augmented code in in [lstm.py](https://github.com/AndreasNeokleous/natural-language-understanding/blob/master/coursework_2/nmt_toolkit/seq2seq/models/lstm.py).

The repository is shared after granting permission from the course organizers.
