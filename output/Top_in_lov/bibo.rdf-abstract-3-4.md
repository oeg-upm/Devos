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



LegalDecision  --> LegalDecision   :affirmedBy  

Agent  --> Agent   :interviewee  

LegalDecision  --> LegalDecision   :subsequentLegalDecision  

LegalDecision  --> LegalDecision   :reversedBy  

Event  --> Agent   :organizer  

Agent  --> Agent   :interviewer  

Document  --> Document   :cites  

Document  --> Event   :presentedAt  

Document  --> Document   :reproducedIn  

Document  --> Document   :citedBy  

Event  --> Document   :presents  

Document  --> Document   :translationOf  

```