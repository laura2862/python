class Student():
   def  __init__(self,name,score):
       self.name=name
       self.score=score
   def __str__(self):
       if self.score>=90:
           return f'{self.name}, score: {self.score}, excellent'
       elif self.score >= 70:
           return f'{self.name}, score: {self.score}, good'
       elif self.score >= 60:
           return f'{self.name}, score: {self.score}, satisfied'
       else:
            return f'{self.name}, score: {self.score}, unsatisfied'

   def __del__(self):
        pass
s1= Student('laura',90)
print(s1)



