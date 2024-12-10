from knowledge import InferenceEngine, parse_rules, parse_facts
import sys

def print_available_commands():
    print("Available commands:")
    print(".print - Print the current rules and facts")
    print(".quit - Exit the program")
    print('.help - Print this help screen')

def main(args):
    file_path = args[1]

    with open(file_path, 'r') as file:
        file_contents = file.read()

    rules = parse_rules(file_contents)
    facts = parse_facts(file_contents)

    inference_engine = InferenceEngine(rules, facts)
    print_available_commands()
    print(inference_engine)
    while True:
        query = input('?-')
        if query.startswith('.'):
            match query[1::].strip():
                case 'print':
                    print(inference_engine)
                case 'quit':
                    exit(0)
                case 'help':
                    print_available_commands()
                case _:
                    print('Error: Unknown command.')
        found = inference_engine.infer(query)
        print(found)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Fatal Error: Missing argument knowledge base file.', file = sys.stderr)
        exit(1)

    main(sys.argv)