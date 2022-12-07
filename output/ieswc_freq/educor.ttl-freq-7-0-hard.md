```mermaid
	classDiagram

    
    class `KnowledgeTopic` {
    
    }

    class `EducationalResource` {
    
    }

    class `UserProfile` {
    
    }

    class `User` {
    
    }

    class `Skill` {
    
    }

    class `Exercise` {
    
    }

    class `LearningPath` {
    
    }



`LearningPath`  --> `KnowledgeTopic`   :consistsOfKnowledge  

`Skill`  --> `KnowledgeTopic`   :requiresKnowledge  

`User`  --> `UserProfile`   :hasProfile  

`Skill`  --> `KnowledgeTopic`   :hasKnowledgeTopic  

`Exercise`  --> `KnowledgeTopic`   :hasKnowledgeTopic  

`KnowledgeTopic`  --> `EducationalResource`   :hasEducationalResource  

`UserProfile`  --> `LearningPath`   :definesLearningPath  

`KnowledgeTopic`  --> `Exercise`   :hasExercise  

`EducationalResource`  --> `KnowledgeTopic`   :hasKnowledgeTopic  

`User`  --> `Exercise`   :solves  

```