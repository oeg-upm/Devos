```mermaid
	classDiagram

    
    class Document {
    
    }

    class Agent {
    
    }

    class LegalDecision {
    
    }

    class Event {
    
    }



LegalDecision  --> LegalDecision   :subsequentLegalDecision  

Document  --> Event   :presentedAt  

Document  --> Document   :cites  

Document  --> Document   :reproducedIn  

LegalDecision  --> LegalDecision   :reversedBy  

Event  --> Agent   :organizer  

Event  --> Document   :presents  

Agent  --> Agent   :interviewee  

Document  --> Document   :citedBy  

Document  --> Document   :translationOf  

LegalDecision  --> LegalDecision   :affirmedBy  

Agent  --> Agent   :interviewer  

```