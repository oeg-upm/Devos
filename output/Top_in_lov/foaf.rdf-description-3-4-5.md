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

    class Image {
    
    }



Document  --> Thing   :topic  

Document  --> Thing   :primaryTopic  

Agent  --> Thing   :mbox  

Thing  --> Agent   :maker  

Agent  --> Thing   :made  

Person  --> Image   :img  

Person  --> Document   :publications  

Agent  --> Document   :openid  

Thing  --> Document   :homepage  

Thing  --> Image   :depiction  

Thing  --> Document   :page  

Agent  --> Document   :tipjar  

Person  --> Thing   :pastProject  

Image  --> Image   :thumbnail  

Person  --> Person   :knows  

Agent  --> Document   :interest  

Person  --> Document   :schoolHomepage  

Person  --> Document   :workplaceHomepage  

Image  --> Thing   :depicts  

Person  --> Thing   :currentProject  

Person  --> Document   :workInfoHomepage  

Agent  --> Document   :weblog  

Agent  --> Thing   :topic_interest  

```