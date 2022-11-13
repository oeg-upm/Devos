```mermaid
	classDiagram

    
    class KnowledgeTopic {
    
    }

    class EducationalResource {
    
    }

    class UserProfile {
    
    }

    class User {
    
    }

    class Skill {
    
    }

    class Exercise {
    
    }

    class LearningPath {
    
    }

    class Recommendation {
    
    }

    class Question {
    
    }

    class Methodology {
    
    }



KnowledgeTopic  --> EducationalResource   :hasEducationalResource  

User  --> Exercise   :solves  

Exercise  --> KnowledgeTopic   :hasKnowledgeTopic  

Skill  --> KnowledgeTopic   :hasKnowledgeTopic  

User  --> UserLogs   :generatesLogs  

KnowledgeTopic  --> Exercise   :hasExercise  

EducationalResource  --> MultimediaData   :hasMultimediaData  

User  --> Answer   :givesAnswer  

UserProfile  --> LearningPath   :definesLearningPath  

Theory  --> KnowledgeTopic   :hasKnowledgeTopic  

EducationalResource  --> QualityIndicator   :hasQuality  

LearningPreference  --> UserProfile   :storedIn  

Recommendation  --> UserProfile   :generatedFrom  

EducationalResource  --> KnowledgeTopic   :hasKnowledgeTopic  

Question  --> Answer   :hasAnswer  

LearningPath  --> KnowledgeTopic   :consistsOfKnowledge  

LearningGoal  --> UserProfile   :storedIn  

KnowledgeTopic  --> Methodology   :hasMethodology  

Skill  --> LearningOutcome   :hasLearningOutcome  

PsycologicalParameter  --> UserProfile   :storedIn  

KnowledgeTopic  --> Theory   :hasTheory  

EducationalResource  --> Accessibility   :accessibility  

Skill  --> Classification   :hasClassification  

AcademicParameter  --> UserProfile   :storedIn  

UserProfile  --> Accessibility   :accessibility  

KnowledgeTopic  --> LearningOutcome   :hasLearningOutcome  

Skill  --> KnowledgeTopic   :requiresKnowledge  

Exercise  --> Question   :hasQuestion  

Methodology  --> KnowledgeTopic   :hasKnowledgeTopic  

User  --> Test   :solves  

User  --> UserProfile   :hasProfile  

LearningPath  --> LearningGoal   :hasLearningGoal  

Test  --> KnowledgeTopic   :testKnowledgeTopic  

Recommendation  --> LearningPath   :definesLearningPath  

```