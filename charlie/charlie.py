

from haystack.pipelines import ExtractiveQAPipeline
from haystack.nodes import TfidfRetriever
import os
from haystack.utils import print_answers
from haystack.nodes import FARMReader, TransformersReader
from haystack.document_stores import InMemoryDocumentStore

reader =  TransformersReader(model_name_or_path="bert-large-uncased-whole-word-masking-finetuned-squad")
pipe = None


dicts = []

def train(new_info):
    document_store = InMemoryDocumentStore()
    global dicts
    dicts.append({'content': new_info})
    document_store.write_documents(dicts)
    retriever = TfidfRetriever(document_store=document_store)
    global pipe
    pipe = ExtractiveQAPipeline(reader, retriever)


def ask(question):
    global pipe
    
    prediction = pipe.run(
        query=question, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
    )
    return (prediction["answers"][1].answer)




