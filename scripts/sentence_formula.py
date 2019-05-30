
import re
import spacy
nlp = spacy.load("en_core_web_lg")
from SRL_dict import return_dict

def action_sent(sent):
    """returns combinations of action sentences generated using SRL labels"""
    roles = return_dict(sent)
    arg0, arg1, arg2, arg4, argm_adv, argm_loc='', '', '', '', '', ''
    argm_prd, argm_mnr, argm_prp, argm_neg, argm_dis, verb= '', '', '', '', '', ''
    if roles.get('ARG0', 0) != 0:
        arg0 = roles['ARG0'].strip()
    if roles.get('ARG1', 0) != 0:
        arg1 = roles['ARG1'].strip()
    if roles.get('ARG2', 0) != 0:
        arg2 = roles['ARG2'].strip()
    if roles.get('ARG4', 0) != 0:
        arg4 = roles['ARG4'].strip()
    if roles.get('ARGM-ADV', 0) != 0:
        argm_adv = roles['ARGM-ADV'].strip()
    if roles.get('ARGM-LOC', 0) !=0:
        argm_loc = roles['ARGM-LOC'].strip()
    if roles.get('ARGM-PRD', 0) !=0:
        argm_prd = roles['ARGM-PRD'].strip()
    if roles.get('ARGM-MNR', 0) !=0:
        argm_mnr = roles['ARGM-MNR'].strip()
    if roles.get('ARGM-PRP', 0) !=0:
        argm_prp = roles['ARGM-PRP'].strip()
    if roles.get('ARGM-NEG', 0) !=0:
        argm_neg = roles['ARGM-NEG'].strip()
    if roles.get('ARGM-DIS', 0) != 0:
        argm_dis = roles['ARGM-DIS'].strip()
        
    verb = [l.lemma_ for l in nlp(roles['V'].strip())][0]
    negs = ["Didn't", "Don't", "Not"]
    if arg1.lower().strip() in ('you','me'):
        arg1='Him'
    if argm_neg !="":
        return (re.sub("\s\s+" , " ", f"{negs[0]} {argm_dis} {verb.strip()} {arg1} {arg2} {argm_adv} {arg4} {argm_loc} {argm_prp} {argm_mnr}"),re.sub("\s\s+" , " ", f"{negs[1]} {argm_dis} {verb.strip()} {arg1} {argm_adv} {arg4} {argm_loc} {argm_prp} {argm_mnr}"),re.sub("\s\s+" , " ", f"{negs[2]} {argm_dis} {verb.strip()} {arg1} {arg2} {argm_adv} {arg4} {argm_loc} {argm_prp} {argm_mnr}"))
    else:
        return (re.sub("\s\s+" , " ", f"{verb.strip()} {arg1} {arg2} {argm_adv} {arg4} {argm_loc} {argm_prp} {argm_mnr}"),re.sub("\s\s+" , " ", f"{verb.strip()} {arg1} {argm_adv} {argm_prp} {argm_dis} {argm_mnr}"),re.sub("\s\s+" , " ", f"{argm_mnr} {argm_dis} {verb.strip()} {arg1} {argm_adv} {arg2} {arg4} {argm_loc} {argm_prp}"))
  