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



KnowledgeTopic  --> Methodology   :hasMethodology  

LearningPreference  --> UserProfile   :storedIn  

LearningGoal  --> UserProfile   :storedIn  

EducationalResource  --> MultimediaData   :hasMultimediaData  

User  --> Exercise   :solves  

EducationalResource  --> Accessibility   :accessibility  

PsycologicalParameter  --> UserProfile   :storedIn  

UserProfile  --> Accessibility   :accessibility  

User  --> UserLogs   :generatesLogs  

KnowledgeTopic  --> Exercise   :hasExercise  

Recommendation  --> UserProfile   :generatedFrom  

Exercise  --> KnowledgeTopic   :hasKnowledgeTopic  

LearningPath  --> KnowledgeTopic   :consistsOfKnowledge  

KnowledgeTopic  --> LearningOutcome   :hasLearningOutcome  

Skill  --> Classification   :hasClassification  

Skill  --> LearningOutcome   :hasLearningOutcome  

User  --> Answer   :givesAnswer  

Skill  --> KnowledgeTopic   :hasKnowledgeTopic  

UserProfile  --> LearningPath   :definesLearningPath  

User  --> UserProfile   :hasProfile  

Theory  --> KnowledgeTopic   :hasKnowledgeTopic  

AcademicParameter  --> UserProfile   :storedIn  

Test  --> KnowledgeTopic   :testKnowledgeTopic  

Skill  --> KnowledgeTopic   :requiresKnowledge  

User  --> Test   :solves  

EducationalResource  --> QualityIndicator   :hasQuality  

EducationalResource  --> KnowledgeTopic   :hasKnowledgeTopic  

KnowledgeTopic  --> EducationalResource   :hasEducationalResource  

KnowledgeTopic  --> Theory   :hasTheory  

Methodology  --> KnowledgeTopic   :hasKnowledgeTopic  

```