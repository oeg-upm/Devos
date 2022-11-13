```mermaid
	classDiagram

    


Skill  --> KnowledgeTopic   :hasKnowledgeTopic  

Methodology  --> KnowledgeTopic   :hasKnowledgeTopic  

KnowledgeTopic  --> LearningOutcome   :hasLearningOutcome  

Skill  --> KnowledgeTopic   :requiresKnowledge  

KnowledgeTopic  --> EducationalResource   :hasEducationalResource  

Recommendation  --> LearningPath   :definesLearningPath  

EducationalResource  --> KnowledgeTopic   :hasKnowledgeTopic  

LearningPath  --> KnowledgeTopic   :consistsOfKnowledge  

Skill  --> LearningOutcome   :hasLearningOutcome  

UserProfile  --> LearningPath   :definesLearningPath  

Test  --> KnowledgeTopic   :testKnowledgeTopic  

LearningPath  --> LearningGoal   :hasLearningGoal  

Theory  --> KnowledgeTopic   :hasKnowledgeTopic  

Exercise  --> KnowledgeTopic   :hasKnowledgeTopic  

```