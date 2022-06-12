```mermaid
	classDiagram

    
    class Document {
    
    }

    class Agent {
    
    }

    class LegalDecision {
    
    }



LegalDecision  --> LegalDecision   :affirmedBy  

Agent  --> Agent   :interviewee  

LegalDecision  --> LegalDecision   :subsequentLegalDecision  

LegalDecision  --> LegalDecision   :reversedBy  

Agent  --> Agent   :interviewer  

Document  --> Document   :cites  

Document  --> Document   :reproducedIn  

Document  --> Document   :citedBy  

Document  --> Document   :translationOf  

```