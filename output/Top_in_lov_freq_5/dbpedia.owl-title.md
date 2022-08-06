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



Woman  --> Person   :daughter  

Place  --> Altitude   :lowestAltitude  

SkiResort  --> Place   :massif  

Ship  --> Place   :homeport  

Work  --> Person   :composer  

Island  --> PopulatedPlace   :capitalRegion  

Settlement  --> PopulatedPlace   :administrativeDistrict  

University  --> Person   :officerInCharge  

GrandPrix  --> Person   :thirdDriver  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

TelevisionEpisode  --> Person   :guest  

PopulatedPlace  --> PopulatedPlace   :borough  

Family  --> Person   :lastFamilyMember  

Person  --> Person   :student  

Island  --> PopulatedPlace   :capitalPlace  

Place  --> Species   :tree  

Band  --> Person   :formerBandMember  

Person  --> Person   :copilote  

WrittenWork  --> Person   :prefaceBy  

Place  --> Place   :land  

Person  --> Tournament   :olympicGames  

Person  --> SportsLeague   :leagueManager  

Comedian  --> Award   :britishComedyAwards  

Food  --> Person   :creatorOfDish  

Restaurant  --> Person   :chef  

PopulatedPlace  --> Saint   :saint  

Organisation  --> Person   :chairperson  

Island  --> PopulatedPlace   :managementRegion  

Band  --> Person   :bandMember  

Person  --> Person   :usurper  

River  --> PopulatedPlace   :mouthState  

Organisation  --> Person   :secretaryGeneral  

Artist  --> Award   :tonyAward  

SoccerClub  --> Person   :clubsRecordGoalscorer  

Film  --> Person   :makeupArtist  

Person  --> Film   :movie  

Animal  --> Place   :deathPlace  

Place  --> PopulatedPlace   :district  

GrandPrix  --> Person   :firstDriver  

Sport  --> Person   :footedness  

Settlement  --> Place   :daira  

Person  --> SpatialThing   :restingPlacePosition  

Athlete  --> SportsTeam   :stateOfOriginTeam  

MilitaryUnit  --> Person   :notableCommander  

Person  --> Place   :announcedFrom  

PopulatedPlace  --> Population   :population  

Canal  --> Place   :originalEndPoint  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Actor  --> Award   :goldenRaspberryAward  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

EducationalInstitution  --> Person   :custodian  

EducationalInstitution  --> Person   :dean  

Work  --> Person   :writer  

Actor  --> Award   :screenActorsGuildAward  

Person  --> Person   :friend  

Artwork  --> Person   :painter  

Settlement  --> PopulatedPlace   :largestMetro  

Scientist  --> Person   :notableStudent  

Place  --> PopulatedPlace   :lowestPlace  

Artist  --> Award   :emmyAward  

Settlement  --> Place   :highestPoint  

Musical  --> Person   :musicBy  

Athlete  --> SportsTeam   :coachClub  

Person  --> SKOSConcept   :usopenWins  

PopulatedPlace  --> Demographics   :agglomerationDemographics  

SportsTeam  --> Person   :manager  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductNominalPerCapita  

TelevisionShow  --> Person   :creativeDirector  

Athlete  --> SportsTeam   :teamCoached  

Actor  --> Award   :iftaAward  

Place  --> PopulatedPlace   :regency  

Monarch  --> Person   :heir  

Place  --> Place   :eastPlace  

Athlete,_CareerStation  --> SportsTeam   :proTeam  

River  --> Place   :sourceConfluenceRegion  

Film  --> Person   :editing  

EducationalInstitution  --> Person   :rector  

Olympics  --> Person   :officialOpenedBy  

Place  --> Mountain   :lowestMountain  

Broadcaster  --> PopulatedPlace   :broadcastArea  

SportsEvent  --> Person   :bronzeMedalist  

Place  --> PopulatedPlace   :sovereignCountry  

Person  --> EducationalInstitution   :almaMater  

School  --> Person   :vicePrincipal  

PopulatedPlace  --> Language   :regionalLanguage  

PopulatedPlace  --> Agglomeration   :agglomeration  

Place  --> Place   :endPoint  

Person  --> Person   :opponent  

Person  --> RadioStation   :radio  

MilitaryUnit  --> PopulatedPlace   :garrison  

Language  --> PopulatedPlace   :spokenIn  

Olympics  --> Person   :olympicOathSwornBy  

Athlete,_CareerStation  --> SportsTeam   :leadTeam  

Woman  --> Person   :mother  

PopulatedPlace  --> Language   :officialLanguage  

Place  --> Place   :northWestPlace  

Person  --> Sport   :sportDiscipline  

Person  --> Person   :sibling  

Animal  --> Place   :birthPlace  

Man  --> Person   :brother  

Place  --> Place   :northPlace  

Place  --> Area   :wholeArea  

GrandPrix  --> Person   :fastestDriver  

Film  --> Person   :cinematography  

Saint  --> PopulatedPlace   :canonizedPlace  

Person  --> Person   :collaboration  

TermOfOffice  --> Person   :presidentGeneralCouncil  

Person  --> Person   :detractor  

Person  --> SKOSConcept   :startReign  

Politician  --> Person   :prefect  

PopulatedPlace  --> Person   :viceLeader  

PopulatedPlace  --> Person   :leaderName  

PopulatedPlace  --> PopulatedPlace   :sheading  

Place  --> Place   :southWestPlace  

Newspaper  --> Person   :managingEditor  

Place  --> PopulatedPlace   :biggestCity  

Settlement  --> PopulatedPlace   :geolocDepartment  

Artist  --> Award   :filmFareAward  

TelevisionShow  --> Person   :storyEditor  

SiteOfSpecialScientificInterest  --> PopulatedPlace   :areaOfSearch  

Family  --> Person   :primogenitor  

Person  --> Work   :created  

Person  --> Person   :colleague  

Place  --> Place   :subregion  

Place  --> Depth   :depths  

Person  --> MilitaryService   :militaryService  

MusicalWork  --> Person   :lyrics  

Magazine  --> Person   :previousEditor  

Place  --> Place   :closeTo  

Person  --> CareerStation   :careerStation  

Place  --> PersonFunction   :politicalLeader  

FigureSkater  --> Person   :formerChoreographer  

Island  --> Place   :subdivisionName  

Actor  --> Award   :naacpImageAward  

Film  --> Person   :director  

Place  --> Altitude   :altitude  

Athlete  --> SportsTeam   :ncaaTeam  

Restaurant  --> Person   :headChef  

Athlete  --> SportsTeam   :currentTeam  

Person  --> Person   :spouse  

Person  --> Person   :parent  

Settlement  --> Place   :wilaya  

GrandPrix  --> Person   :secondDriver  

PopulatedPlace  --> PopulatedPlace   :largestCity  

RouteOfTransportation  --> Place   :routeStartLocation  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueWinner  

Person  --> Organisation   :employer  

Organisation  --> PopulatedPlace   :headquarter  

Person  --> Organisation   :federation  

Place  --> Place   :hasInsidePlace  

FigureSkater  --> Person   :formerCoach  

Settlement  --> PopulatedPlace   :jointCommunity  

Place  --> Place   :southEastPlace  

Man  --> Person   :son  

Athlete  --> SportsTeam   :managerClub  

Place  --> PopulatedPlace   :nearestCity  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

River  --> PopulatedPlace   :sourceConfluenceState  

Comedian  --> Award   :olivierAward  

SoccerPlayer  --> SportsTeam   :trainerClub  

Race  --> Person   :firstWinner  

Place  --> Place   :westPlace  

Place  --> Place   :nextEntity  

Place  --> Province   :provinceLink  

MilitaryUnit  --> Person   :secondCommander  

Person  --> Project   :project  

Organisation  --> Person   :administrator  

Scientist  --> Person   :doctoralStudent  

Artist  --> Award   :goldenGlobeAward  

Place  --> SpatialThing   :lowestPosition  

AdministrativeRegion  --> Place   :administrativeCenter  

PopulatedPlace  --> City   :capital  

Athlete  --> SportsTeam   :formerTeam  

LegalCase  --> Person   :attorneyGeneral  

Place  --> Place   :previousEntity  

SportsTeam  --> Person   :generalManager  

Organisation  --> Person   :superintendent  

Newspaper  --> Person   :associateEditor  

Scientist  --> Person   :doctoralAdvisor  

Woman  --> Person   :sister  

Island  --> PopulatedPlace   :capitalDistrict  

Place  --> Organisation   :governingBody  

TelevisionShow  --> Person   :presenter  

Athlete  --> SportsTeam   :juniorTeam  

Artist  --> Award   :academyAward  

Person  --> Person   :dubber  

PopulatedPlace  --> PoliticalParty   :viceLeaderParty  

Mountain  --> Person   :firstAscentPerson  

RouteOfTransportation  --> Place   :routeEndLocation  

River  --> PopulatedPlace   :mouthRegion  

Canal  --> Person   :principalEngineer  

Scientist  --> Person   :academicAdvisor  

Settlement  --> PopulatedPlace   :federalState  

Artist  --> Award   :grammyAward  

SoccerClub  --> Place   :ground  

VideoGame  --> Person   :gameArtist  

PopulatedPlace  --> Population   :previousPopulation  

PopulatedPlace  --> EthnicGroup   :ethnicGroup  

Organisation  --> Place   :regionServed  

EducationalInstitution  --> Person   :actingHeadteacher  

Person  --> Country   :stateOfOrigin  

Person  --> SportsEvent   :competitionTitle  

Island  --> PopulatedPlace   :lowestState  

School  --> Person   :headteacher  

Island  --> PopulatedPlace   :highestRegion  

Person  --> Tournament   :continentalTournament  

Place  --> Place   :mainIsland  

Place  --> Province   :province  

Place  --> Sea   :sea  

School  --> Person   :executiveHeadteacher  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductPurchasingPowerParityPerCapita  

SportsEvent  --> Person   :medalist  

Place  --> River   :river  

Athlete  --> SportsTeam   :oldTeamCoached  

Man  --> Person   :father  

Actor  --> Award   :nationalFilmAward  

Work  --> Person   :chiefEditor  

Organisation  --> Person   :ceo  

School  --> Person   :nobelLaureates  

Work  --> Place   :releaseLocation  

PopulatedPlace  --> Department   :department  

Olympics  --> Person   :olympicOathSwornByJudge  

Canal  --> Place   :originalStartPoint  

Person  --> Person   :relative  

Person  --> Country   :nationality  

Person  --> SKOSConcept   :world  

Actor  --> Award   :laurenceOlivierAward  

PoliticalParty  --> Person   :spokesperson  

Person  --> Place   :bodyDiscovered  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Work  --> Person   :translator  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Person  --> Tournament   :worldTournament  

AdministrativeRegion  --> Person   :landeshauptmann  

Athlete,_CareerStation  --> SportsTeam   :amateurTeam  

Person  --> Person   :relation  

Person  --> PersonFunction   :otherOccupation  

EducationalInstitution  --> Person   :principal  

Person  --> Tournament   :nationalTournament  

Person  --> Work   :debutWork  

Place  --> RouteStop   :isRouteStop  

Athlete  --> SportsTeam   :youthClub  

Artist  --> Award   :cesarAward  

PopulatedPlace  --> Place   :touristicSite  

PopulatedPlace  --> Legislature   :legislature  

Person  --> SportsTeam   :currentTeamManager  

Saint  --> Person   :canonizedBy  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Person  --> Person   :child  

TelevisionShow  --> Person   :coExecutiveProducer  

Artist  --> Award   :afiAward  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

Actor  --> Award   :goldenCalfAward  

Artist  --> Award   :gaudiAward  

Person  --> SportsTeam   :teamManager  

TelevisionShow  --> Person   :showJudge  

Person  --> Place   :livingPlace  

Place  --> Species   :flower  

Saint  --> Person   :beatifiedBy  

Person  --> Contest   :contest  

Person  --> SKOSConcept   :endReign  

Person  --> EducationalInstitution   :college  

Man  --> Person   :uncle  

Film  --> Person   :setDesigner  

HistoricBuilding  --> Person   :pastor  

FigureSkater  --> Person   :currentPartner  

Athlete  --> SportsTeam   :club  

SportsTeam  --> TeamMember   :currentTeamMember  

Settlement  --> Place   :settlementAttached  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueRelegated  

Work  --> Person   :mainCharacter  

Organisation  --> Person   :trustee  

Island  --> PopulatedPlace   :lowestRegion  

Island  --> PopulatedPlace   :governmentPlace  

Person  --> List   :relatedFunctions  

Athlete  --> SportsTeam   :nflTeam  

Race  --> Person   :recentWinner  

FigureSkater  --> Person   :choreographer  

Work  --> Person   :coverArtist  

Actor  --> Award   :geminiAward  

Film  --> Person   :specialEffects  

River  --> PopulatedPlace   :mouthDistrict  

Person  --> EthnicGroup   :ethnicity  

MilitaryUnit  --> Person   :fourthCommander  

Album  --> Person   :compiler  

Settlement  --> Person   :bourgmestre  

Family  --> Person   :headOfFamily  

PopulatedPlace  --> PopulatedPlace   :principalArea  

EducationalInstitution  --> Person   :alumni  

Person  --> Place   :educationPlace  

MusicalWork  --> PopulatedPlace   :recordedIn  

Athlete  --> SportsTeam   :debutTeam  

Settlement  --> PopulatedPlace   :frazioni  

GrandPrix  --> SportsTeam   :fastestDriverTeam  

PopulatedPlace  --> Area   :agglomerationArea  

Place  --> Species   :bird  

Organisation  --> Person   :chaplain  

GrandPrix  --> SportsTeam   :secondTeam  

Place  --> Place   :locatedInArea  

Place  --> Place   :supply  

Person  --> Person   :cousurper  

Road  --> PopulatedPlace   :ruralMunicipality  

Olympics  --> Person   :torchBearer  

WrittenWork  --> Person   :illustrator  

Athlete  --> Person   :trainer  

LegalCase  --> Person   :solicitorGeneral  

Person  --> Person   :seiyu  

SportsTeam  --> Person   :currentMember  

Department  --> PopulatedPlace   :subprefecture  

Person  --> SKOSConcept   :britishWins  

Place  --> Place   :northEastPlace  

Person  --> Diploma   :diploma  

Place  --> Place   :hasOutsidePlace  

Work  --> Person   :author  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

Actor  --> Award   :arielAward  

Person  --> SKOSConcept   :mastersWins  

Settlement  --> Place   :lowestPoint  

PopulatedPlace  --> Demographics   :previousDemographics  

Person  --> Place   :residence  

Island  --> PopulatedPlace   :governmentRegion  

Saint  --> PopulatedPlace   :beatifiedPlace  

```