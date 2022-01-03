import tensorflow as tf
import tensorflow_hub as hub
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('tokenizer_tf2_qa')
model = hub.load("https://tfhub.dev/see--/bert-uncased-tf2-qa/1")

questions = [
    'How long did it take to find the answer?',
    'What\'s the answer to the great question?',
    'What\'s the name of the computer?']
paragraph = '''<p>The computer is named Deep Thought.</p>.
               <p>After 46 million years of training it found the answer.</p>
               <p>However, nobody was amazed. The answer was 42.</p>'''

for question in questions:
  question_tokens = tokenizer.tokenize(question)
  paragraph_tokens = tokenizer.tokenize(paragraph)
  tokens = ['[CLS]'] + question_tokens + ['[SEP]'] + paragraph_tokens + ['[SEP]']
  input_word_ids = tokenizer.convert_tokens_to_ids(tokens)
  input_mask = [1] * len(input_word_ids)
  input_type_ids = [0] * (1 + len(question_tokens) + 1) + [1] * (len(paragraph_tokens) + 1)

  input_word_ids, input_mask, input_type_ids = map(lambda t: tf.expand_dims(
      tf.convert_to_tensor(t, dtype=tf.int32), 0), (input_word_ids, input_mask, input_type_ids))
  outputs = model([input_word_ids, input_mask, input_type_ids])
  # using `[1:]` will enforce an answer. `outputs[0][0][0]` is the ignored '[CLS]' token logit
  short_start = tf.argmax(outputs[0][0][1:]) + 1
  short_end = tf.argmax(outputs[1][0][1:]) + 1
  answer_tokens = tokens[short_start: short_end + 1]
  answer = tokenizer.convert_tokens_to_string(answer_tokens)
  
  
