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

    class RDFSResource {
    
    }



Document  --> RDFSResource   :reviewOf  

LegalDecision  --> LegalDecision   :affirmedBy  

Agent  --> Agent   :interviewee  

LegalDecision  --> LegalDecision   :subsequentLegalDecision  

Document  --> RDFSResource   :transcriptOf  

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