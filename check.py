import argparse
import json
import os
import sys
import yaml

override_key = "EVENT_PATH"


def list_of_strings(arg):
    return arg.split(",")


def main(articles_dir, ignore_list=None, category_list=None, contrib_url=None) -> int:
    with open("action.yml") as yaml_file:
        action_yml = yaml.safe_load(yaml_file)

    categories = (
        list_of_strings(category_list)
        if category_list
        else list_of_strings(action_yml["inputs"]["categories"]["default"])
    )
    ignored_labels = (
        list_of_strings(ignore_list)
        if ignore_list
        else list_of_strings(action_yml["inputs"]["ignores"]["default"])
    )

    event_path = (
        os.environ.get(override_key)
        if override_key in os.environ
        else os.environ.get("GITHUB_EVENT_PATH")
    )
    with open(event_path) as event_file:
        event = json.load(event_file)

    for ignored in ignored_labels:
        tag = event["pull_request"]["title"].split(":", maxsplit=1)[0]
        if tag.casefold() == ignored.casefold():
            print(f"Skipped on title prefix: {ignored}")
            return 0

        for label in event["pull_request"]["labels"]:
            if label["name"].casefold() == ignored.casefold():
                print(f"Skipped on PR label: {label['name']}")
                return 0

    pull_request_number = event["pull_request"]["number"]

    for category in categories:
        article = f"{articles_dir}/{pull_request_number}.{category}.md"
        if os.path.exists(article):
            print(f"Found article: {article}")
            return 0

    print(f"Article {pull_request_number} not found in the `{articles_dir}` directory.")

    if contrib_url:
        print(f"See guidelines at {args.contrib_guide_url}")

    return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Directory containing news articles")
    parser.add_argument(
        "-c", "--categories", type=str, help="Comma separated category list"
    )
    parser.add_argument(
        "-i", "--ignores", type=str, help="Comma separated ignored labels list"
    )
    parser.add_argument(
        "--contrib_guide_url", required=False, help="URL of contributing guide"
    )
    args = parser.parse_args()

    sys.exit(main(args.dir, args.ignores, args.categories, args.contrib_guide_url))
