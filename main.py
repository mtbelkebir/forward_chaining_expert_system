from knowledge import InferenceEngine, parse_rules, parse_facts
import sys

def main(args):
    file_path = args[1]

    with open(file_path, 'r') as file:
        file_contents = file.read()

    rules = parse_rules(file_contents)
    facts = parse_facts(file_contents)

    inference_engine = InferenceEngine(rules, facts)

    print(inference_engine)
    while True:
        query = input('?-')
        found = inference_engine.infer(query)
        print(found)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Fatal Error: Missing argument knowledge base file.', file = sys.stderr)
        exit(1)

    main(sys.argv)