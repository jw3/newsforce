import argparse
import json
import os

override_key = "EVENT_PATH"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Directory containing news articles")
    parser.add_argument("-c", "--change_type", nargs="+", default=[], help="Add to the change type labels list")
    parser.add_argument("--change_types", help="Replace the default change type labels list")
    parser.add_argument("-i", "--ignore_label", nargs="+", default=[], help="Add to the ignored labels list")
    parser.add_argument("--ignored_labels", help="Replace the default list of ignored labels")
    parser.add_argument("--contrib_guide_url", required=False, help="URL of contrib guide")

    args = parser.parse_args()

    articles_dir = args.dir
    change_types = args.change_types if args.ignored_labels else ["added", "removed", "changed", "fixed"]
    for change_type in args.change_type:
        change_types.append(change_type)
    ignored_labels = args.ignored_labels if args.ignored_labels else ["release", "documentation"]
    for ignored_label in args.ignore_label:
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

    for change_type in change_types:
        article = f"{articles_dir}/{pull_request_number}.{change_type}.md"
        if os.path.exists(article):
            print(f"Found article: {article}")
            return 0

    print(f"Article {pull_request_number} not found in the `{articles_dir}` directory.")

    if args.contrib_guide_url:
        print(f"See {args.contrib_guide_url} for more information.")

    return 1


if __name__ == '__main__':
    main()
