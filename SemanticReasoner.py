import Software, Tutorials, Fields, Languages
object_lists = [Software.Software, Tutorials.Tutorials, Fields.Fields, Languages.Languages]

def FetchObject(ID, search_lists=object_lists):
    for search_list in search_lists:
        for s_object in search_list:
            try:
                if s_object["ID"] == ID:
                    return s_object
            except KeyError:
                print("ERROR: detected an object without ID")
    return 0

def BranchOf(object, depth=0, search_lists=object_lists):
    branch = [object]
    if 'BranchOf' in object.keys():
        parent = FetchObject(object["BranchOf"], search_lists=search_lists)
        if parent == 0:
            branch.append({'ID': object["BranchOf"]})
            return branch
        else:
            branch.append(parent)
        if depth==1:
            return branch
        else:
            branch += BranchOf(parent, depth=depth-1)[1:]
    return branch

def Requirements(object, depth=0, search_lists=object_lists):
    requirements = []
    if 'Requires' in object.keys():
        requirements_IDs = object["Requires"]
        if type(requirements_IDs) is not list:
            requirements_IDs = [requirements_IDs]
        for requirement_ID in requirements_IDs:
            requirement = FetchObject(requirement_ID, search_lists=search_lists)
            if requirement == 0:
                requirements.append({'ID': requirement_ID})
            else:
                requirements.append(requirement)
                if not(depth==1):
                    requirements += Requirements(requirement, depth=depth-1)
    return requirements

def IDs(objects_list):
    return [_object["ID"] for _object in objects_list]

def UsefulFor(object_ID, search_lists=object_lists):
    usefulFor = []
    for search_list in search_lists:
        for s_object in search_list:
            if 'UsefulIn' in s_object.keys():
                uses = s_object['UsefulIn']
                if type(uses) is not list:
                    uses = [uses]
                if object_ID in uses:
                    usefulFor.append(s_object)
    return usefulFor

def TutorialOf(object_ID, search_lists=object_lists):
    tutorialOf = []
    for search_list in search_lists:
        for s_object in search_list:
            if 'TutorialOf' in s_object.keys():
                uses = s_object['TutorialOf']
                if type(uses) is not list:
                    uses = [uses]
                if object_ID in uses:
                    tutorialOf.append(s_object)
    return tutorialOf


def CompileLearningResources(object_ID):
    _object = FetchObject(object_ID)
    useful_for_object = UsefulFor(object_ID)
    if not(_object == 0):
        requirements = Requirements(_object, depth=1)
    else:
        requirements = []
    print("Topic: " + object_ID + "\n")
    print("1. Useful for " + object_ID)
    for a in IDs(useful_for_object):
        print("\t" + a)
    print("2. Requirements for " + object_ID)
    for a in IDs(requirements):
        print("\t" + a)
    print("3. Tutorials for " + object_ID)
    tutorials = TutorialOf(object_ID)
    for tutorial in tutorials:
        print("\t" + tutorial["Title"] + " : " + tutorial["Link"])
    print("4. Tutorials for related topics")
    for topic in useful_for_object + requirements:
        print("\t" + topic["ID"])
        tutorials = TutorialOf(topic["ID"])
        for tutorial in tutorials:
            print("\t\t" + tutorial["Title"] + " : " + tutorial["Link"])

CompileLearningResources('Numpy')