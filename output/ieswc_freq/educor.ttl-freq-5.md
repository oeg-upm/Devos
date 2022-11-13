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



Skill  --> KnowledgeTopic   :hasKnowledgeTopic  

LearningGoal  --> UserProfile   :storedIn  

User  --> Exercise   :solves  

KnowledgeTopic  --> EducationalResource   :hasEducationalResource  

UserProfile  --> Accessibility   :accessibility  

User  --> UserProfile   :hasProfile  

Test  --> KnowledgeTopic   :testKnowledgeTopic  

PsycologicalParameter  --> UserProfile   :storedIn  

UserProfile  --> LearningPath   :definesLearningPath  

Exercise  --> KnowledgeTopic   :hasKnowledgeTopic  

Methodology  --> KnowledgeTopic   :hasKnowledgeTopic  

EducationalResource  --> MultimediaData   :hasMultimediaData  

LearningPreference  --> UserProfile   :storedIn  

Skill  --> LearningOutcome   :hasLearningOutcome  

User  --> Answer   :givesAnswer  

KnowledgeTopic  --> Exercise   :hasExercise  

KnowledgeTopic  --> LearningOutcome   :hasLearningOutcome  

EducationalResource  --> QualityIndicator   :hasQuality  

Skill  --> KnowledgeTopic   :requiresKnowledge  

Recommendation  --> UserProfile   :generatedFrom  

Theory  --> KnowledgeTopic   :hasKnowledgeTopic  

User  --> Test   :solves  

EducationalResource  --> KnowledgeTopic   :hasKnowledgeTopic  

LearningPath  --> KnowledgeTopic   :consistsOfKnowledge  

KnowledgeTopic  --> Methodology   :hasMethodology  

KnowledgeTopic  --> Theory   :hasTheory  

Skill  --> Classification   :hasClassification  

User  --> UserLogs   :generatesLogs  

AcademicParameter  --> UserProfile   :storedIn  

EducationalResource  --> Accessibility   :accessibility  

```