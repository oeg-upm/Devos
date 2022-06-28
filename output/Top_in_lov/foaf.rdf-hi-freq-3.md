```mermaid
	classDiagram

    
    class Document {
    
    }

    class Thing {
    
    }

    class Agent {
    
    }



Agent  --> Thing   :topic_interest  

Agent  --> Document   :weblog  

Thing  --> Document   :page  

Agent  --> Document   :openid  

Thing  --> Document   :homepage  

Document  --> Thing   :primaryTopic  

Agent  --> Document   :tipjar  

Agent  --> Document   :interest  

Agent  --> Thing   :made  

Agent  --> Thing   :mbox  

Thing  --> Agent   :maker  

Document  --> Thing   :topic  

```