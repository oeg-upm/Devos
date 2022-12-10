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



`UserProfile`  --> `LearningPath`   :definesLearningPath  

`Skill`  --> `KnowledgeTopic`   :requiresKnowledge  

`User`  --> `UserProfile`   :hasProfile  

`Skill`  --> `KnowledgeTopic`   :hasKnowledgeTopic  

`EducationalResource`  --> `KnowledgeTopic`   :hasKnowledgeTopic  

`LearningPath`  --> `KnowledgeTopic`   :consistsOfKnowledge  

`User`  --> `Exercise`   :solves  

`KnowledgeTopic`  --> `Exercise`   :hasExercise  

`Exercise`  --> `KnowledgeTopic`   :hasKnowledgeTopic  

`KnowledgeTopic`  --> `EducationalResource`   :hasEducationalResource  

```