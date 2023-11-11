import nltk

def build_dependency_graph(input_sentence):
    # Tokenize the sentence
    tokens = nltk.word_tokenize(input_sentence)

    # Perform part-of-speech tagging
    pos_tags = nltk.pos_tag(tokens)

    # Use the Stanford Dependency Parser to get the dependency graph
    dependency_parser = nltk.parse.corenlp.CoreNLPDependencyParser()
    result = dependency_parser.raw_parse(input_sentence)

    # Extract the dependency graph
    dependency_graph = result.__next__()

    return dependency_graph

def transition_based_dependency_parsing(input_sentence):
    # Tokenize the sentence
    tokens = nltk.word_tokenize(input_sentence)

    # Initialize stack, buffer, and dependency list
    stack = []
    buffer = tokens.copy()
    dependencies = []

    while buffer or len(stack) > 1:
        # Print the current stack, buffer, and dependencies for each step
        print("Stack:", stack)
        print("Buffer:", buffer)
        print("Dependencies:", dependencies)
        print("----------------------")

        # If the stack is empty, perform a SHIFT operation
        if not stack:
            stack.append(buffer.pop(0))
        else:
            # Perform a SHIFT or REDUCE operation based on your transition rules
            # For simplicity, we'll alternate between SHIFT and REDUCE
            if len(stack) % 2 == 0:
                stack.append(buffer.pop(0))
            else:
                dependencies.append((stack[-2], stack[-1]))  # Assume left arc for simplicity
                stack.pop(-1)

    # Print the final state
    print("Final Stack:", stack)
    print("Final Buffer:", buffer)
    print("Final Dependencies:", dependencies)

# Example usage:
input_sentence = "The quick brown fox jumps over the lazy dog."
dependency_graph = build_dependency_graph(input_sentence)
print(dependency_graph.to_conll(4))

print("\nTransition-Based Dependency Parsing:")
transition_based_dependency_parsing(input_sentence)
