from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    def __str__(self):
        return "Objecto Familia"

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
         member['id']=self._generateId()
         self._members.append(member)

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            #if id == member.get('id'):
            if  id == member['id']:
                return member
        return None


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members


family = FamilyStructure('Cantudo')
member = {
    'name': 'Paco',
    'address': 'Castillo 27'
}

member_two = { 
    'name':'Ana',
    'address': 'Avd. Andalucia 8'
}
family.add_member(member)
family.add_member(member_two)
print(family.get_all_members())