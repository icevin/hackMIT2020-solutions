
danger_words = [" drop ", " delete ", "information_schema.tables", "information_schema.columns", "information_schema.schemata","noam_chomsky"]

def sanitize_query(query):
    # invalidate queries containing these words
    danger_words = [" drop ", " delete ", "information_schema.tables", "information_schema.columns", "information_schema.schemata","noam_chomsky"]
    for word in danger_words:
        if word in query:
            return False
    query = query.replace(" ", "")
    query = query.replace("%20", "")
    query = query.replace("'", "")
    query = query.encode("ascii").decode("utf-8")
    print(query)
    return query

while True:
    x = input()
    print(sanitize_query(x))
    # print(x.encode("ascii").decode("utf-8"))
    # invalidate queries containing these words
        # for word in danger_words:
        #     if word in x:
        #         print("false")
        #         print(word)