
users = {
    "Hangkong": ['Grilled-Asian-Flank-Steak-513532'],
    "Florian": ['Blue-Moon-Inn-Cheese-Spread-MyRecipes-242160'],
    "Samu":['Lasagna-494544'],
    "Martin":['Beaten-Biscuits-Martha-Stewart','Saucy-Sirloin-Steak-My-Recipes']
}

class UserModelDB:
    
    def get_user_model(self,user):
        return users[user]
        