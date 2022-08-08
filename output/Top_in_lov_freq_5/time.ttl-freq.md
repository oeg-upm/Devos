```mermaid
	classDiagram

    
    class ProperInterval {
    
    }

    class TemporalEntity {
    
    }

    class Instant {
    
    }

    class GeneralDateTimeDescription {
    
    }

    class DayOfWeek {
    
    }



ProperInterval  --> ProperInterval   :intervalOverlappedBy  

ProperInterval  --> ProperInterval   :intervalStarts  

TemporalEntity  --> TemporalEntity   :after  

GeneralDateTimeDescription  --> MonthOfYear   :monthOfYear  

DateTimeInterval  --> GeneralDateTimeDescription   :hasDateTimeDescription  

ProperInterval  --> ProperInterval   :intervalDuring  

Instant  --> GeneralDateTimeDescription   :inDateTime  

ProperInterval  --> ProperInterval   :intervalStartedBy  

ProperInterval  --> ProperInterval   :intervalFinishes  

ProperInterval  --> ProperInterval   :intervalIn  

TemporalEntity  --> Instant   :hasBeginning  

ProperInterval  --> ProperInterval   :intervalBefore  

ProperInterval  --> ProperInterval   :intervalFinishedBy  

ProperInterval  --> ProperInterval   :intervalAfter  

ProperInterval  --> ProperInterval   :intervalOverlaps  

Interval  --> Instant   :inside  

Instant  --> TemporalPosition   :inTemporalPosition  

ProperInterval  --> ProperInterval   :intervalEquals  

TemporalEntity  --> Instant   :hasEnd  

GeneralDateTimeDescription  --> TimeZone   :timeZone  

TemporalEntity  --> TemporalDuration   :hasTemporalDuration  

ProperInterval  --> ProperInterval   :intervalMetBy  

GeneralDateTimeDescription  --> DayOfWeek   :dayOfWeek  

Instant  --> TimePosition   :inTimePosition  

TemporalEntity  --> TemporalEntity   :before  

ProperInterval  --> ProperInterval   :intervalMeets  

ProperInterval  --> ProperInterval   :intervalDisjoint  

ProperInterval  --> ProperInterval   :intervalContains  

```