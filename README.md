# Lexical Analyzer

## Overview

This document details the implementation of a basic lexical analyzer (also known as a scanner) for a simple custom programming language. The lexical analyzer is implemented in Python and is designed to tokenize source code into recognizable elements.

## Custom Language Definition

The custom programming language handled by this lexical analyzer includes:

- **Numeric Literals**: Both integers and floating-point numbers.
- **Identifiers**: Variable names that are alphanumeric strings starting with a letter.
- **Arithmetic Operators**: `+`, `-`, `*`, `/`.
- **Assignment Operator**: The `=` symbol.
- **String Literals**: Text enclosed in double quotes.
- **Comments**: Lines starting with `#`.
- **Parentheses**: For grouping expressions.
- **Control Structures**: Basic `if` statements.

## Lexical Analyzer Implementation

### Token Specification

Each token is defined with a regular expression pattern:

- **NUMBER**: Matches integers and floating-point numbers (`\d+(\.\d+)?`).
- **ASSIGN**: Matches the assignment operator `=` (`=`).
- **OPERATOR**: Matches arithmetic operators (`[+\-*/]`).
- **STRING**: Matches string literals (`"[^"]*"`).
- **IF**: Matches the `if` keyword (`\bif\b`).
- **IDENTIFIER**: Matches identifiers (`[A-Za-z]\w*`).
- **COMMENT**: Matches comments (`#.*`).
- **PAREN**: Matches parentheses (`[\(\)]`).
- **SKIP**: Ignores spaces and tabs (`[ \t]`).
- **NEWLINE**: Matches newline characters (`\n`).
- **MISMATCH**: Catches any other character (`.`).

### Tokenization Function

The `tokenize` function breaks a string of source code into tokens based on the defined patterns.

```python
def tokenize(code):
# Tokenization logic...
```

### Utility Function: `get_token_regex`

Combines individual token regexes into a single pattern for matching.

```python
def get_token_regex():
# Combining regex logic...
```

## Sample Programs and Testing

The `test_lexer` function demonstrates the lexer's functionality using sample code snippets:

```python
def test_lexer():
# Testing logic...
```

## Running the Lexer

To run the lexer and see the tokens for the sample programs, execute:

```python
test_lexer()
```

## Error Handling

The lexer raises a `RuntimeError` for any unexpected or mismatched characters during tokenization.
