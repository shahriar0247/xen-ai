import os


def search(said):
    if 'search' in said:
        search_for = said.split("search ")[1]
        if search_for[:3] == "for":
            search_for = search_for.replace("for","",1)

        search_for = quote(search_for)
        if "google" in said:
            search_for = search_for.replace("in%20google%20", "", 1)
            search_for = search_for.replace("google%20", "", 1)
            if search_for.startswith("for%20"):
                search_for = search_for.replace("for%20", "", 1)
            os.system("start https://www.google.com/search?q=" + search_for)
        elif "bing" in said:
            search_for = search_for.replace("in%20bing%20", "", 1)
            search_for = search_for.replace("bing%20", "", 1)
            if search_for.startswith("for%20"):
                search_for = search_for.replace("for%20", "", 1)
            os.system("start https://www.bing.com/search?q=" + search_for)
        elif "yahoo" in said:
            search_for = search_for.replace("in%20yahoo%20", "", 1)
            search_for = search_for.replace("yahoo%20", "", 1)
            if search_for.startswith("for%20"):
                search_for = search_for.replace("for%20", "", 1)
            os.system("start https://search.yahoo.com/search?p=" + search_for)
          