from abc import ABCMeta, abstractmethod

class Fertilizers(metaclass=ABCMeta):

    def __init__(self,name,price,description,rating):
        self.name=name
        self.price=price
        self.description=description
        self.rating=rating


    @abstractmethod
    def getListOfFertilizers(self):
        pass

class Fertilizers_Updates(Fertilizers):

    def __init__(self,name,price,weight,description,rating):
        Fertilizers.__init__(self,name,price,description,rating)
        self.weight=weight

    @staticmethod
    def getListOfFertilizers():
        obj1=Fertilizers_Updates('Urban Farm LL128','Rs/=3722','5.5 Kg',
                         """Urban Farm LL128 is a liquid fertilizer that contains enzymes designed for root activation, making it perfect for filling in dead spots.
            It is the only instant lawn fertilizer with both calcium and iron, but it can burn your grass if you overapply""",'4.0/5.0')
        obj2=Fertilizers_Updates('Milorganite 0636','Rs/=3262','16.5 Kg',
                         """Milorganite 0636 is an organic nitrogen that's made of heat-dried microbes, enabling it to quickly penetrate and re-energize the soil.
            As an added bonus, the smell can help keep pests like rabbits from nibbling on your grass, but you will have to deal with the odor as well""", '4.0/5.0')
        obj4=Fertilizers_Updates("Garden Peals Gypsum","Rs/=3110","11.3 Kg",
                         """Garden Peals Gypsum is a fantastic choice if you have problems with clay in your soil, as gypsum breaks it up and increases water
            absorption. It also leaches salt out of the dirt to restore the proper soil structure,allowing nutrients to reach the roots.""","4.9/5,0")
        obj5=Fertilizers_Updates("Safer Brand 9333 Ringer","Rs/=5953","11.35 Kg",
                         """Safer Brand 9333 Ringer uses plant-based nutrients instead of bio-solids, so it leaves no odors behind and is safe to walk on. It feeds
            the beneficial bacteria and fungi deep in your soil, giving your grass plenty of the fuel it needs to grow green and lush.""","4.6/5.0")

        return [obj1,obj2,obj4,obj5]
                

class Alternatives_Of_Fertilizers(Fertilizers):

    def __init__(self,name,description,rating,price):
        Fertilizers.__init__(self,name,price,description,rating)

    @staticmethod
    def getListOfFertilizers():
        obj6=Alternatives_Of_Fertilizers("Coffee Grounds","Best use: Alkaline soils. Acid-loving plants like blueberries and azaleas.","4.1/5.0","Rs/=1566")
        obj7=Alternatives_Of_Fertilizers("Eggshells","Best use: Slug-infested gardens. Calcium-craving plants such as tomatoes, squash and peppers","4.0/5.0","Rs/=1384")
        obj8=Alternatives_Of_Fertilizers("Compost","Best use: All-purpose. Especially good for dense, compacted soil.","3.9/5.0","RS/=2123")
        obj9=Alternatives_Of_Fertilizers("Wood Ash","Best use: Acidic soil. A substitute for garden lime.","3.0/5.0","Rs/=1720")

        return [obj6,obj7,obj8,obj9]
                

class Suggestions_Of_Fertilizers:

    def __init__(self,suggestion,UseFor):
        self.suggestion=suggestion
        self.UseFor=UseFor

    @staticmethod
    def getListOfSuggestedFertilizers():
        obj10=Suggestions_Of_Fertilizers("Nitrogen, Phosphate, Potash, Sulfur, and Copper","Wheat")
        obj11=Suggestions_Of_Fertilizers("Nitrogen, Potash, Phosphate, Sulfur, and Magnesium","Corn")
        obj12=Suggestions_Of_Fertilizers("Nitrogen, Phosphate and Potash","Soyabean")
        obj13=Suggestions_Of_Fertilizers("Nitrogen, Sulfur, Phosphate and Potash","Oat")
        obj14=Suggestions_Of_Fertilizers("Nitrogen, Phosphorus and Potassium","Wild Rice")
        obj15=Suggestions_Of_Fertilizers("Nitrogen, Phosphate, Copper and Potash","Barley")
        return [obj10,obj11,obj12,obj13,obj14,obj15]
