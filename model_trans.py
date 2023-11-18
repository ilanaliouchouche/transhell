import sys
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


TEMPLATE = """Can you translate into {output_lang} this sentence: {prompt}"""
PROMPT = PromptTemplate(template=TEMPLATE, input_variables=["output_lang","prompt"])

MODEL_PATH = "google/flan-t5-large"
TOKENIZER = AutoTokenizer.from_pretrained(MODEL_PATH)
MODEL = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

PIPE = pipeline(
    "text2text-generation",
    model=MODEL,
    tokenizer=TOKENIZER,
    max_length=100
)

LOCAL_LLM = HuggingFacePipeline(pipeline=PIPE)

LLM = LLMChain(prompt=PROMPT,
                     llm=LOCAL_LLM)

def translation(out : str, prompt : str):
    return LLM.predict(output_lang=out, prompt=prompt)

if __name__ == "__main__":
    print(translation(sys.argv[1], sys.argv[2]))






