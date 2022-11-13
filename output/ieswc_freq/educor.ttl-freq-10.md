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



Exercise  --> Question   :hasQuestion  

Recommendation  --> UserProfile   :generatedFrom  

Methodology  --> KnowledgeTopic   :hasKnowledgeTopic  

PsycologicalParameter  --> UserProfile   :storedIn  

User  --> Exercise   :solves  

Exercise  --> KnowledgeTopic   :hasKnowledgeTopic  

User  --> Answer   :givesAnswer  

Skill  --> Classification   :hasClassification  

KnowledgeTopic  --> LearningOutcome   :hasLearningOutcome  

LearningPreference  --> UserProfile   :storedIn  

Recommendation  --> LearningPath   :definesLearningPath  

EducationalResource  --> KnowledgeTopic   :hasKnowledgeTopic  

LearningGoal  --> UserProfile   :storedIn  

EducationalResource  --> QualityIndicator   :hasQuality  

Skill  --> KnowledgeTopic   :hasKnowledgeTopic  

EducationalResource  --> Accessibility   :accessibility  

User  --> UserProfile   :hasProfile  

Question  --> Answer   :hasAnswer  

Theory  --> KnowledgeTopic   :hasKnowledgeTopic  

AcademicParameter  --> UserProfile   :storedIn  

Skill  --> KnowledgeTopic   :requiresKnowledge  

KnowledgeTopic  --> Methodology   :hasMethodology  

KnowledgeTopic  --> EducationalResource   :hasEducationalResource  

LearningPath  --> LearningGoal   :hasLearningGoal  

KnowledgeTopic  --> Theory   :hasTheory  

User  --> UserLogs   :generatesLogs  

UserProfile  --> LearningPath   :definesLearningPath  

EducationalResource  --> MultimediaData   :hasMultimediaData  

User  --> Test   :solves  

Skill  --> LearningOutcome   :hasLearningOutcome  

KnowledgeTopic  --> Exercise   :hasExercise  

Test  --> KnowledgeTopic   :testKnowledgeTopic  

LearningPath  --> KnowledgeTopic   :consistsOfKnowledge  

UserProfile  --> Accessibility   :accessibility  

```