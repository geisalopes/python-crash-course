from operator import itemgetter
import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Get the list of top story IDs.
submission_ids = r.json()

submission_dicts = []

for submission_id in submission_ids[:30]:
    # API call for each individual story
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    if r.status_code != 200:
        print(f"Failed to fetch story {submission_id}. Skipping.")
        continue

    response_dict = r.json()

    # Sometimes 'title' or 'descendants' may not exist — let's be cautious!
    title = response_dict.get("title", "No title available")
    hn_link = f"https://news.ycombinator.com/item?id={submission_id}"
    comments = response_dict.get("descendants", 0)

    submission_dict = {
        "title": title,
        "hn_link": hn_link,
        "comments": comments,
    }

    submission_dicts.append(submission_dict)

# Sort stories by number of comments, descending
submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

# Print the top stories
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
