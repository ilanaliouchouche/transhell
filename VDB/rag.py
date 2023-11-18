from langchain.vectorstores.pgvector import PGVector


def prompt_out(query,lang_in, lang_out, vdb: PGVector):
    prompt = f"Translation from {lang_in} to {lang_out}: {query}"
    docs = vdb.similarity_search(prompt, k=5, filter={"lang": f"{lang_in}-{lang_out}"}).reverse()
    return prompt + f"if it's necessary you can use these examples:{docs}"  

