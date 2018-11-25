import nltk

def _get_tokens(text):
  tokens = nltk.word_tokenize(text)
  pos_tokens = nltk.pos_tag(tokens)

  return pos_tags

def _get_chunks(text):
  grammar = r"""
    NP: {<JJ.*>*<NN.*>}
        {<NNP>+}
  """
  cp = nltk.RegexpParser(grammar)

  return cp
