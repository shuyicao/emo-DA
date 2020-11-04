# Causal Relationships between Emotions and Dialogue Acts in Human Conversation

## Setup

### Python
The causal discovery experiments are implemented using **Causal Discovery Toolbox** https://fentechsolutions.github.io/CausalDiscoveryToolbox/html/index.html

Additional R libraries are required while using the _cdt_ framework such as bnlearn, kpcalg, pcalg and RCIT. Please see [CausalDiscoveryToolbox](https://github.com/FenTechSolutions/CausalDiscoveryToolbox) for further details.


### R
The FCI model is implemented using standard R package pcalg. Install the latest pcalg package https://cran.r-project.org/web/packages/pcalg/index.html



## Datasets

### DailyDialogue
The [DailyDialogue](https://arxiv.org/abs/1710.03957) data used for this project is parsed using https://github.com/jojonki/DailyDialog-Parser/blob/master/parser.py.

### Switchboard Dialogue Act Corpus (SwDA)
The [SwDA](https://web.stanford.edu/~jurafsky/ws97/) data used for replication of the Dialog Act tagger model is a parsed version from https://github.com/NathanDuran/Switchboard-Corpus. 



## Automatic Dailog Act Classification
To obtain DA labels for the DailyDialogue data, we use the hierarchical encoder with CRF, proposed by [Kumar et al. (2017)](https://arxiv.org/abs/1709.04250). The original source code can be found at https://github.com/YanWenqiang/HBLSTM-CRF. 

Slight changes has been made on the code to adapt to our own research. 
Please refer to the [forked repo](https://github.com/shuyicao/HBLSTM-CRF).



## Experiments

### Data
The [input data](https://github.com/shuyicao/emo-DA/tree/master/input%20data) folder contains 4 csv files:
* **annotated.csv** - 65 manually annotated DailyDialogue sessions 
* **pred.csv** - The rest of all dialogue sessions from the parsed DailyDialogue dataset with predicted DA labels through automatic dailog act classification
* **trans_curr.csv** - transformed binary data including current utterances' emotion and DAs, where each column represents an individual type of emotion/DA and each row represents a single utterance (0 for non-existence and 1 or existence)
* **trans_prev.csv** - transformed binary data including previous utterance's emotion and current utterance's DA, same format with trans_curr.csv. 

### Qualitative analysis
The [case study.py](https://github.com/shuyicao/emo-DA/blob/master/case%20study.py) file contains our case study counting co-occurences of emotion-DA pairs for each utterance of annotated data.

The [case study fisher.R](https://github.com/shuyicao/emo-DA/blob/master/case%20study%20fisher.R) file contains the Fisher's exact test performed on discovered relationships from the case study.


### Quantitative analysis
The [causal_variable_fci.R](https://github.com/shuyicao/emo-DA/blob/master/causal_variable_fci.R) file contains our FCI model for discovering causal relationships between emotion and DA as two random variables in different contexts.

The [causal_variable_gies_mmpc.py](https://github.com/shuyicao/emo-DA/blob/master/causal_variable_gies_mmpc.py) file contains our MMPC and GIES models for same experiment as in causal_variable_fci.R. 

The [causal_specific_types.py](https://github.com/shuyicao/emo-DA/blob/master/causal_specific_types.py) file performs causal discovery on relationships between specific types of emotion and DA, using GIES and MMPC algorithms in two contexts:
* current utterance's emotion vs. current utterance's DA
* previous utterance's emotion vs. current utterance's DA


## References

Juraksky, D. (1997). Switchboard SWBD-DAMSL Shallow-Discourse-Function Annotation Coders Manual. Retrieved from https://web.stanford.edu/~jurafsky/ws97/manual.august1.html.

Kalainathan, D. & Goudet, O. (2019). Causal Discovery Toolbox: Uncover Causal Relationships in Python. arXiv preprint arXiv: 1903.02278.

Kumar, H., Agarwal, A., Dasgupta, R., Joshi, S. & Kumar, A. (2017). Dialogue Act Sequence
Labeling using Hierarchical encoder with CRF. arXiv preprint arXiv:1709.04250.

Li, Y., Shen, X., Li, W., Cao, Z. & Niu, S. (2017). DailyDialog: A Manually Labelled Multi-turn
Dialogue Dataset. arXiv preprint arXiv:1710.03957.


