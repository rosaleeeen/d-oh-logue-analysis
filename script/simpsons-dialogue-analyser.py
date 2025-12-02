import argparse
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS


def load_character_data(char_names, char_paths, normalise_names=True):
    """load character dialogue data from CSV files and assign character names."""

    char_names = [name.strip().replace(' ', '-').lower() for name in char_names]

    dfs = []
    for name, path in zip(char_names, char_paths):
        temp = pd.read_csv(path)
        temp['character'] = name
        dfs.append(temp)
    df = pd.concat(dfs, ignore_index=True)
    return df


def read_stop_words(stop_words_path):
    """read custom stop words from user's stop-word file."""

    with open(stop_words_path, 'r', encoding='utf-8') as f:
        custom_stops = {w.strip() for w in f.read().splitlines() if w.strip()}
    return custom_stops


def initialise_custom_stops_tfidf(extra_stops):
    """initialise TfidfVectorizer with custom stop words."""

    custom_stop_words = list(ENGLISH_STOP_WORDS.union(extra_stops))

    vectoriser = TfidfVectorizer(
        lowercase=True,
        stop_words=custom_stop_words,
        min_df=2,                               # ignore words in fewer than 2 tags
        max_df=0.90,                            # ignore words in more than 90% of tags
        token_pattern=r'(?u)\b[a-zA-Z]{3,}\b',  # tokens of 3 or more letters
    )
    return vectoriser


def get_top_10_tfidf_per_topic(vectoriser, topic_docs):
    """compute TF-IDF and extract top 10 words per topic."""

    X = vectoriser.fit_transform(topic_docs['quote'])
    feature_names = vectoriser.get_feature_names_out()
    topic_labels = topic_docs['tag'].tolist() 

    rows = []
    Xd = X.toarray()
    for i, tag in enumerate(topic_labels):
        idx = Xd[i].argsort()[::-1][:10]
        for r, j in enumerate(idx): rows.append((tag, r+1, feature_names[j], Xd[i][j]))

    tfidf_table = pd.DataFrame(rows, columns=['topic','rank','word','tfidf'])
    tfidf_table.to_csv(args.output, index=False)

    return tfidf_table


def get_stats(df):
    """compute and save topic statistics per character."""

    # 1. topic counts per char
    topic_counts = df.groupby(['character', 'tag']).size().unstack(fill_value=0)
    topic_counts.to_csv('topic_counts.csv')

    # 2. topic percentage table 
    topic_percentages = topic_counts.div(topic_counts.sum(axis=1), axis=0)
    topic_percentages.to_csv('topic_percentages.csv')

    # 3. word-weighted topic percentages
    df['word_count'] = df['quote'].str.split().apply(len)

    weighted = df.groupby(['character', 'tag'])['word_count'].sum()
    weighted = weighted.unstack(fill_value=0)

    weighted_percent = weighted.div(weighted.sum(axis=1), axis=0)
    weighted_percent.to_csv('topic_weighted_percentages.csv')

    return topic_counts, topic_percentages, weighted_percent


if __name__ == '__main__':
    # read command-line arguments
    parser = argparse.ArgumentParser(description='TF-IDF Analyser')
    parser.add_argument('stop_words', type=str, help='path to stop_words file')
    parser.add_argument('char_1_name', type=str, help='name of character 1')
    parser.add_argument('char_1_path', type=str, help='path to input CSV file for char 1')
    parser.add_argument('char_2_name', type=str, help='name of character 2')
    parser.add_argument('char_2_path', type=str, help='path to input CSV file for char 2')
    parser.add_argument('char_3_name', type=str, help='name of character 3')
    parser.add_argument('char_3_path', type=str, help='path to input CSV file for char 3')
    parser.add_argument(
        '--output',
        type=str,
        default='tfidf_top10.csv',
        help='path to output CSV file for TF-IDF table',
    )
    args = parser.parse_args()

    # convert arguments to lists
    char_names = [args.char_1_name, args.char_2_name, args.char_3_name]
    char_paths = [args.char_1_path, args.char_2_path, args.char_3_path]

    # load character data
    df = load_character_data(char_names, char_paths)
    print(f'...loaded data for characters: {char_names}...')

    # prepare documents per topic
    topic_docs = df.groupby('tag')['quote'].apply(lambda x: ' '.join(x)).reset_index()
    print('...prepared documents per topic...')
    
    # compute TF-IDF and get stats
    extra_stops = read_stop_words(args.stop_words)
    print(f'...read extra stop words from {args.stop_words}...')

    # initialise vectoriser with custom stops
    vectoriser = initialise_custom_stops_tfidf(extra_stops)
    print('...initialised vectoriser with custom stop words...')

    # compute TF-IDF and get top 10 words per topic
    tfidf_table = get_top_10_tfidf_per_topic(vectoriser, topic_docs)
    print('...computed TF-IDF and extracted top 10 words per topic...')

    # compute and save topic statistics per character
    get_stats(df)
    print('...computed and saved topic statistics per character!')