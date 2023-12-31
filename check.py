import argparse
import json
import os
import sys

override_key = "EVENT_PATH"
default_categories = ["added", "removed", "changed", "fixed", "packaging", "build"]
default_ignores = ["release", "documentation"]


def list_of_strings(arg):
    return arg.split(',')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Directory containing news articles")
    parser.add_argument("-c", "--category", nargs="+", default=[], help="Add to the categories list")
    parser.add_argument("--categories", type=list_of_strings, help="Replace the default category list")
    parser.add_argument("-i", "--ignore", nargs="+", default=[], help="Add to the ignored labels list")
    parser.add_argument("--ignores", type=list_of_strings, help="Replace the default list of ignored labels")
    parser.add_argument("--contrib_guide_url", required=False, help="URL of contrib guide")

    args = parser.parse_args()

    articles_dir = args.dir
    categories = args.categories if args.categories else default_categories
    for category in args.category:
        categories.append(category)
    ignored_labels = args.ignores if args.ignores else default_ignores
    for ignored_label in args.ignore:
        ignored_labels.append(ignored_label)

    event_path = os.environ.get(override_key) if override_key in os.environ else os.environ.get("GITHUB_EVENT_PATH")
    with open(event_path) as event_file:
        event = json.load(event_file)

    for label in ignored_labels:
        if event["pull_request"]["title"].startswith(f"{label}:"):
            print(f"Changelog skip on title prefix: {label}")
            return 0

        if label in event["pull_request"]["labels"]:
            print(f"Changelog skip on PR label: {label}")
            return 0

    pull_request_number = event["pull_request"]["number"]

    for category in categories:
        article = f"{articles_dir}/{pull_request_number}.{category}.md"
        if os.path.exists(article):
            print(f"Found article: {article}")
            return 0

    print(f"Article {pull_request_number} not found in the `{articles_dir}` directory.")

    if args.contrib_guide_url:
        print(f"See {args.contrib_guide_url} for more information.")

    return 1


if __name__ == '__main__':
    sys.exit(main())
