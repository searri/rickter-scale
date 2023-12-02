import os, json, datetime

movies = []
for f in os.listdir("movie-jsons"):
    with open("movie-jsons/" + f, "r") as infile:
        this_movie = json.load(infile)

    # Filename without ".json"
    this_movie["short_title"] = f[:-5]

    # TODO: Old movie conditional

    # Datetime object of watch date
    this_movie["date"] = datetime.datetime.strptime(this_movie["watched"], "%Y-%m-%d")

    movies.append(this_movie)

movies_sorted = sorted(movies, key=lambda x: x["date"])

for i, item in enumerate(movies_sorted):
    # TODO: Old movie conditional

    with open("_posts/" + item["watched"] + "-" + item["short_title"] + ".md", "w") as outfile:
        outfile.write("---\nlayout: default\n")
        outfile.write("date: " + item["watched"] + "\n")
        outfile.write("img: " + item["short_title"] + ".jpg\n")
        outfile.write("alt: " + item["title"] + " movie poster\n")
        outfile.write("thumbnail-img: " + item["short_title"] + "-small.png\n")
        outfile.write("rewatch: " + str(item["rewatch"]) + "\n")
        outfile.write("characters: " + str(item["characters"]) + "\n")
        outfile.write("super: " + str(item["super"]) + "\n")
        outfile.write("pace: " + str(item["pace"]) + "\n")
        outfile.write("cinema: " + str(item["cinema"]) + "\n")
        outfile.write("structure: " + str(item["structure"]) + "\n")
        outfile.write("vibe: " + item["vibe"] + "\n")
        outfile.write("---\n")
