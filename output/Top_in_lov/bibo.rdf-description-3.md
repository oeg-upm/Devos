```mermaid
	classDiagram

    
    class Document {
    
    }

    class Agent {
    
    }

    class LegalDecision {
    
    }



LegalDecision  --> LegalDecision   :affirmedBy  

Document  --> Document   :translationOf  

Agent  --> Agent   :interviewer  

Document  --> Document   :citedBy  

Document  --> Document   :reproducedIn  

LegalDecision  --> LegalDecision   :subsequentLegalDecision  

Agent  --> Agent   :interviewee  

LegalDecision  --> LegalDecision   :reversedBy  

Document  --> Document   :cites  


```