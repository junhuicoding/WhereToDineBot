import logging
import pandas as pd

# Enable logging
logging.basicConfig(
    filename="../log.txt",
    filemode='a',
    format=u'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def parse_results(result_list: [dict]) -> [dict]:
    df = pd.json_normalize(result_list)

    # calculate mean ratings for all results
    C = df['rating'].mean()
    # Calculate top 70 percentile
    upper = df['user_ratings_total'].quantile(0.70)
    # Calculate bottom 30 percentile
    lower = df['user_ratings_total'].quantile(0.30)
    # TODO filter out based on number of ratings
    evaluated_df = df.copy().loc[df['user_ratings_total'] >= 0]
    evaluated_df['score'] = evaluated_df.apply(weighted_rating, args=(upper, C), axis=1)

    # Sort results by generated scores
    evaluated_df = evaluated_df.sort_values('score', ascending=False)

    # Reduce size of frame by removing unnecessary columns and taking top 20 rows
    evaluated_df = evaluated_df[['name', 'user_ratings_total', 'rating', 'score', 'place_id', 'vicinity']].head(20)
    # Parse into dict
    evaluatedResults = evaluated_df.to_dict('records')

    return evaluatedResults


# Calculate score based on IMDb weighted rating.
# https://math.stackexchange.com/questions/169032/understanding-the-imdb-weighted-rating-function-for-usage-on-my-own-website
def weighted_rating(x, m, C):
    v = x['user_ratings_total']
    R = x['rating']
    return (v / (v + m) * R) + (m / (m + v) * C)




    return 1


def generate_scores(place):
    return -1


