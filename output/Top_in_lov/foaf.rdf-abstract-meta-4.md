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



Person  --> Person   :knows  

Person  --> Document   :schoolHomepage  

Person  --> Thing   :pastProject  

Document  --> Thing   :primaryTopic  

Agent  --> Document   :weblog  

Person  --> Document   :workInfoHomepage  

Agent  --> Thing   :mbox  

Thing  --> Document   :homepage  

Agent  --> Thing   :made  

Person  --> Document   :workplaceHomepage  

Agent  --> Document   :interest  

Person  --> Thing   :currentProject  

Thing  --> Agent   :maker  

Agent  --> Thing   :topic_interest  

Document  --> Thing   :topic  

Person  --> Document   :publications  

Thing  --> Document   :page  

Agent  --> Document   :tipjar  

Agent  --> Document   :openid  

```