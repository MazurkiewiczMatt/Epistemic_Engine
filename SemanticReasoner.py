import Software, Tutorials, Fields
object_lists = [Software.Software, Tutorials.Tutorials, Fields.Fields]

def FetchObject(ID, search_lists=object_lists):
    for search_list in search_lists:
        for s_object in search_list:
            try:
                if s_object["ID"] == ID:
                    return s_object
            except KeyError:
                print("ERROR: detected an object without ID")
    return 0

def BranchOf(object, depth=0):
    branch = [object]
    if 'BranchOf' in object.keys():
        parent = FetchObject(object["BranchOf"])
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

def Requirements(object, depth=0):
    requirements = []
    if 'Requires' in object.keys():
        requirements_IDs = object["Requires"]
        if type(requirements_IDs) is not list:
            requirements_IDs = [requirements_IDs]
        for requirement_ID in requirements_IDs:
            requirement = FetchObject(requirement_ID)
            if requirement == 0:
                requirements.append(requirement_ID)
            else:
                requirements.append(requirement)
                if not(depth==1):
                    requirements += Requirements(requirement, depth=depth-1)
    return requirements

print(BranchOf(FetchObject("SignalProcessing"), depth=1))