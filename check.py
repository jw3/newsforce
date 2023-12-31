import argparse
import json
import os
import sys
import yaml

override_key = "EVENT_PATH"


def list_of_strings(arg):
    return arg.split(',')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Directory containing news articles")
    parser.add_argument("-c", "--categories", type=list_of_strings, help="Update the category list")
    parser.add_argument("-i", "--ignores", type=list_of_strings, help="Update the ignored labels list")
    parser.add_argument("--contrib_guide_url", required=False, help="URL of contrib guide")
    args = parser.parse_args()

    articles_dir = args.dir

    with open("action.yml") as yaml_file:
        action_yml = yaml.safe_load(yaml_file)

    categories = args.categories if args.categories else list_of_strings(action_yml["inputs"]["ignores"]["default"])
    ignored_labels = args.ignores if args.ignores else list_of_strings(action_yml["inputs"]["categories"]["default"])

    event_path = os.environ.get(override_key) if override_key in os.environ else os.environ.get("GITHUB_EVENT_PATH")
    with open(event_path) as event_file:
        event = json.load(event_file)

    for label in ignored_labels:
        if event["pull_request"]["title"].startswith(f"{label}:"):
            print(f"skipped on title prefix: {label}")
            return 0

        if label in event["pull_request"]["labels"]:
            print(f"skipped on PR label: {label}")
            return 0

    pull_request_number = event["pull_request"]["number"]

    for category in categories:
        article = f"{articles_dir}/{pull_request_number}.{category}.md"
        if os.path.exists(article):
            print(f"found article: {article}")
            return 0

    print(f"Article {pull_request_number} not found in the `{articles_dir}` directory.")

    if args.contrib_guide_url:
        print(f"see guidelines at {args.contrib_guide_url}")

    return 1


if __name__ == '__main__':
    sys.exit(main())
