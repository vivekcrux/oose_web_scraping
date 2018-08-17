import requests
from bs4 import BeautifulSoup


def read_codechef_profile(handle):
    try:
        r = requests.get("https://www.codechef.com/users/" + handle)
        soup = BeautifulSoup(r.text, 'html.parser')

        data = soup.find_all('article')

        solve_categories = ['Fully Solved', 'Partially Solved']

        profile = dict()
        state = dict()

        for i in range(2):
            x = data[i].find_all('p')

            for j in range(len(x) - 1, 0, -1):
                contest_title = x[j].find('strong').text[:-1]

                if '18' in contest_title or '19' in contest_title:
                    attempted = x[j].find_all('a')

                    if contest_title not in state:
                        state[contest_title] = dict()

                    state[contest_title][solve_categories[i]] = len(attempted)


        profile['current_rating'] = soup.find('div', attrs={'class': 'rating-number'}).text

        rank_obj = soup.find('div', attrs={'class': 'rating-ranks'}).find_all('a')
        profile['global_rank'] = rank_obj[0].text
        profile['country_rank'] = rank_obj[1].text

        profile['work'] = state

        username_content = soup.find('section', attrs={'class': 'user-details'}).find('span').contents
        if len(username_content) == 1:
            profile['stars'] = '0'
        else:
            profile['stars'] = username_content[0].text[:1]

        return profile

    except IndexError:
        return None
