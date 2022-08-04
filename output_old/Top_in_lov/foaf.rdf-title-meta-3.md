```mermaid
	classDiagram

    
    class Document {
    
    }

    class Thing {
    
    }

    class Agent {
    
    }



Document  --> Thing   :primaryTopic  

Agent  --> Document   :weblog  

Agent  --> Thing   :mbox  

Thing  --> Document   :homepage  

Agent  --> Thing   :made  

Agent  --> Document   :interest  

Thing  --> Agent   :maker  

Agent  --> Thing   :topic_interest  

Document  --> Thing   :topic  

Thing  --> Document   :page  

Agent  --> Document   :tipjar  

Agent  --> Document   :openid  

```