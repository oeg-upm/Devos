```mermaid
	classDiagram

    
    class Document {
    
    }

    class Thing {
    
    }

    class Agent {
    
    }

    class Person {
    
    }



Document  --> Thing   :topic  

Document  --> Thing   :primaryTopic  

Agent  --> Thing   :mbox  

Thing  --> Agent   :maker  

Agent  --> Thing   :made  

Person  --> Document   :publications  

Agent  --> Document   :openid  

Thing  --> Document   :homepage  

Thing  --> Document   :page  

Agent  --> Document   :tipjar  

Person  --> Thing   :pastProject  

Person  --> Person   :knows  

Agent  --> Document   :interest  

Person  --> Document   :schoolHomepage  

Person  --> Document   :workplaceHomepage  

Person  --> Thing   :currentProject  

Person  --> Document   :workInfoHomepage  

Agent  --> Document   :weblog  

Agent  --> Thing   :topic_interest  

```