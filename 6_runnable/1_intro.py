# runnables are basically langchain components
# In LangChain, a Runnable is a core abstraction that represents any callable component—a prompt, model, retriever, chain, or even a sequence of these components—that can be executed (invoked), streamed, or batched.

# runnables are unit of work
# each runnable performs certain task
# they provide abstraction and flexibility

# we can connect runnables to form a workflow
# that worflow is also runnable 
# so several workflows can also be connected to form bigger workflow

# runnables take input, process, and gives output; and that output is input for another runnable

# they have common interface:
# invoke(), batch(), stream()







# two types of runnables
# 1. Task specific runnables  -->  they are basically our core langchain components
# 2. Runnable primitive  -->  they are for structuring and making workflows by combining task specific runnables. 
# Ex: 
# 1. RunnableSequence (|)
# 2. RunnableParallel
# 3. RunnableBranch
# 4. RunnableLambda: Wraps custom python function into runnables
# 5. Runnable Map: Maps the same input across multiple functions
# 6. RunnablePassthrough: Just forwards input as output (acts as placeholder)
