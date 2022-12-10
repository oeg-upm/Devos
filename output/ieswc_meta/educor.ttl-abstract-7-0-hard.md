```mermaid
	classDiagram

    
    class `Recommendation` {
    
    }

    class `LearningOutcome` {
    
    }

    class `KnowledgeTopic` {
    
    }

    class `LearningPreference` {
    
    }

    class `LearningGoal` {
    
    }

    class `EducationalResource` {
    
    }

    class `LearningPath` {
    
    }



`EducationalResource`  --> `KnowledgeTopic`   :hasKnowledgeTopic  

`LearningPath`  --> `KnowledgeTopic`   :consistsOfKnowledge  

`KnowledgeTopic`  --> `EducationalResource`   :hasEducationalResource  

`KnowledgeTopic`  --> `LearningOutcome`   :hasLearningOutcome  

`LearningPath`  --> `LearningGoal`   :hasLearningGoal  

`Recommendation`  --> `LearningPath`   :definesLearningPath  

```