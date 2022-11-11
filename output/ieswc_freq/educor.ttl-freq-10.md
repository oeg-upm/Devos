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



UserProfile  --> Accessibility   :accessibility  

EducationalResource  --> QualityIndicator   :hasQuality  

UserProfile  --> LearningPath   :definesLearningPath  

Theory  --> KnowledgeTopic   :hasKnowledgeTopic  

KnowledgeTopic  --> EducationalResource   :hasEducationalResource  

Test  --> KnowledgeTopic   :testKnowledgeTopic  

Exercise  --> Question   :hasQuestion  

Exercise  --> KnowledgeTopic   :hasKnowledgeTopic  

Skill  --> KnowledgeTopic   :requiresKnowledge  

PsycologicalParameter  --> UserProfile   :storedIn  

AcademicParameter  --> UserProfile   :storedIn  

KnowledgeTopic  --> Exercise   :hasExercise  

Recommendation  --> LearningPath   :definesLearningPath  

EducationalResource  --> Accessibility   :accessibility  

KnowledgeTopic  --> Methodology   :hasMethodology  

User  --> Exercise   :solves  

EducationalResource  --> KnowledgeTopic   :hasKnowledgeTopic  

LearningGoal  --> UserProfile   :storedIn  

User  --> Answer   :givesAnswer  

LearningPath  --> KnowledgeTopic   :consistsOfKnowledge  

Methodology  --> KnowledgeTopic   :hasKnowledgeTopic  

Recommendation  --> UserProfile   :generatedFrom  

User  --> UserProfile   :hasProfile  

User  --> UserLogs   :generatesLogs  

KnowledgeTopic  --> Theory   :hasTheory  

KnowledgeTopic  --> LearningOutcome   :hasLearningOutcome  

LearningPath  --> LearningGoal   :hasLearningGoal  

Skill  --> KnowledgeTopic   :hasKnowledgeTopic  

Question  --> Answer   :hasAnswer  

LearningPreference  --> UserProfile   :storedIn  

EducationalResource  --> MultimediaData   :hasMultimediaData  

Skill  --> Classification   :hasClassification  

```