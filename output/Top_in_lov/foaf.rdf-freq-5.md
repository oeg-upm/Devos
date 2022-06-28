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

Thing  --> Agent   :maker  

Thing  --> Document   :homepage  

Thing  --> Document   :page  

Agent  --> Thing   :mbox  

Agent  --> Document   :interest  

Person  --> Document   :workInfoHomepage  

Agent  --> Document   :weblog  

Agent  --> Document   :tipjar  

Person  --> Document   :publications  

Person  --> Thing   :currentProject  

Person  --> Thing   :pastProject  

Document  --> Thing   :primaryTopic  

Person  --> Document   :workplaceHomepage  

Image  --> Thing   :depicts  

Person  --> Person   :knows  

Person  --> Document   :schoolHomepage  

Agent  --> Thing   :topic_interest  

Thing  --> Image   :depiction  

Image  --> Image   :thumbnail  

Agent  --> Thing   :made  

Agent  --> Document   :openid  

Person  --> Image   :img  

```