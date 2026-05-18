# validate_me
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

## Example JSON response
```
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

## Example JSON rules file

```
{
  "required_keys": [
    "userId",
    "id",
    "title",
    "body"
  ],
  "expected_types": {
    "userId": "integer",
    "id": "integer",
    "title": "string",
    "body": "string"
  }
}
```

## Example Output
Passing example:
```
{
  "overall_passed": true,
  "all_checks": [
    {
      "path": "userId",
      "check_type": "required",
      "passed": true
    },
    {
      "path": "id",
      "check_type": "required",
      "passed": true
    },
    {
      "path": "title",
      "check_type": "required",
      "passed": true
    },
    {
      "path": "body",
      "check_type": "required",
      "passed": true
    },
    {
      "path": "userId",
      "check_type": "type",
      "expected_type": "integer",
      "passed": true
    },
    {
      "path": "id",
      "check_type": "type",
      "expected_type": "integer",
      "passed": true
    },
    {
      "path": "title",
      "check_type": "type",
      "expected_type": "string",
      "passed": true
    },
    {
      "path": "body",
      "check_type": "type",
      "expected_type": "string",
      "passed": true
    }
  ]
}
```

Failing example:
```
{
  "overall_passed": false,
  "all_checks": [
    {
      "path": "userId",
      "check_type": "required",
      "passed": true
    },
    {
      "path": "id",
      "check_type": "required",
      "passed": true
    },
    {
      "path": "title",
      "check_type": "required",
      "passed": true
    },
    {
      "path": "body",
      "check_type": "required",
      "passed": false,
      "reason": "missing key"
    },
    {
      "path": "userId",
      "check_type": "type",
      "expected_type": "integer",
      "passed": false,
      "reason": "wrong type",
      "actual_type": "str"
    },
    {
      "path": "id",
      "check_type": "type",
      "expected_type": "integer",
      "passed": true
    },
    {
      "path": "title",
      "check_type": "type",
      "expected_type": "string",
      "passed": true
    },
    {
      "path": "body",
      "check_type": "type",
      "expected_type": "string",
      "passed": false,
      "reason": "missing key"
    }
  ]
}
```

## Lessons Learned
Building this API validation tool forced me to learn many key skills, most notably:
- Nested JSON traversal
- List index validation
- CLI argument parsing with argparse
- JSON schema logic
- Debugging validation edge cases

