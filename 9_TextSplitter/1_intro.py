# we cant give large pdfs in input to give context (because of context limit)
# so to minimize input text splitting is done

# split the text in several docs
# create embeddings for each docs
# get query and generate embedding for that query
# do semantic search to find which context embedding does it match the most
# now give that context whose embedding was closest as input instead of whole doc

# Different ways of text splitting
# 1. Length Based
# 2. Text Structure Based
# 3. Document Strucutre Based
# 4. Semantic meaning Based