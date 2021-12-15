import Software, Tutorials, Fields
object_lists = [Software.Software, Tutorials.Tutorials, Fields.Fields]

def FetchObject(ID, search_lists=object_lists):
    for search_list in search_lists:
        for s_object in search_list:
            if s_object["ID"] == ID:
                return s_object
    return 0


print(FetchObject("FourierTransform"))