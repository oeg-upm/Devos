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



Person  --> Document   :workInfoHomepage  

Agent  --> Thing   :topic_interest  

Person  --> Document   :publications  

Agent  --> Document   :weblog  

Person  --> Thing   :pastProject  

Thing  --> Document   :page  

Agent  --> Document   :openid  

Thing  --> Document   :homepage  

Person  --> Thing   :currentProject  

Person  --> Document   :schoolHomepage  

Person  --> Document   :workplaceHomepage  

Document  --> Thing   :primaryTopic  

Agent  --> Document   :tipjar  

Agent  --> Document   :interest  

Agent  --> Thing   :made  

Agent  --> Thing   :mbox  

Thing  --> Agent   :maker  

Person  --> Person   :knows  

Document  --> Thing   :topic  

```