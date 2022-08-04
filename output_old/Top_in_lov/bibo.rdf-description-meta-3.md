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

Document  --> Document   :reproducedIn  

LegalDecision  --> LegalDecision   :reversedBy  

Agent  --> Agent   :interviewee  

Document  --> Document   :citedBy  

Document  --> Document   :translationOf  

LegalDecision  --> LegalDecision   :affirmedBy  

Agent  --> Agent   :interviewer  

```