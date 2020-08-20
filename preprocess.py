import io
import re

def preprocess_sentence(w):
  w = w.lower().strip()
  w = re.sub(r"([?.!,¿])", r" \1 ", w)
  w = re.sub(r'[" "]+', " ", w)
  w = re.sub(r"[^a-zA-Z?.!,¿]+", " ", w)
  w = w.strip()
  w = '<start> ' + w + ' <end>'
  return w


def create_dataset(filename,num_examples):
  lines = io.open(filename, errors = "ignore").read().strip().split('\n')
  print(len(lines))
  word_pairs = [[preprocess_sentence(w) for w in l.split('\t')]  for l in lines[:num_examples]]
  return zip(*word_pairs)

en, kr = create_dataset("Dataset6013.txt",None)
print(en[-1])
print(kr[-1])