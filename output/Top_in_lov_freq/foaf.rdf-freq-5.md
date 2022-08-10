```mermaid
	classDiagram

    
    class Thing {
    
    }

    class Document {
    
    }

    class Image {
    
    }

    class Agent {
    
    }

    class OnlineAccount {
    
    }



Thing  --> Thing   :fundedBy  

OnlineAccount  --> Document   :accountServiceHomepage  

Image  --> Thing   :depicts  

Agent  --> OnlineAccount   :holdsAccount  

Person  --> Document   :workInfoHomepage  

Thing  --> Thing   :logo  

Document  --> Thing   :topic  

Document  --> Thing   :primaryTopic  

Agent  --> Thing   :mbox  

Person  --> Document   :publications  

Thing  --> Document   :page  

Agent  --> Thing   :topic_interest  

Person  --> Thing   :currentProject  

Thing  --> Agent   :maker  

Thing  --> Document   :homepage  

Image  --> Image   :thumbnail  

SKOSConcept  --> Thing   :focus  

Agent  --> Thing   :made  

Person  --> Document   :workplaceHomepage  

Person  --> Thing   :pastProject  

Thing  --> Thing   :theme  

Agent  --> Document   :weblog  

Agent  --> Document   :tipjar  

Person  --> Image   :img  

Person  --> Document   :schoolHomepage  

Agent  --> Document   :interest  

Agent  --> OnlineAccount   :account  

Group  --> Agent   :member  

Agent  --> Document   :openid  

Thing  --> Image   :depiction  

```