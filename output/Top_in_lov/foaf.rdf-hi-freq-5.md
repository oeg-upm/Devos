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



Person  --> Document   :workInfoHomepage  

Person  --> Image   :img  

Agent  --> Thing   :topic_interest  

Person  --> Document   :publications  

Agent  --> Document   :weblog  

Person  --> Thing   :pastProject  

Thing  --> Document   :page  

Image  --> Image   :thumbnail  

Agent  --> Document   :openid  

Thing  --> Image   :depiction  

Thing  --> Document   :homepage  

Image  --> Thing   :depicts  

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