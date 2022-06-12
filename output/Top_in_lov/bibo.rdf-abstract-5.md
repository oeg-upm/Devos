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

Document  --> Document   :translationOf  

Event  --> Agent   :organizer  

Agent  --> Agent   :interviewer  

Document  --> RDFSResource   :transcriptOf  

Document  --> Document   :citedBy  

Document  --> Document   :reproducedIn  

LegalDecision  --> LegalDecision   :subsequentLegalDecision  

Document  --> Event   :presentedAt  

Agent  --> Agent   :interviewee  

LegalDecision  --> LegalDecision   :reversedBy  

Document  --> Document   :cites  

Event  --> Document   :presents  


```