class system:
    def __init__(self, name):
        self.name = name

class human():
    def __init__(self,human_system):
        self.humansystem=[system(name) for name in human_system ]

human1=human(["Respiratory system","digestivesystem","Excretorysystem","Cardiovascularsystem","nervoussystem"])


for i in human1.humansystem:
    print(i.name)