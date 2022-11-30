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



UserProfile  --> LearningPath   :definesLearningPath  

KnowledgeTopic  --> Theory   :hasTheory  

Exercise  --> Question   :hasQuestion  

EducationalResource  --> KnowledgeTopic   :hasKnowledgeTopic  

User  --> Answer   :givesAnswer  

KnowledgeTopic  --> Exercise   :hasExercise  

Skill  --> Classification   :hasClassification  

User  --> Exercise   :solves  

PsycologicalParameter  --> UserProfile   :storedIn  

User  --> UserLogs   :generatesLogs  

Recommendation  --> UserProfile   :generatedFrom  

KnowledgeTopic  --> LearningOutcome   :hasLearningOutcome  

AcademicParameter  --> UserProfile   :storedIn  

Recommendation  --> LearningPath   :definesLearningPath  

LearningPath  --> KnowledgeTopic   :consistsOfKnowledge  

EducationalResource  --> MultimediaData   :hasMultimediaData  

Test  --> KnowledgeTopic   :testKnowledgeTopic  

User  --> Test   :solves  

Skill  --> LearningOutcome   :hasLearningOutcome  

LearningPath  --> LearningGoal   :hasLearningGoal  

LearningPreference  --> UserProfile   :storedIn  

User  --> UserProfile   :hasProfile  

EducationalResource  --> Accessibility   :accessibility  

Methodology  --> KnowledgeTopic   :hasKnowledgeTopic  

LearningGoal  --> UserProfile   :storedIn  

Skill  --> KnowledgeTopic   :requiresKnowledge  

UserProfile  --> Accessibility   :accessibility  

Skill  --> KnowledgeTopic   :hasKnowledgeTopic  

KnowledgeTopic  --> Methodology   :hasMethodology  

EducationalResource  --> QualityIndicator   :hasQuality  

Exercise  --> KnowledgeTopic   :hasKnowledgeTopic  

KnowledgeTopic  --> EducationalResource   :hasEducationalResource  

Theory  --> KnowledgeTopic   :hasKnowledgeTopic  

```