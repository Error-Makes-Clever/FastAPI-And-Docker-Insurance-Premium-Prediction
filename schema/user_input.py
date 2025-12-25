from typing import Literal, Annotated
from pydantic import BaseModel, Field, computed_field, field_validator
from config.city_tier import tier_1_cities, tier_2_cities

class UserInput(BaseModel):

    age : Annotated[int, Field(..., description="Age of the user", gt=0, lt=120)]
    weight : Annotated[float, Field(..., description="Weight of the user", gt=0)]
    height : Annotated[float, Field(..., description="Height of the user", gt=0, lt=2.5)]
    income_lpa : Annotated[float, Field(...,description="Income of the user")]
    smoker : Annotated[bool, Field(..., description="Smoker of the user")]
    city : Annotated[str, Field(..., description="City of the user")]
    occupation : Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the user")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height * self.height), 2)
    
    @computed_field 
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        else:
            return "senior"
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def city_tier(self) -> str:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

    @field_validator('city')
    @classmethod
    def normalize_city(cls, value) -> str:
        value = value.strip().title()
        return value