from twitter_scraper import get_tweets
import markovify
import sys
import string
import lxml

acceptable_chars = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!/\',-.'


def main():
    try:
        user = sys.argv[1]
    except KeyError:
        print('Who do you want a fake tweet from?')
        return

    try:
        no_of_tweets = int(sys.argv[2])
    except KeyError:
        no_of_tweets = 1
    except ValueError:
        print('Secong arg should be the number of tweets to generate')

    print('Getting user tweets...')
    try:
        tweets = ''
        for t in get_tweets(user, pages=20):
            try:
                tweets += ''.join(
                    filter(lambda x: x in acceptable_chars, t['text'])) + '\n'
            except:
                continue
    except lxml.etree.ParserError:
        print('The user doesn\'t have enough tweets for data.')
        return
    except IndexError:
        print('Some bug happened with twitter_scraper.')

    text_model = markovify.Text(tweets)

    print('Generating new tweets...')
    for i in range(no_of_tweets):
        print('@{}: {}'.format(user, text_model.make_short_sentence(140)))


if __name__ == '__main__':
    main()