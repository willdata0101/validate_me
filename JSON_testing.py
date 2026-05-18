# Validate function
import json
import argparse
from nested_json import get_json_value
from cli_design import display_report

def validate_response(response, rules):
    """
    Takes an API response in JSON format and checks it against a rules JSON file.
    Args:
    response: An API response doc in JSON format (i.e. response.json)
    rules: An API rules doc in JSON format (i.e. rules.json)

    Returns a dictionary containing overall pass/fail and all validation checks.
    """
    check_list = []
    required_keys = rules["required_keys"]
    for element in required_keys:
        path = element.split(".")
        found, _ = get_json_value(path, response)
        check_dict = {}
        if found:
            check_dict["path"] = element
            check_dict["check_type"] = "required"
            check_dict["passed"] = True
            check_list.append(check_dict)
        else:
            check_dict["path"] = element
            check_dict["check_type"] = "required"
            check_dict["passed"] = False
            check_dict["reason"] = "missing key"
            check_list.append(check_dict)

    # Mapping dictionary
    type_dict = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "object": dict,
        "array": list,
        "boolean": bool
    }

    type_check_list = []

    expected_types = rules["expected_types"]
    for element in expected_types:
        expected_type_name = expected_types[element]
        check_dict = {}
        check_dict["path"] = element
        check_dict["check_type"] = "type"
        check_dict["expected_type"] = expected_type_name
        path = element.split(".")
        found, value = get_json_value(path, response)
        if found:
            if isinstance(value, type_dict[expected_type_name]):
                check_dict["passed"] = True
                type_check_list.append(check_dict)
            else:
                check_dict["passed"] = False
                check_dict["reason"] = "wrong type"
                check_dict["actual_type"] = type(value).__name__
                type_check_list.append(check_dict)
        else:
            check_dict["passed"] = False
            check_dict["reason"] = "missing key"
            type_check_list.append(check_dict)

    check_lists = check_list + type_check_list

    final_dict = {}
    overall_passed = True
    for e in check_lists:
        if not e["passed"]:
            overall_passed = False

    final_dict["overall_passed"] = overall_passed
    final_dict["all_checks"] = check_lists
    return final_dict

# CLI tool logic
def main():

    parser = argparse.ArgumentParser(description="Validate an API JSON response against rules.")

    parser.add_argument("response")
    parser.add_argument("rules")

    args = parser.parse_args()

    def load_json(filename):
        with open(filename) as f:
            return json.load(f)
        
    response_data = load_json(args.response)
    print(response_data.keys())
    rules_data = load_json(args.rules)

    results = validate_response(response_data, rules_data)

    overall_passed = results["overall_passed"]
    all_checks = results["all_checks"]

    # Pre-retro CLI code (commented out for now)
    # results_json = json.dumps(results, indent=2)
    # print(results_json)

    display_report(all_checks, overall_passed)



if __name__ == "__main__":
    main()