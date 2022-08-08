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



Place  --> River   :river  

Settlement  --> PopulatedPlace   :frazioni  

Person  --> SportsTeam   :currentTeamManager  

PopulatedPlace  --> PopulatedPlace   :ceremonialCounty  

Artist  --> Award   :cesarAward  

SportsTeam  --> Person   :manager  

Actor  --> Award   :naacpImageAward  

MusicalWork  --> Person   :lyrics  

TelevisionShow  --> Person   :storyEditor  

Person  --> Place   :bodyDiscovered  

PopulatedPlace  --> Population   :population  

EducationalInstitution  --> Person   :principal  

Person  --> Diploma   :diploma  

SportsEvent  --> Person   :medalist  

Island  --> PopulatedPlace   :capitalRegion  

PopulatedPlace  --> PopulatedPlace   :arrondissement  

Work  --> Person   :mainCharacter  

Person  --> Tournament   :olympicGames  

Person  --> Person   :spouse  

Work  --> Person   :author  

School  --> Person   :nobelLaureates  

River  --> Place   :sourceConfluenceRegion  

Athlete  --> SportsTeam   :ncaaTeam  

Newspaper  --> Person   :associateEditor  

Place  --> Organisation   :governingBody  

Saint  --> PopulatedPlace   :beatifiedPlace  

WrittenWork  --> Person   :prefaceBy  

Athlete  --> SportsTeam   :nflTeam  

Olympics  --> Person   :officialOpenedBy  

Place  --> Place   :previousEntity  

Organisation  --> Person   :secretaryGeneral  

Person  --> Person   :seiyu  

Person  --> Work   :debutWork  

River  --> PopulatedPlace   :mouthRegion  

Island  --> PopulatedPlace   :capitalDistrict  

Work  --> Person   :writer  

Athlete  --> SportsTeam   :juniorTeam  

Restaurant  --> Person   :chef  

MilitaryUnit  --> Person   :fourthCommander  

Athlete  --> SportsTeam   :managerClub  

EducationalInstitution  --> Person   :custodian  

SoccerPlayer  --> SportsTeam   :trainerClub  

Place  --> PopulatedPlace   :sovereignCountry  

GrandPrix  --> Person   :fastestDriver  

Island  --> PopulatedPlace   :capitalPlace  

Artist  --> Award   :grammyAward  

SportsTeam  --> TeamMember   :currentTeamMember  

SiteOfSpecialScientificInterest  --> PopulatedPlace   :areaOfSearch  

Person  --> Person   :relation  

Settlement  --> Place   :daira  

PopulatedPlace  --> EthnicGroup   :ethnicGroup  

EducationalInstitution  --> Person   :alumni  

Place  --> Place   :northWestPlace  

FigureSkater  --> Person   :choreographer  

Organisation  --> Person   :trustee  

Person  --> SKOSConcept   :britishWins  

GrandPrix  --> SportsTeam   :secondTeam  

Island  --> PopulatedPlace   :lowestState  

Place  --> Species   :bird  

Settlement  --> PopulatedPlace   :largestMetro  

Settlement  --> Place   :lowestPoint  

Comedian  --> Award   :olivierAward  

Person  --> Tournament   :worldTournament  

PopulatedPlace  --> PopulatedPlace   :borough  

Settlement  --> Person   :bourgmestre  

Road  --> PopulatedPlace   :ruralMunicipality  

PopulatedPlace  --> Population   :previousPopulation  

TelevisionShow  --> Person   :creativeDirector  

Place  --> Place   :closeTo  

Canal  --> Place   :originalStartPoint  

PopulatedPlace  --> Demographics   :agglomerationDemographics  

Person  --> Person   :cousurper  

Person  --> RadioStation   :radio  

GrandPrix  --> Person   :firstDriver  

Athlete  --> SportsTeam   :currentTeam  

Person  --> Person   :student  

Person  --> SKOSConcept   :startReign  

Film  --> Person   :cinematography  

Actor  --> Award   :goldenRaspberryAward  

Athlete  --> SportsTeam   :teamCoached  

Man  --> Person   :son  

Island  --> Place   :subdivisionName  

Person  --> List   :relatedFunctions  

Restaurant  --> Person   :headChef  

Athlete  --> SportsTeam   :formerTeam  

Person  --> Person   :relative  

School  --> Person   :executiveHeadteacher  

Place  --> Species   :tree  

PopulatedPlace  --> Language   :officialLanguage  

Person  --> Tournament   :continentalTournament  

Film  --> Person   :specialEffects  

MusicalWork  --> PopulatedPlace   :recordedIn  

Work  --> Person   :chiefEditor  

FigureSkater  --> Person   :formerCoach  

Place  --> Place   :northEastPlace  

RouteOfTransportation  --> Place   :routeStartLocation  

Olympics  --> Person   :olympicOathSwornBy  

Island  --> PopulatedPlace   :highestRegion  

Person  --> Place   :announcedFrom  

Actor  --> Award   :arielAward  

Person  --> SportsTeam   :teamManager  

PopulatedPlace  --> PopulatedPlace   :largestCity  

Settlement  --> PopulatedPlace   :associationOfLocalGovernment  

Place  --> PopulatedPlace   :district  

River  --> PopulatedPlace   :mouthDistrict  

Film  --> Person   :makeupArtist  

Place  --> Place   :southEastPlace  

Person  --> Tournament   :nationalTournament  

HistoricBuilding  --> Person   :pastor  

GrandPrix  --> Person   :secondDriver  

PopulatedPlace  --> Department   :department  

Person  --> SKOSConcept   :mastersWins  

SoccerClub  --> Person   :clubsRecordGoalscorer  

Person  --> Person   :detractor  

Place  --> Depth   :depths  

Monarch  --> Person   :heir  

Artist  --> Award   :goldenGlobeAward  

Person  --> Person   :collaboration  

Work  --> Person   :composer  

Island  --> PopulatedPlace   :governmentPlace  

Food  --> Person   :creatorOfDish  

Person  --> Country   :nationality  

Ship  --> Place   :homeport  

Canal  --> Place   :originalEndPoint  

PopulatedPlace  --> Place   :touristicSite  

Place  --> Place   :hasOutsidePlace  

Place  --> Sea   :sea  

Scientist  --> Person   :doctoralStudent  

GrandPrix  --> SportsTeam   :fastestDriverTeam  

Organisation  --> Person   :administrator  

FigureSkater  --> Person   :formerChoreographer  

Woman  --> Person   :mother  

Athlete,_CareerStation  --> SportsTeam   :amateurTeam  

Athlete,_CareerStation  --> SportsTeam   :leadTeam  

Place  --> Place   :northPlace  

School  --> Person   :vicePrincipal  

VideoGame  --> Person   :gameArtist  

Person  --> SKOSConcept   :world  

Saint  --> PopulatedPlace   :canonizedPlace  

Race  --> Person   :recentWinner  

PopulatedPlace  --> PopulatedPlace   :oldProvince  

PopulatedPlace  --> City   :capital  

Organisation  --> Person   :chaplain  

Person  --> Person   :copilote  

Athlete  --> Person   :trainer  

Actor  --> Award   :laurenceOlivierAward  

Person  --> SpatialThing   :restingPlacePosition  

Work  --> Place   :releaseLocation  

Person  --> Work   :created  

PopulatedPlace  --> Legislature   :legislature  

PopulatedPlace  --> Person   :leaderName  

Athlete  --> SportsTeam   :club  

Artist  --> Award   :emmyAward  

Scientist  --> Person   :doctoralAdvisor  

PopulatedPlace  --> PopulatedPlace   :lieutenancyArea  

Olympics  --> Person   :olympicOathSwornByJudge  

LegalCase  --> Person   :attorneyGeneral  

Olympics  --> Person   :torchBearer  

Person  --> Person   :usurper  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductNominalPerCapita  

Place  --> Place   :eastPlace  

River  --> PopulatedPlace   :mouthState  

Place  --> PopulatedPlace   :biggestCity  

Newspaper  --> Person   :managingEditor  

EducationalInstitution  --> Person   :actingHeadteacher  

PopulatedPlace  --> Language   :regionalLanguage  

Place  --> PopulatedPlace   :regency  

Saint  --> Person   :canonizedBy  

Person  --> Person   :sibling  

PopulatedPlace  --> PopulatedPlace   :principalArea  

Athlete  --> SportsTeam   :stateOfOriginTeam  

Person  --> Person   :opponent  

Canal  --> Person   :principalEngineer  

Settlement  --> PopulatedPlace   :federalState  

Place  --> Mountain   :lowestMountain  

Athlete  --> SportsTeam   :youthClub  

Man  --> Person   :uncle  

Artist  --> Award   :academyAward  

Family  --> Person   :headOfFamily  

Person  --> Film   :movie  

Place  --> Place   :land  

Band  --> Person   :formerBandMember  

Saint  --> Person   :beatifiedBy  

Person  --> Person   :child  

Artist  --> Award   :filmFareAward  

Musical  --> Person   :musicBy  

RouteOfTransportation  --> Place   :routeEndLocation  

WrittenWork  --> Person   :illustrator  

Comedian  --> Award   :britishComedyAwards  

Animal  --> Place   :birthPlace  

PopulatedPlace  --> PopulatedPlace   :sheading  

Place  --> Place   :southWestPlace  

Animal  --> Place   :deathPlace  

Person  --> Project   :project  

Album  --> Person   :compiler  

Department  --> PopulatedPlace   :subprefecture  

TelevisionShow  --> Person   :showJudge  

Place  --> PopulatedPlace   :lowestPlace  

Person  --> EthnicGroup   :ethnicity  

Actor  --> Award   :screenActorsGuildAward  

Island  --> PopulatedPlace   :lowestRegion  

Man  --> Person   :brother  

Settlement  --> PopulatedPlace   :jointCommunity  

Work  --> Person   :coverArtist  

Person  --> Person   :colleague  

Athlete  --> SportsTeam   :debutTeam  

School  --> Person   :headteacher  

PopulatedPlace  --> PopulatedPlace   :neighboringMunicipality  

Place  --> SpatialThing   :lowestPosition  

Artist  --> Award   :tonyAward  

Person  --> EducationalInstitution   :college  

Island  --> PopulatedPlace   :managementRegion  

Place  --> Place   :subregion  

PopulatedPlace  --> Agglomeration   :agglomeration  

Place  --> Place   :supply  

Settlement  --> Place   :highestPoint  

AdministrativeRegion  --> Person   :landeshauptmann  

Settlement  --> Place   :settlementAttached  

Family  --> Person   :lastFamilyMember  

SportsEvent  --> Person   :bronzeMedalist  

PopulatedPlace  --> Person   :viceLeader  

Place  --> Province   :provinceLink  

University  --> Person   :officerInCharge  

Person  --> Organisation   :federation  

Person  --> SportsEvent   :competitionTitle  

Person  --> Place   :educationPlace  

Person  --> MilitaryService   :militaryService  

Artist  --> Award   :gaudiAward  

Magazine  --> Person   :previousEditor  

Place  --> Province   :province  

Film  --> Person   :director  

Place  --> Area   :wholeArea  

Sport  --> Person   :footedness  

Actor  --> Award   :goldenCalfAward  

Person  --> Place   :livingPlace  

Person  --> Sport   :sportDiscipline  

Place  --> Place   :locatedInArea  

MilitaryUnit  --> Person   :secondCommander  

Place  --> RouteStop   :isRouteStop  

Artwork  --> Person   :painter  

TelevisionEpisode  --> Person   :guest  

Person  --> Place   :residence  

AdministrativeRegion  --> Place   :administrativeCenter  

Organisation  --> PopulatedPlace   :headquarter  

Organisation  --> Person   :chairperson  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueWinner  

Race  --> Person   :firstWinner  

Place  --> Place   :hasInsidePlace  

PopulatedPlace  --> Area   :agglomerationArea  

Person  --> EducationalInstitution   :almaMater  

Woman  --> Person   :daughter  

Language  --> PopulatedPlace   :spokenIn  

Organisation  --> Place   :regionServed  

Actor  --> Award   :nationalFilmAward  

Person  --> SKOSConcept   :usopenWins  

PopulatedPlace  --> PopulatedPlace   :largestSettlement  

Scientist  --> Person   :academicAdvisor  

Woman  --> Person   :sister  

Settlement  --> PopulatedPlace   :geolocDepartment  

River  --> PopulatedPlace   :sourceConfluenceState  

Actor  --> Award   :geminiAward  

Broadcaster  --> PopulatedPlace   :broadcastArea  

Film  --> Person   :editing  

Person  --> Person   :friend  

LegalCase  --> Person   :solicitorGeneral  

Athlete  --> SportsTeam   :oldTeamCoached  

SportsTeam  --> Person   :generalManager  

Place  --> Place   :endPoint  

SoccerLeagueSeason  --> SportsTeam   :soccerLeagueRelegated  

Organisation  --> Person   :ceo  

Person  --> CareerStation   :careerStation  

Organisation  --> Person   :superintendent  

Film  --> Person   :setDesigner  

PopulatedPlace  --> PopulatedPlace   :oldDistrict  

Person  --> PersonFunction   :otherOccupation  

Artist  --> Award   :afiAward  

PopulatedPlace  --> Demographics   :previousDemographics  

Settlement  --> Place   :wilaya  

FigureSkater  --> Person   :currentPartner  

EducationalInstitution  --> Person   :rector  

MilitaryUnit  --> PopulatedPlace   :garrison  

Work  --> Person   :translator  

SoccerClub  --> Place   :ground  

Place  --> PersonFunction   :politicalLeader  

Person  --> Contest   :contest  

Person  --> Organisation   :employer  

Person  --> Person   :dubber  

Man  --> Person   :father  

TermOfOffice  --> Person   :presidentGeneralCouncil  

Place  --> Place   :mainIsland  

Athlete,_CareerStation  --> SportsTeam   :proTeam  

PoliticalParty  --> Person   :spokesperson  

PopulatedPlace  --> PoliticalParty   :viceLeaderParty  

Actor  --> Award   :iftaAward  

Mountain  --> Person   :firstAscentPerson  

GrandPrix  --> Person   :thirdDriver  

Place  --> Altitude   :lowestAltitude  

TelevisionShow  --> Person   :coExecutiveProducer  

Person  --> Country   :stateOfOrigin  

EducationalInstitution  --> Person   :dean  

Place  --> Species   :flower  

Place  --> Altitude   :altitude  

TelevisionShow  --> Person   :presenter  

MilitaryUnit  --> Person   :notableCommander  

Person  --> Person   :parent  

Island  --> PopulatedPlace   :governmentRegion  

Settlement  --> PopulatedPlace   :administrativeDistrict  

Family  --> Person   :primogenitor  

PopulatedPlace  --> Saint   :saint  

Person  --> SportsLeague   :leagueManager  

Place  --> Place   :nextEntity  

Place  --> PopulatedPlace   :nearestCity  

SkiResort  --> Place   :massif  

Place  --> Place   :westPlace  

Athlete  --> SportsTeam   :coachClub  

Band  --> Person   :bandMember  

SportsTeam  --> Person   :currentMember  

Scientist  --> Person   :notableStudent  

Settlement  --> PopulatedPlace   :administrativeCollectivity  

Person  --> SKOSConcept   :endReign  

PopulatedPlace  --> GrossDomesticProductPerCapita   :grossDomesticProductPurchasingPowerParityPerCapita  

Politician  --> Person   :prefect  

```