# Action-Sentence-using-SRL

This repo contains methods for coming up with action sentences using Semantic role labeling and Language modeling.

Workflow:
1. Get Semantic role labels for a sentence 
2. Using the SRL labels, create a combination of sentences using different sentence generation formulas. 
3. Score those sentences using a Langugage Model(BERT) and select the one with Highest score/minimum loss 

I used Allennlp for extracting semantic role labels. And a pretrained BERT language model to score sentences. 
