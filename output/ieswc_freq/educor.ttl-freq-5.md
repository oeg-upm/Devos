```mermaid
	classDiagram

    
    class KnowledgeTopic {
    
    }

    class UserProfile {
    
    }

    class Answer {
    
    }

    class Exercise {
    
    }

    class Accessibility {
    
    }



Exercise  --> KnowledgeTopic   :hasKnowledgeTopic  

UserProfile  --> LearningPath   :definesLearningPath  

KnowledgeTopic  --> LearningOutcome   :hasLearningOutcome  

KnowledgeTopic  --> EducationalResource   :hasEducationalResource  

Skill  --> KnowledgeTopic   :hasKnowledgeTopic  

KnowledgeTopic  --> Theory   :hasTheory  

EducationalResource  --> Accessibility   :accessibility  

LearningPath  --> KnowledgeTopic   :consistsOfKnowledge  

Recommendation  --> UserProfile   :generatedFrom  

AcademicParameter  --> UserProfile   :storedIn  

PsycologicalParameter  --> UserProfile   :storedIn  

Question  --> Answer   :hasAnswer  

Skill  --> KnowledgeTopic   :requiresKnowledge  

Test  --> KnowledgeTopic   :testKnowledgeTopic  

LearningPreference  --> UserProfile   :storedIn  

EducationalResource  --> KnowledgeTopic   :hasKnowledgeTopic  

Methodology  --> KnowledgeTopic   :hasKnowledgeTopic  

Theory  --> KnowledgeTopic   :hasKnowledgeTopic  

KnowledgeTopic  --> Exercise   :hasExercise  

UserProfile  --> Accessibility   :accessibility  

User  --> Answer   :givesAnswer  

User  --> UserProfile   :hasProfile  

User  --> Exercise   :solves  

KnowledgeTopic  --> Methodology   :hasMethodology  

Exercise  --> Question   :hasQuestion  

LearningGoal  --> UserProfile   :storedIn  

```