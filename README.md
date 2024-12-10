# Forward Chaining Expert System Project

This project is meant to showcase a small example of an expert system with a forward-chaining inference algorithm.

The knowledge base is stored in a text file.

## Syntax

Here's an example of knowledge base. Each rules and facts follow the following formats.

```txt
-| Fact1;
-| Fact2;

Fact1, Fact2 -> Fact3;
```

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/mtbelkebir/forward_chaining_expert_system.git
    ```

2. Launch the app with a specified knowledge base.

    ```bash
    python main.py /path/to/knowledge/base
    ```

3. Query the knowledge base by entering the name of the fact to be inferred.

    ```txt
    ?- MyFact
    True
    ```

    The inference engine may display `True` or `False` depending on whether the specified goal was reached or not.

### Available commands

Commands are available for certain special actions.

- `.print`: Prints the current knowledg base with all rules and facts.
- `.quit`: Exists the program.
- `.help`: Prints the help screen.

## Sample knowledge base

```txt
-| B;
-| C;
B,D,E -> F;
G,D -> A;
C,F -> A;
B -> X;
X,A -> H;
C -> D;
X,C -> A;
X,B -> D
```
