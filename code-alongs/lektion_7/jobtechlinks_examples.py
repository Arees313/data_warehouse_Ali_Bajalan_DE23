import requests
import json

"""
Install python packages:
pip install -r requirements.txt
"""

url = 'https://links.api.jobtechdev.se'
url_for_search = f"{url}/joblinks"


def _get_ads(params):
    headers = {'accept': 'application/json'}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()  # check for http errors
    return json.loads(response.content.decode('utf8'))


def _print_ad(ad):
    print(f"{ad['headline']}, {ad['employer']['name']}")
    source_links = [item['label'] for item in ad['source_links']]
    print(source_links)
    print(ad['brief'])  # 'brief' is a shortened description from the original ad
    print()


def example_search_return_number_of_hits(query):
    # limit: 0 means no ads, just a value of how many ads were found.
    search_params = {'q': query, 'limit': 0}
    json_response = _get_ads(search_params)
    number_of_hits = json_response['total']['value']
    print(f"\nTotal number of hits = {number_of_hits}")


def example_search_loop_through_hits(query):
    # limit = 100 is the max number of hits that can be returned.
    # If there are more (which you find with ['total']['value'] in the json response)
    # you have to use offset and multiple requests to get all ads.
    search_params = {'q': query, 'limit': 100}
    json_response = _get_ads(search_params)
    hits = json_response['hits']
    for hit in hits:
        _print_ad(hit)
    print('---------------------------\n')


def example_filter_source(query):
    """
    This example excludes all hits that comes from Arbetsförmedlingen and only show results from other sources
    the field 'source_links' in the ad is a list of the source(s) where the original ad was found
    """
    exclude = 'arbetsformedlingen.se'
    limit = 100
    search_params = {'q': query, 'limit': limit, 'exclude_source': exclude}
    json_response = _get_ads(search_params)
    hits = json_response['hits']
    for hit in hits:
        _print_ad(hit)
    number_of_hits = json_response['total']['value']
    print(f"Number of hits, excluding {exclude} = {number_of_hits}")


if __name__ == '__main__':
    query = 'lärare uppsala'
    example_search_loop_through_hits(query)
    example_filter_source(query)
    example_search_return_number_of_hits(query)
