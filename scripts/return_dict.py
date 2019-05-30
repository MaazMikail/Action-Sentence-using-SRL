import re
import spacy
nlp = spacy.load("en_core_web_lg")
from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("srl-model-2018.05.25.tar.gz")

def return_dict(sent):
    """Returns a dictionary of SRL labels for sentence"""
    pred = predictor.predict(
          sentence=sent)
    
    dict_roles = dict()
    temp = ''
    a = nlp(sent)
    root = [x.text for x in a if x.dep_ == 'ROOT' and x.pos_ == 'VERB']
    for each in pred['verbs']:
        if root == []:
            temp = each['description']
            break
        elif each['verb'] == root[0]:
            temp = each['description']
    roles_str = re.findall("\[(.*?)\]",temp)
    
    for each in roles_str:
        vals=each.split(':')
        dict_roles[vals[0]]=vals[1]
    return dict_roles 