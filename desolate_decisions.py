decisions = {

    #Starting statement
    "decision1" : """You have arrived to a desolate wasteland. 
You must find ways to survive in this land of nothing. 
Each time you arrive to a new destination you must find a charging port.
Time is of the essance.... 
The remote will point you in the right direction, but once it dies you will be on your own.
Find the charging port before the battery dies and you could still make it out of here with your life.
""",
    
    #Goes to decision3 & decision6
    "decision2" : """You can see mountains off in the distance. You are currently standing with sand all around you.
There is a Juniper Berry Bush 50 meters away. You see a tipped over empty fishing boat hull a few meters away from the tree.
You found some rope when you picked up the boat. You decide to hold on to it just in case you need it later.
The remote is telling you the charging port will take 2 days of walking to get to. You have a quarter charge worth of battery left.
Depending on how often the remote is used 1/4 of charge will keep the remote on for two days.

Do you want to make camp for the night? or Continue walking to the charging port?""",

    #Goes to decision4 & decision5
    "decision3" : """You have decided to make camp. 
You pull the boat hull over to the tree to make a shelter for the night.
You lean the boat against the tree to help provide a wind break and shelter from any potential rain.

Do you make a fire for the night?, Do you enjoy seeing how bright all the stars are?""",

    #Goes to decision7
    "decision4" : """You made a fire. You fall asleep with the fire still going. 
A few embers blew up into the dried up juniper berry tree and lit the whole tree on fire. 
You wake up and have to get out quickly. While springing out of your makeshift bed, 
you almost forgot the remote in the shelter. When you turn back for the remote the wind blows the fire directly towards you.
You are able to get the remote, but not without injury. You burn your arm right arm and right hand.""",

    #Goes to decision9
    "decision5" : """You are staring at the stars for the night. 
You begin to think about what you need to do to survive. 
You think you will be able to figure it out long enough to charge your remote and
hopefully make it to another place that it will be easier to survive in.
                """,

    #Goes to decision15 & decision16
    "decision6" : """You have decided to continue walking through the night. 
The remote GPS is pointing you towards the mountain. You begin making the dangerous and trecherous walk to continue your travels. 
You are grateful there is a full moon tonight and you are able to walk in the brightly lit starry night sky. 
Since you had to light the remote up so many times you notice the battery is draining faster than you expected.

Do you go out looking for supplies? or Do you continue on your journey of following the map to find a charging port?
                """,

    #Goes to decision8 & player_dies()
    "decision7" : """You are waiting until the sun comes up to see how badly you are injured.
When the sun rises you realize your arm has been seriously burned in the fire.
You are on the lookout for water and plants that could help soothe your burn.
You continue following the map on your remote while also checking revines and gullys for water.
You are now about 1 days walk away from the charging port.

Do you walk through the night to the charging port? or Do you stop and make camp for one more night? 
                 """,

    #Goes to next_era() & decision17
    "decision8" : """You continue walking through the night. Luckily it is a full moon and clear skies.
It has made it much easier to see where you are going. 
You find an aloe vera plant growing and rub it all over your burns helping to soothe your skin.
A small stream of water was close to the aloe vera plant. 
You collect some water, but wait to drink any of it since it needs to be purified.
You are feeling much better now. You are mostly tired and ready to drink some water.

Do you continue pushing to the charging station? 
                        or 
Do you stop for a small break to build a fire and purify your water?
                        """,

        #Goes to decision10 & decision11
        "decision9" : """You need to find water and make it to the charging station. 
It is incredibly hot in the middle of the day. There is not much left in this barren wasteland of sand,
a few small shrubs, and big rocky mountains. Your first priority is to make it to the charging station. 
You believe that you might be able to make it without water, just long enough to get to the charging port,
as long as you play it smart.
         
Do you begin only travelling at night? 
                or  
Do you move slowly, take more breaks, 
and just keep pushing to get to the charging port before the remote dies?
                        """,

        #Goes to decision12
        "decision10" : """You decide to only travel at night. 
Once it is time for the sun to rise you will find somewhere to escape the sun for most of the day.
While resting in the shade you find some shiny metal tucked under a rock. 
You find a knife with the initials B.N.
You think to yourself there is no way there is anyone else left alive in this desolate land. 
You know that there may come a time when you need this knife, but are concerned as you do not want to take what is not yours.
                        """,

        #player_dies()
        "decision11" : """You realize very quickly that you are becoming far to dehydrated.
There are to few places to escape the sun when trying to travel mid-day. 
You decide to rest under a small shrub that provides very little shade but, 
it helps break up the sun to provide some relief. You fall asleep from being to hot.
You wake up unsure of how long you have been out.
                        """,

        #Goes to decision13 & decision14
        "decision12" : """Do you keep the knife and hope you don't run into anyone else while your out here?
                                        or
Do you keep the knife and come up with a plan for in case you run into someone?    
                            """,

        #next_era()
        "decision13" : """You kept the knife. You decide this evening you will move quicker than what you have been.
You want to make sure you can make it to the charging port without any distruptions and make it out of here alive.

As soon as the sun was low enough in the sky for it to begin cooling off, you begin following the map to the charging port.
You ran like you have never run before. You are on a mission to get out of here.
                            """,

        #player_dies()
        "decision14" : """You kept the knife and now are contemplating every life decision that got you here. 
You begin to overthink everything. You are worried you won't make it to the charging port in time. 

Your theory was correct. You overthink everything. 
Once it is cool enough to start moving agian, you stay in your head thinking about all the what if scenarios and pay no attention to where you are at.
You fall into a gully carved out by torrential down pours of rain. When you fall into the gully you break your leg.
                            """,

        #Goes to decision18
        "decision15" : """You went out looking for supplies. You find some broken pottery and fishing line. 
You hold onto it for now just in case to use it later.
You get lost and end up an extra day worth of travel away from the charging port. 
                        """,

        #next_era()
        "decision16" : """You continued your journey to the charging port. 
You make it just in time before the battery dies and you would have been stuck in this desolate wasteland.
You are giddy with excitement!
                        """,

        #Goes to player_dies()
        "decision17" : """The plant you thought was aloe vera turned out to be Aloe ruspoliana.
A poisonous plant that looks similar to Aloe vera. 
You start to become extremely ill while preparing a fire and waiting for your water to boil. 
You pass out. When you wake up...
                        """,

        #player_dies()
        "decision18" : """You get lost and end up an extra day worth of travel away from the charging port.
You try to use what ever you have in your inventory to survive and continue pushing to the charging port."""
}
