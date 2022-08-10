```mermaid
	classDiagram

    
    class Person {
    
    }

    class PopulatedPlace {
    
    }

    class Place {
    
    }

    class SportsTeam {
    
    }

    class Award {
    
    }



Work  --> Person   :translator  

EducationalInstitution  --> Person   :rector  

Person  --> Tournament   :olympicGames  

Person  --> Organisation   :federation  

SportsTeam  --> Person   :currentMember  

Family  --> Person   :headOfFamily  

Animal  --> Place   :deathPlace  

Island  --> PopulatedPlace   :lowestState  

Person  --> SKOSConcept   :usopenWins  

Person  --> CareerStation   :careerStation  

SportsEvent  --> Person   :bronzeMedalist  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

WrittenWork  --> Person   :prefaceBy  

Person  --> Organisation   :employer  

Mountain  --> Person   :firstAscentPerson  

MilitaryUnit  --> PopulatedPlace   :garrison  

MilitaryUnit  --> Person   :fourthCommander  

Olympics  --> Person   :olympicOathSwornByJudge  

Place  --> Place   :northWestPlace  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueRelegated  

River  --> PopulatedPlace   :mouthRegion  

Artist  --> Award   :academyAward  

Artist  --> Award   :grammyAward  

PopulatedPlace  --> PopulatedPlace   :sheading  

FigureSkater  --> Person   :formerChoreographer  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Person  --> Contest   :contest  

Place  --> PopulatedPlace   :sovereignCountry  

Newspaper  --> Person   :associateEditor  

Athlete  --> SportsTeam   :teamCoached  

PopulatedPlace  --> Language   :regionalLanguage  

TelevisionShow  --> Person   :showJudge  

Person  --> Sport   :sportDiscipline  

Person  --> Person   :relation  

Politician  --> Person   :prefect  

Person  --> SKOSConcept   :startReign  

Actor  --> Award   :laurenceOlivierAward  

Person  --> Person   :cousurper  

SportsTeam  --> Person   :manager  

EducationalInstitution  --> Person   :alumni  

Place  --> Depth   :depths  

Film  --> Person   :makeupArtist  

Person  --> List   :relatedFunctions  

PopulatedPlace  --> Legislature   :legislature  

Olympics  --> Person   :torchBearer  

Island  --> PopulatedPlace   :managementRegion  

Scientist  --> Person   :doctoralStudent  

PopulatedPlace  --> Person   :viceLeader  

Athlete  --> SportsTeam   :coachClub  

GrandPrix  --> SportsTeam   :secondTeam  

FigureSkater  --> Person   :choreographer  

Scientist  --> Person   :doctoralAdvisor  

Person  --> Diploma   :diploma  

Person  --> Person   :opponent  

Athlete  --> SportsTeam   :ncaaTeam  

Athlete  --> SportsTeam   :formerTeam  

Place  --> Place   :northPlace  

Actor  --> Award   :goldenRaspberryAward  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductPurchasingPowerParityPerCapita  

Comedian  --> Award   :britishComedyAwards  

PopulatedPlace  --> PopulatedPlace   :principalArea  

SoccerClub  --> Person   :clubsRecordGoalscorer  

Olympics  --> Person   :officialOpenedBy  

PopulatedPlace  --> PoliticalParty   :viceLeaderParty  

Film  --> Person   :setDesigner  

MusicalWork  --> PopulatedPlace   :recordedIn  

School  --> Person   :vicePrincipal  

Man  --> Person   :son  

Person  --> RadioStation   :radio  

Sport  --> Person   :footedness  

Race  --> Person   :recentWinner  

Organisation  --> Person   :secretaryGeneral  

Person  --> Country   :stateOfOrigin  

Athlete  --> SportsTeam   :debutTeam  

GrandPrix  --> Person   :firstDriver  

PopulatedPlace  --> Area   :agglomerationArea  

Actor  --> Award   :iftaAward  

Olympics  --> Person   :olympicOathSwornBy  

Person  --> Place   :announcedFrom  

SoccerClub  --> Place   :ground  

Place  --> Mountain   :lowestMountain  

Saint  --> Person   :beatifiedBy  

Band  --> Person   :bandMember  

Settlement  --> Place   :highestPoint  

Person  --> Person   :sibling  

Person  --> SKOSConcept   :endReign  

Place  --> Place   :southEastPlace  

Place  --> Organisation   :governingBody  

SkiResort  --> Place   :massif  

LegalCase  --> Person   :attorneyGeneral  

EducationalInstitution  --> Person   :custodian  

Place  --> Place   :hasInsidePlace  

Person  --> Person   :child  

Settlement  --> Place   :settlementAttached  

SportsEvent  --> Person   :medalist  

Restaurant  --> Person   :headChef  

Magazine  --> Person   :previousEditor  

Person  --> Work   :created  

Animal  --> Place   :birthPlace  

Person  --> SKOSConcept   :britishWins  

TelevisionShow  --> Person   :coExecutiveProducer  

Settlement  --> Place   :daira  

Place  --> PopulatedPlace   :nearestCity  

Settlement  --> PopulatedPlace   :geolocDepartment  

Place  --> Place   :land  

PopulatedPlace  --> City   :capital  

River  --> PopulatedPlace   :mouthState  

Organisation  --> Person   :administrator  

Place  --> PersonFunction   :politicalLeader  

Artist  --> Award   :tonyAward  

Film  --> Person   :editing  

Person  --> SportsTeam   :teamManager  

Person  --> Work   :debutWork  

VideoGame  --> Person   :gameArtist  

GrandPrix  --> Person   :secondDriver  

School  --> Person   :executiveHeadteacher  

Person  --> Place   :livingPlace  

Work  --> Person   :coverArtist  

Person  --> Tournament   :worldTournament  

TelevisionShow  --> Person   :creativeDirector  

Place  --> Sea   :sea  

Person  --> Country   :nationality  

River  --> PopulatedPlace   :mouthDistrict  

Place  --> PopulatedPlace   :regency  

Actor  --> Award   :goldenCalfAward  

Woman  --> Person   :sister  

Actor  --> Award   :geminiAward  

PopulatedPlace  --> Department   :department  

Saint  --> PopulatedPlace   :beatifiedPlace  

Place  --> Place   :endPoint  

Person  --> Person   :spouse  

PopulatedPlace  --> Population   :population  

Organisation  --> Person   :trustee  

Canal  --> Person   :principalEngineer  

Actor  --> Award   :screenActorsGuildAward  

Broadcaster  --> PopulatedPlace   :broadcastArea  

Person  --> Place   :bodyDiscovered  

Place  --> Province   :provinceLink  

Organisation  --> PopulatedPlace   :headquarter  

Settlement  --> Place   :wilaya  

Place  --> Place   :westPlace  

Canal  --> Place   :originalEndPoint  

Place  --> SpatialThing   :lowestPosition  

Place  --> Place   :northEastPlace  

PopulatedPlace  --> Agglomeration   :agglomeration  

Person  --> Person   :student  

Film  --> Person   :director  

PopulatedPlace  --> Demographics   :agglomerationDemographics  

Settlement  --> PopulatedPlace   :frazioni  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

Person  --> EducationalInstitution   :almaMater  

Island  --> PopulatedPlace   :governmentRegion  

Person  --> Tournament   :nationalTournament  

RouteOfTransportation  --> Place   :routeStartLocation  

FigureSkater  --> Person   :currentPartner  

Artist  --> Award   :gaudiAward  

Person  --> PersonFunction   :otherOccupation  

Settlement  --> Place   :lowestPoint  

Artist  --> Award   :afiAward  

Place  --> Place   :hasOutsidePlace  

Work  --> Person   :chiefEditor  

Monarch  --> Person   :heir  

Artist  --> Award   :cesarAward  

Person  --> Person   :friend  

Ship  --> Place   :homeport  

PopulatedPlace  --> EthnicGroup   :ethnicGroup  

University  --> Person   :officerInCharge  

Athlete  --> SportsTeam   :youthClub  

Organisation  --> Person   :chaplain  

Family  --> Person   :lastFamilyMember  

Place  --> Province   :province  

Place  --> Place   :supply  

Man  --> Person   :father  

Person  --> Person   :dubber  

Work  --> Person   :mainCharacter  

Department  --> PopulatedPlace   :subprefecture  

Artwork  --> Person   :painter  

PopulatedPlace  --> Saint   :saint  

Person  --> EducationalInstitution   :college  

Person  --> SKOSConcept   :world  

Person  --> MilitaryService   :militaryService  

LegalCase  --> Person   :solicitorGeneral  

Person  --> Person   :collaboration  

PoliticalParty  --> Person   :spokesperson  

Island  --> Place   :subdivisionName  

Place  --> PopulatedPlace   :district  

Island  --> PopulatedPlace   :lowestRegion  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Place  --> Place   :mainIsland  

Organisation  --> Person   :chairperson  

Place  --> Place   :nextEntity  

Work  --> Person   :writer  

Person  --> Person   :detractor  

Person  --> Person   :parent  

Comedian  --> Award   :olivierAward  

Canal  --> Place   :originalStartPoint  

Language  --> PopulatedPlace   :spokenIn  

Place  --> PopulatedPlace   :biggestCity  

Work  --> Person   :composer  

AdministrativeRegion  --> Person   :landeshauptmann  

School  --> Person   :headteacher  

Place  --> Altitude   :altitude  

EducationalInstitution  --> Person   :principal  

GrandPrix  --> Person   :fastestDriver  

Settlement  --> PopulatedPlace   :federalState  

Person  --> Person   :copilote  

Family  --> Person   :primogenitor  

MilitaryUnit  --> Person   :notableCommander  

Actor  --> Award   :naacpImageAward  

RouteOfTransportation  --> Place   :routeEndLocation  

PopulatedPlace  --> Language   :officialLanguage  

Athlete  --> SportsTeam   :oldTeamCoached  

River  --> PopulatedPlace   :sourceConfluenceState  

Film  --> Person   :specialEffects  

Person  --> Film   :movie  

Person  --> Person   :relative  

PopulatedPlace  --> Population   :previousPopulation  

Place  --> Place   :locatedInArea  

Athlete  --> Person   :trainer  

FigureSkater  --> Person   :formerCoach  

MusicalWork  --> Person   :lyrics  

Road  --> PopulatedPlace   :ruralMunicipality  

Person  --> Person   :seiyu  

Organisation  --> Place   :regionServed  

Work  --> Person   :author  

TelevisionEpisode  --> Person   :guest  

Artist  --> Award   :emmyAward  

Athlete  --> SportsTeam   :stateOfOriginTeam  

Place  --> Altitude   :lowestAltitude  

Athlete  --> SportsTeam   :managerClub  

Person  --> SportsLeague   :leagueManager  

SoccerPlayer  --> SportsTeam   :trainerClub  

Person  --> Place   :educationPlace  

Band  --> Person   :formerBandMember  

Musical  --> Person   :musicBy  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

AdministrativeRegion  --> Place   :administrativeCenter  

Person  --> Place   :residence  

Person  --> EthnicGroup   :ethnicity  

Athlete  --> SportsTeam   :currentTeam  

Man  --> Person   :uncle  

Place  --> River   :river  

Person  --> Person   :colleague  

Athlete  --> SportsTeam   :juniorTeam  

Place  --> RouteStop   :isRouteStop  

Place  --> Species   :bird  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueWinner  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductNominalPerCapita  

Person  --> Project   :project  

Island  --> PopulatedPlace   :highestRegion  

Artist  --> Award   :filmFareAward  

EducationalInstitution  --> Person   :dean  

SportsTeam  --> TeamMember   :currentTeamMember  

Film  --> Person   :cinematography  

Place  --> Place   :previousEntity  

GrandPrix  --> SportsTeam   :fastestDriverTeam  

PopulatedPlace  --> Person   :leaderName  

Person  --> SportsTeam   :currentTeamManager  

Athlete  --> SportsTeam   :nflTeam  

Athlete,_CareerStation  --> SportsTeam   :leadTeam  

Artist  --> Award   :goldenGlobeAward  

Athlete  --> SportsTeam   :club  

Scientist  --> Person   :notableStudent  

Place  --> Place   :closeTo  

Person  --> Tournament   :continentalTournament  

MilitaryUnit  --> Person   :secondCommander  

Island  --> PopulatedPlace   :capitalRegion  

Island  --> PopulatedPlace   :capitalPlace  

Person  --> Person   :usurper  

PopulatedPlace  --> PopulatedPlace   :borough  

EducationalInstitution  --> Person   :actingHeadteacher  

Place  --> PopulatedPlace   :lowestPlace  

Place  --> Place   :subregion  

Organisation  --> Person   :superintendent  

Person  --> SportsEvent   :competitionTitle  

Place  --> Place   :eastPlace  

PopulatedPlace  --> Demographics   :previousDemographics  

Settlement  --> PopulatedPlace   :jointCommunity  

Food  --> Person   :creatorOfDish  

PopulatedPlace  --> Place   :touristicSite  

HistoricBuilding  --> Person   :pastor  

TermOfOffice  --> Person   :presidentGeneralCouncil  

WrittenWork  --> Person   :illustrator  

Race  --> Person   :firstWinner  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

River  --> Place   :sourceConfluenceRegion  

Person  --> SpatialThing   :restingPlacePosition  

Actor  --> Award   :nationalFilmAward  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Saint  --> Person   :canonizedBy  

Newspaper  --> Person   :managingEditor  

SportsTeam  --> Person   :generalManager  

Actor  --> Award   :arielAward  

Saint  --> PopulatedPlace   :canonizedPlace  

Album  --> Person   :compiler  

TelevisionShow  --> Person   :storyEditor  

Organisation  --> Person   :ceo  

Place  --> Area   :wholeArea  

Athlete,_CareerStation  --> SportsTeam   :amateurTeam  

Island  --> PopulatedPlace   :capitalDistrict  

TelevisionShow  --> Person   :presenter  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Restaurant  --> Person   :chef  

Woman  --> Person   :mother  

Place  --> Species   :tree  

Person  --> SKOSConcept   :mastersWins  

Athlete,_CareerStation  --> SportsTeam   :proTeam  

Man  --> Person   :brother  

Island  --> PopulatedPlace   :governmentPlace  

Settlement  --> Person   :bourgmestre  

Place  --> Place   :southWestPlace  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

School  --> Person   :nobelLaureates  

Woman  --> Person   :daughter  

Settlement  --> PopulatedPlace   :largestMetro  

Place  --> Species   :flower  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

GrandPrix  --> Person   :thirdDriver  

Scientist  --> Person   :academicAdvisor  

Work  --> Place   :releaseLocation  

SiteOfSpecialScientificInterest  --> PopulatedPlace   :areaOfSearch  

```