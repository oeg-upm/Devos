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



Person  --> Person   :knows  

Person  --> Document   :schoolHomepage  

Person  --> Thing   :pastProject  

Person  --> Image   :img  

Document  --> Thing   :primaryTopic  

Image  --> Image   :thumbnail  

Agent  --> Document   :weblog  

Person  --> Document   :workInfoHomepage  

Agent  --> Thing   :mbox  

Thing  --> Document   :homepage  

Agent  --> Thing   :made  

Person  --> Document   :workplaceHomepage  

Agent  --> Document   :interest  

Person  --> Thing   :currentProject  

Thing  --> Agent   :maker  

Thing  --> Image   :depiction  

Agent  --> Thing   :topic_interest  

Document  --> Thing   :topic  

Person  --> Document   :publications  

Thing  --> Document   :page  

Image  --> Thing   :depicts  

Agent  --> Document   :tipjar  

Agent  --> Document   :openid  

```