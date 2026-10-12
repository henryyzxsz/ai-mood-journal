"""AI Mood Journal - daily entry app.
Each TODO is yours to write. Ask Claude Code or Meeple for help when stuck.
"""
import csv
from datetime import date

DATA_FILE = "dataset/entries.csv"

PANAS_POSITIVE = ["interested", "excited", "strong", "enthusiastic", "proud",
                  "alert", "inspired", "determined", "attentive", "active"]
PANAS_NEGATIVE = ["distressed", "upset", "guilty", "scared", "hostile",
                  "irritable", "ashamed", "nervous", "jittery", "afraid"]


def get_journal_entry():
    # TODO: ask the user for a 3-5 sentence entry and return it
    pass


def get_panas_ratings():
    # TODO: ask for a 1-5 rating for each word above.
    # Return positive_score (sum of positive) and negative_score (sum of negative).
    pass


def score_with_ai(text):
    # TODO: use VADER (from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer)
    # and return the "compound" score (-1 to 1).
    pass


def save_entry(entry, pos, neg, ai_score):
    # TODO: append a row to DATA_FILE: date, entry, pos, neg, ai_score.
    # Write a header row if the file is new.
    pass


def main():
    # TODO: call the functions above in order and print a summary.
    pass


if __name__ == "__main__":
    main()
