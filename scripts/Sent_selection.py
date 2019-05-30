# Uses BERT language modeling to score sentences and then select the one 
# with the minimum loss. 


from pytorch_pretrained_bert import BertTokenizer,BertForMaskedLM
import torch
from sentence_formula import action_sent

bertMaskedLM = BertForMaskedLM.from_pretrained('bert-base-uncased')
bertMaskedLM.eval()

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def get_score(sentence):
    """returns scores for a sentence"""
    tokenize_input = tokenizer.tokenize(sentence)
    tensor_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
    predictions=bertMaskedLM(tensor_input)
    loss_fct = torch.nn.CrossEntropyLoss()
    loss = loss_fct(predictions.squeeze(),tensor_input.squeeze()).data 
    return math.exp(loss)


def get_sent(sent):
    """returns the sentence with minimum score"""
    sents = action_sent(sent)
    arg_min = np.argmin([get_score(x) for x in sents])
    return sents[arg_min]


sentence = 'He hit me with a bat'

get_sent(sentence) # Returns: 'hit Him with a bat'