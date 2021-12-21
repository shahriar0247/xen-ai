from transformers import pipeline

question_answering = pipeline("question-answering")


context = ""
def train(new_context):
        global context
        context = context + new_context

def ask(question):
        result = question_answering(question=question, context=context)
        return result['answer']

