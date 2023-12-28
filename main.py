import time

import requests


class WikiFetcher:
    min_interval = 1000

    def __init__(self):
        self.last_request_time = -1

    def fetch_wikipedia(self, url):
        r = requests.get(url)
        print(r.content)

    def sleep_if_needed(self) -> None:
        if self.last_request_time == -1:
            return

        current_time = time.time()
        next_request_time = self.last_request_time + self.min_interval
        if current_time < next_request_time:
            try:
                ...
            except KeyboardInterrupt:
                ...

        self.last_request_time = time.time()


if __name__ == "__main__":
    wf = WikiFetcher()
    url = "https://en.wikipedia.org/wiki/Java_(programming_language)"
    wf.fetch_wikipedia(url)
    print(wf)
