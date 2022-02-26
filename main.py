import pandas as pd

compact_results_1 = pd.read_csv('data/WDataFiles_Stage1/WRegularSeasonCompactResults.csv')

compact_results_1 = compact_results_1.drop(['NumOT', 'WLoc'], axis=1)


def team_game_summary(compact_results):
    compact_results['WScoreDiff'] = compact_results['WScore'] - compact_results['LScore']
    compact_results['LScoreDiff'] = -compact_results['WScoreDiff']

    won = compact_results[['Season', 'WTeamID', 'WScoreDiff']].rename(
        columns={'WTeamID': 'TeamID', 'WScoreDiff': 'ScoreDiff'})
    lost = compact_results[['Season', 'LTeamID', 'LScoreDiff']].rename(
        columns={'LTeamID': 'TeamID', 'LScoreDiff': 'ScoreDiff'})

    all_games = pd.concat([won, lost])
    all_games['Won'] = all_games['ScoreDiff'] > 0

    return (all_games)


def compute_avg_result(all_games):
    avg_score = all_games.groupby(['Season', 'TeamID']).mean().rename(
        columns={'ScoreDiff': 'MeanScoreDiff',
                 'Won': 'WonPerc'}).reset_index()

    return(avg_score)
