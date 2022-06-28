```mermaid
	classDiagram

    
    class Document {
    
    }

    class Thing {
    
    }

    class Agent {
    
    }



Document  --> Thing   :topic  

Thing  --> Agent   :maker  

Thing  --> Document   :homepage  

Thing  --> Document   :page  

Agent  --> Thing   :mbox  

Agent  --> Document   :interest  

Agent  --> Document   :weblog  

Agent  --> Document   :tipjar  

Document  --> Thing   :primaryTopic  

Agent  --> Thing   :topic_interest  

Agent  --> Thing   :made  

Agent  --> Document   :openid  

```