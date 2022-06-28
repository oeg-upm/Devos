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



Document  --> Document   :citedBy  

Document  --> Document   :cites  

Document  --> Document   :reproducedIn  

LegalDecision  --> LegalDecision   :reversedBy  

Agent  --> Agent   :interviewee  

Document  --> Document   :translationOf  

LegalDecision  --> LegalDecision   :affirmedBy  

Event  --> Document   :presents  

LegalDecision  --> LegalDecision   :subsequentLegalDecision  

Event  --> Agent   :organizer  

Document  --> Event   :presentedAt  

Agent  --> Agent   :interviewer  

```