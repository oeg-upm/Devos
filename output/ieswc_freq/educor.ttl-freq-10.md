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

    class LearningPath {
    
    }

    class UserLogs {
    
    }

    class Classification {
    
    }

    class EducationalResource {
    
    }

    class LearningGoal {
    
    }



UserProfile  --> LearningPath   :definesLearningPath  

User  --> Exercise   :solves  

Recommendation  --> LearningPath   :definesLearningPath  

LearningPath  --> KnowledgeTopic   :consistsOfKnowledge  

EducationalResource  --> Accessibility   :accessibility  

Question  --> Answer   :hasAnswer  

KnowledgeTopic  --> Theory   :hasTheory  

KnowledgeTopic  --> LearningOutcome   :hasLearningOutcome  

KnowledgeTopic  --> Exercise   :hasExercise  

LearningGoal  --> UserProfile   :storedIn  

EducationalResource  --> QualityIndicator   :hasQuality  

AcademicParameter  --> UserProfile   :storedIn  

User  --> Answer   :givesAnswer  

User  --> UserProfile   :hasProfile  

KnowledgeTopic  --> EducationalResource   :hasEducationalResource  

Test  --> KnowledgeTopic   :testKnowledgeTopic  

Skill  --> KnowledgeTopic   :hasKnowledgeTopic  

Skill  --> KnowledgeTopic   :requiresKnowledge  

Recommendation  --> UserProfile   :generatedFrom  

PsycologicalParameter  --> UserProfile   :storedIn  

EducationalResource  --> MultimediaData   :hasMultimediaData  

Theory  --> KnowledgeTopic   :hasKnowledgeTopic  

Skill  --> Classification   :hasClassification  

KnowledgeTopic  --> Methodology   :hasMethodology  

Methodology  --> KnowledgeTopic   :hasKnowledgeTopic  

EducationalResource  --> KnowledgeTopic   :hasKnowledgeTopic  

Exercise  --> KnowledgeTopic   :hasKnowledgeTopic  

User  --> UserLogs   :generatesLogs  

LearningPath  --> LearningGoal   :hasLearningGoal  

UserProfile  --> Accessibility   :accessibility  

LearningPreference  --> UserProfile   :storedIn  

Exercise  --> Question   :hasQuestion  

```