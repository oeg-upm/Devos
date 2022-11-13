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



Exercise  --> KnowledgeTopic   :hasKnowledgeTopic  

LearningPath  --> KnowledgeTopic   :consistsOfKnowledge  

LearningPreference  --> UserProfile   :storedIn  

Theory  --> KnowledgeTopic   :hasKnowledgeTopic  

Test  --> KnowledgeTopic   :testKnowledgeTopic  

EducationalResource  --> Accessibility   :accessibility  

User  --> Test   :solves  

EducationalResource  --> KnowledgeTopic   :hasKnowledgeTopic  

PsycologicalParameter  --> UserProfile   :storedIn  

UserProfile  --> Accessibility   :accessibility  

User  --> UserProfile   :hasProfile  

Skill  --> KnowledgeTopic   :requiresKnowledge  

KnowledgeTopic  --> LearningOutcome   :hasLearningOutcome  

AcademicParameter  --> UserProfile   :storedIn  

User  --> UserLogs   :generatesLogs  

UserProfile  --> LearningPath   :definesLearningPath  

KnowledgeTopic  --> Exercise   :hasExercise  

KnowledgeTopic  --> EducationalResource   :hasEducationalResource  

Methodology  --> KnowledgeTopic   :hasKnowledgeTopic  

User  --> Answer   :givesAnswer  

Skill  --> Classification   :hasClassification  

KnowledgeTopic  --> Theory   :hasTheory  

LearningGoal  --> UserProfile   :storedIn  

EducationalResource  --> MultimediaData   :hasMultimediaData  

Skill  --> KnowledgeTopic   :hasKnowledgeTopic  

User  --> Exercise   :solves  

EducationalResource  --> QualityIndicator   :hasQuality  

Recommendation  --> UserProfile   :generatedFrom  

KnowledgeTopic  --> Methodology   :hasMethodology  

Skill  --> LearningOutcome   :hasLearningOutcome  

```