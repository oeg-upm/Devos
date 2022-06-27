```mermaid
	classDiagram

    
    class Document {
    
    }

    class Thing {
    
    }

    class Agent {
    
    }



Agent  --> Document   :tipjar  

Agent  --> Thing   :made  

Document  --> Thing   :topic  

Document  --> Thing   :primaryTopic  

Agent  --> Thing   :topic_interest  

Thing  --> Agent   :maker  

Agent  --> Document   :interest  

Agent  --> Document   :openid  

Thing  --> Document   :homepage  

Agent  --> Thing   :mbox  

Agent  --> Document   :weblog  

Thing  --> Document   :page  

```