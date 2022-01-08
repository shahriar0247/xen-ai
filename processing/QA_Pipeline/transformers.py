from outputs.debug.debug import debug

question_answering = None


def init_qa_pipeline():
    from transformers import pipeline
    global question_answering
    question_answering = pipeline("question-answering")
    debug("QA Pipeline", "init")


context = ""


def train(new_context):
    global context
    context = context + new_context


def ask(question):
    result = question_answering(question=question, context=context)
    return result['answer']
