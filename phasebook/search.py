from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    
    if not args:
        return USERS
    
    usersToReturn = list() # Storage for users to be returned/displayed
    argsList = list(args.items()) # List of arguments

    for [ i, x ] in argsList: #Loop through args given to sort
        for user in USERS:
            if user not in usersToReturn:

                if ( i == "id" or i == "name" or i == "occupation"):
                    
                    xIsSubstring = user.get(i).lower().find(x.lower())

                    if ( xIsSubstring > -1 ):
                        usersToReturn.append(user)
                
                if ( i == "age" ):
                    age = int(x)

                    if ( age in user.values() 
                          or age - 1 in user.values() 
                          or age + 1 in user.values()):
                        
                        usersToReturn.append(user)

    return usersToReturn
