import re

# Token specification
TOKEN_SPECIFICATION = [
    ('NUMBER',    r'\d+(\.\d+)?'),   # Integer or decimal number
    ('ASSIGN',    r'='),             # Assignment operator
    ('OPERATOR',  r'[+\-*/]'),       # Arithmetic operators
    ('STRING',    r'"[^"]*"'),       # String literals
    ('IF',        r'\bif\b'),        # 'if' keyword
    ('IDENTIFIER',r'[A-Za-z]\w*'),   # Identifiers
    ('COMMENT',   r'#.*'),           # Comments
    ('PAREN',     r'[\(\)]'),        # Parentheses
    ('SKIP',      r'[ \t]'),         # Skip spaces and tabs
    ('NEWLINE',   r'\n'),            # New line
    ('MISMATCH',  r'.'),             # Any other character
]

def get_token_regex():
    # Combines the individual token regexes into a single regex that can be used to match tokens in the source code.
    return '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPECIFICATION)

def tokenize(code):
    # Tokenize the input code string.
    token_regex = get_token_regex()
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup  # The name of the matched token type.
        value = mo.group()   # The actual matched text from the input.

        # Converts numeric literals to Python number types.
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        # Skips over any whitespace or newlines.
        elif kind in ['SKIP', 'NEWLINE']:
            continue
        # Raises an error for any unexpected/mismatched character.
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r}')

        # Yield a tuple of the token type and its value.
        yield kind, value


def test_lexer():
    # Sample programs to demonstrate the functionality of the lexer.
    code_samples = [
        'x = 42',
        'y = x * 2 - (5 / z)',
        'a = 3 + 4 - 5 * 6 / 7'
    ]

    # Testing each sample program.
    for code in code_samples:
        print(f'\nCode: {code}')
        try:
            # Tokenizing the sample program and printing the tokens.
            for token in tokenize(code):
                print(token)
        except RuntimeError as e:
            # Catching and displaying any errors encountered during tokenization.
            print(f'Error: {e}')

# Running the test lexer to display the tokens of the sample programs.
test_lexer()