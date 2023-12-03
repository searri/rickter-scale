import os, json, datetime

movies = []
for f in os.listdir("movie-jsons"):
    with open("movie-jsons/" + f, "r") as infile:
        this_movie = json.load(infile)

    # Filename without ".json"
    this_movie["short_title"] = f[:-5]

    # Datetime object of watch date
    if "old_rating" in this_movie:
        if this_movie["time_category"] == "old":
            this_movie["watched"] = "2020-01-01"
        elif this_movie["time_category"] == "youth":
            this_movie["watched"] = "2014-01-01"
        elif this_movie["time_category"] == "childhood":
            this_movie["watched"] = "2008-01-01"
        elif this_movie["time_category"] == "semirecent":
            this_movie["watched"] = "2022-01-01"
        else:
            assert this_movie["time_category"] == "recent"
            this_movie["watched"] = "2023-01-01"

    this_movie["date"] = datetime.datetime.strptime(this_movie["watched"], "%Y-%m-%d")

    movies.append(this_movie)

movies_sorted = sorted(movies, key=lambda x: x["date"])

for i, item in enumerate(movies_sorted):
    with open("_posts/" + item["watched"] + "-" + item["short_title"] + ".md", "w") as outfile:
        outfile.write("---\nlayout: default\n")
        outfile.write("alt: '" + item["title"] + " stylized movie heading'\n")
        outfile.write("img: " + item["short_title"] + ".jpg\n")
        outfile.write("thumbnail-img: " + item["short_title"] + "-small.png\n")
        outfile.write("date: " + item["watched"] + "\n")
        outfile.write("title: '" + item["title"] + "'\n")

        if "old_rating" in item:
            outfile.write("old: true\n")
            assert item["old_rating"] in {"good", "fine", "bad"}
            outfile.write("rating: " + item["old_rating"] + "\n")

        else:
            outfile.write("old: false\n")
            outfile.write("rewatch: " + str(item["rewatch"]) + "\n")
            outfile.write("characters: " + str(item["characters"]) + "\n")
            outfile.write("super: " + str(item["super"]) + "\n")
            outfile.write("pace: " + str(item["pace"]) + "\n")
            outfile.write("cinema: " + str(item["cinema"]) + "\n")
            outfile.write("structure: " + str(item["structure"]) + "\n")
            outfile.write("vibe: " + item["vibe"] + "\n")

        if "subhead" in item:
            outfile.write("subhead: " + item["subhead"] + "\n")

        outfile.write("---\n")
