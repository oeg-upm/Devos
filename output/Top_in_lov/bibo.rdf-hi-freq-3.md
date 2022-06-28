```mermaid
	classDiagram

    
    class Document {
    
    }

    class Agent {
    
    }

    class LegalDecision {
    
    }



Document  --> Document   :citedBy  

Document  --> Document   :cites  

Document  --> Document   :reproducedIn  

LegalDecision  --> LegalDecision   :reversedBy  

Agent  --> Agent   :interviewee  

Document  --> Document   :translationOf  

LegalDecision  --> LegalDecision   :affirmedBy  

LegalDecision  --> LegalDecision   :subsequentLegalDecision  

Agent  --> Agent   :interviewer  

```