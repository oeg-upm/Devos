```mermaid
	classDiagram

    
    class `LearningGoal` {
    
    }

    class `LearningPath` {
    
    }

    class `LearningPreference` {
    
    }

    class `EducationalResource` {
    
    }

    class `LearningOutcome` {
    
    }

    class `Recommendation` {
    
    }

    class `KnowledgeTopic` {
    
    }



`KnowledgeTopic`  --> `EducationalResource`   :hasEducationalResource  

`Recommendation`  --> `LearningPath`   :definesLearningPath  

`EducationalResource`  --> `KnowledgeTopic`   :hasKnowledgeTopic  

`LearningPath`  --> `KnowledgeTopic`   :consistsOfKnowledge  

`KnowledgeTopic`  --> `LearningOutcome`   :hasLearningOutcome  

`LearningPath`  --> `LearningGoal`   :hasLearningGoal  

```