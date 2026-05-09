# api-response-validator-cli
Python CLI tool for validating API JSON responses against configurable rules. Supports nested JSON, array indexing, and QA/Postman workflows.

<img width="1895" height="962" alt="json_validator_github_readme" src="https://github.com/user-attachments/assets/fd9e68b7-37af-466b-a571-b0991f1d9608" />

## Why I built this
While learning QA Engineering and API Testing with Postman, I wanted to get my hands super dirty and build a project that forced me to learn the ins and outs of API response validation with Python. To this end, I built a Python CLI validator that checks an API response in Postman against prescribed, configurable rules.

## Features

The tool allows the user to:
- Validate required fields
- Validate expected data types
- Support nested JSON via dot-path syntax
- Support array/list indexing (movies[0].title)
- Generate structured JSON validation reports
- CLI workflow for API/Postman testing
