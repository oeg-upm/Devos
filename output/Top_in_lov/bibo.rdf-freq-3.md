```mermaid
	classDiagram

    
    class Document {
    
    }

    class Agent {
    
    }

    class LegalDecision {
    
    }



LegalDecision  --> LegalDecision   :subsequentLegalDecision  

Document  --> Document   :cites  

Agent  --> Agent   :interviewer  

Document  --> Document   :citedBy  

Agent  --> Agent   :interviewee  

LegalDecision  --> LegalDecision   :affirmedBy  

LegalDecision  --> LegalDecision   :reversedBy  

Document  --> Document   :reproducedIn  

Document  --> Document   :translationOf  

```