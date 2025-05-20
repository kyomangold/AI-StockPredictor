# Project Title

## Summary
This repository is designed to facilitate automated documentation generation for codebases, streamlining the process of creating comprehensive README files and related documentation.

## Key Modules
- **autodocu**: Main module that handles the extraction of information from the codebase and formats it into a README.
- **parser**: A utility for parsing various code files and extracting relevant documentation comments.
- **formatter**: Module to format the extracted information into Markdown.

## Installation
To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Quick Start
To generate a README file for your project, use the following command:

```bash
python -m autodocu
```

Make sure you are in the root directory of your project when you execute this command. The generated README will be saved to the project root.