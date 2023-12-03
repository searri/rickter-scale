import argparse as ap
import json

p = ap.ArgumentParser()
p.add_argument("short_title")
p.add_argument("--old", action="store_true")
p.add_argument("--long_title")
p.add_argument("--subhead", required=False)
p.add_argument("--old_rating", choices={"good", "fine", "bad"}, required=False)
p.add_argument(
    "--old_how_old", choices={"recent", "semirecent", "old", "youth", "childhood"}, required=False
)
p.add_argument("--rewatch", choices=range(1, 6), required=False)
p.add_argument("--charact", choices=range(1, 6), required=False)
p.add_argument("--supercal", choices=range(1, 6), required=False)
p.add_argument("--pacing", choices=range(1, 6), required=False)
p.add_argument("--cinema", choices=range(1, 6), required=False)
p.add_argument("--structure", choices=range(1, 6), required=False)
p.add_argument("--vibe", required=False)
p.add_argument("--date_watched", required=False)
args = p.parse_args()

movie_dict = {"title": args.long_title}

if args.subhead:
    movie_dict["subhead"] = args.subhead

if args.old:
    movie_dict["old_rating"] = args.old_rating
    movie_dict["time_category"] = args.old_how_old
else:
    movie_dict["rewatch"] = args.rewatch
    movie_dict["characters"] = args.charact
    movie_dict["super"] = args.supercal
    movie_dict["pace"] = args.pacing
    movie_dict["cinema"] = args.cinema
    movie_dict["structure"] = args.structure
    movie_dict["vibe"] = args.vibe
    movie_dict["watched"] = args.date_watched

with open("movie-jsons/" + args.short_title + ".json", "w") as outfile:
    json.dump(movie_dict, outfile)
