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



Image  --> Image   :thumbnail  

Group  --> Agent   :member  

Thing  --> Thing   :fundedBy  

Image  --> Thing   :depicts  

Document  --> Thing   :topic  

Thing  --> Thing   :logo  

Person  --> Document   :workInfoHomepage  

Agent  --> Document   :interest  

Agent  --> Thing   :mbox  

Agent  --> Document   :tipjar  

Thing  --> Document   :page  

Thing  --> Document   :homepage  

Thing  --> Agent   :maker  

Person  --> Thing   :currentProject  

Person  --> Document   :workplaceHomepage  

Person  --> Document   :schoolHomepage  

Agent  --> Document   :openid  

Thing  --> Image   :depiction  

Person  --> Document   :publications  

SKOSConcept  --> Thing   :focus  

Thing  --> Thing   :theme  

Agent  --> Thing   :made  

Agent  --> OnlineAccount   :account  

Agent  --> Document   :weblog  

Person  --> Thing   :pastProject  

OnlineAccount  --> Document   :accountServiceHomepage  

Person  --> Image   :img  

Agent  --> OnlineAccount   :holdsAccount  

Agent  --> Thing   :topic_interest  

Document  --> Thing   :primaryTopic  

```