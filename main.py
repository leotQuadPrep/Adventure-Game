from Level import *
from DisplayRelocator import *
from DisplayBox import *
from InputBox import *
from Sword import Sword
from Creature import Creature
from Door import Door
from PersonalityTraits import PersonalityTraits
from Personality import Personality
from Weapon import Weapon
import GlobalContanor
IronSword = Sword("Iron Sword", 1, 5, 20, 1)
Rabbit1 = Creature("Spotted Rabbit", 1, "none", 5, 2)
Rabbit2 = Creature("White Rabbit", 1, "none", 5, 2)
Rabbit3 = Creature("Brown Rabbit", 1, "none", 5, 2)
Rabbit4 = Creature("Black Rabbit", 1, "none", 5, 2)
Cottage_Door_Outside1 = Door(False, False, "south", "", "cottage door", "door", False, False)
Cottage_Door_Inside1 = Door(False, False, "north", "", "door", "door", True, False)
Cottage_Window_East_Outside1 = Door(False, True, "west", "", "window", "window", False, True)
Cottage_Window_East_Inside1 = Door(False, True, "east", "", "window", "window", True, True)
Cottage_Window_West_Outside1 = Door(False, True, "east", "", "window", "window", False, True)
Cottage_Window_West_Inside1 = Door(False, True, "west", "", "window", "window", True, True)
Cottage_Trapdoor_Bottom1 = Door(False, False, "up", "", "trapdoor", "trapdoor", False, False)
Cottage_Trapdoor_Top1 = Door(False, False, "down", "", "trapdoor", "trapdoor", True, False)
forest_trail_fork_directions1 = ["", "northeast", "", "", "south", "", "", "northwest", "", ""]
forest_trail_fork_occupants1 = []
forest_trail_northeast_directions1 = ["", "northeast", "", "", "", "southwest", "", "", "", ""]
forest_trail_northeast_occupants1 = []
forest_trail_northwest_directions1 = ["", "", "", "southeast", "", "", "", "northwest", "", ""]
forest_trail_northwest_occupants1 = [Rabbit1, Rabbit4]
dead_forest_trail_end_directions1 = ["north", "", "", "", "", "", "", "", "up", ""]
dead_forest_trail_end_occupants1 = [Rabbit3]
forest_canyon_trail_end_directions1 = ["", "", "", "southeast", "", "", "", "northwest", "", ""]
forest_canyon_trail_end_occupants1 = []
south_of_cottage_directions1 = ["", "northeast", "east", "", "", "southwest", "west", "northwest", "", ""]
south_of_cottage_occupants1 = []
west_of_cottage_directions1 = ["north", "northeast", "east", "southeast", "south", "", "", "", "", ""]
west_of_cottage_occupants1 = [Rabbit2]
west_of_cottage_doors1 = [GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, Cottage_Window_West_Outside1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1,
                          GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1]
east_of_cottage_directions1 = ["north", "", "", "", "south", "southwest", "west", "northwest", "", ""]
east_of_cottage_occupants1 = []
east_of_cottage_doors1 = [GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1,
                          Cottage_Window_East_Outside1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1]
north_of_cottage_directions1 = ["", "", "east", "southeast", "south", "southwest", "west", "", "", ""]
north_of_cottage_occupants1 = []
north_of_cottage_doors1 = [GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, Cottage_Door_Outside1,
                           GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1]
inside_of_cottage_directions1 = ["north", "", "east", "", "", "", "west", "", "up", ""]
inside_of_cottage_occupants1 = [IronSword]
inside_of_cottage_doors1 = [Cottage_Door_Inside1, GlobalContanor.Compare_Door1, Cottage_Window_East_Inside1, GlobalContanor.Compare_Door1,
                            GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, Cottage_Window_West_Inside1, GlobalContanor.Compare_Door1,
                            Cottage_Trapdoor_Bottom1, GlobalContanor.Compare_Door1]
cottage_attic_directions1 = ["", "", "", "", "", "", "", "", "", "down"]
cottage_attic_occupants1 = []
cottage_attic_doors1 = [GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1,
                        GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, GlobalContanor.Compare_Door1, Cottage_Trapdoor_Top1]
Forest_Trail_Fork1 = Level("You are in a forest on a trail that forks", forest_trail_fork_directions1,
                           forest_trail_fork_occupants1, "", "", "", "", "", "", "", "", "", "", [])
Forest_Trail_Northeast1 = Level("You are in a forest on a trail", forest_trail_northeast_directions1,
                                forest_trail_northeast_occupants1, "", "", "", "", "", "", "", "", "", "", [])
Forest_Trail_Northwest1 = Level("You are in a forest on a trail", forest_trail_northwest_directions1,
                                forest_trail_northwest_occupants1, "", "", "", "", "", "", "", "", "", "", [])
Dead_Forest_Trail_End1 = Level("You are on a dead end trail on the border of a forest and a dead forest. The "
                               "trail leads back into the forest",
                               dead_forest_trail_end_directions1, dead_forest_trail_end_occupants1, "", "", "", "", "",
                               "", "", "", "", "", [])
Forest_Canyon_Trail_End1 = Level("You are on the edge of a canyon and a forest with a trail leading into the "
                                 "forest and a broken bridge across the canyon", forest_canyon_trail_end_directions1,
                                 forest_canyon_trail_end_occupants1, "", "", "", "", "", "", "", "", "", "", [])
South_Of_Cottage1 = Level("You are on the edge of a clearing in a forest. There is a cottage to the north of"
                          " you in the center of the clearing", south_of_cottage_directions1,
                          south_of_cottage_occupants1, "", "", "", "", "", "", "", "", "", "", [])
West_Of_Cottage1 = Level("You are in clearing in a forest. There is a cottage to the east of you in the center of the "
                         "clearing. There is a window on this side of the cottage", west_of_cottage_directions1,
                         west_of_cottage_occupants1, "", "", "", "", "", "", "", "", "", "", [], west_of_cottage_doors1, [[5,1,1,1]])
East_Of_Cottage1 = Level("You are in clearing in a forest. There is a cottage to the west of you in the center of the "
                         "clearing. There is a window on this side of the cottage", east_of_cottage_directions1,
                         east_of_cottage_occupants1, "", "", "", "", "", "", "", "", "", "", [], east_of_cottage_doors1)
North_Of_Cottage1 = Level("You are in clearing in a forest. There is a cottage to the south of you in the center of the"
                          " clearing. There is a door on this side of the cottage", north_of_cottage_directions1,
                          north_of_cottage_occupants1, "", "", "", "", "", "", "", "", "", "", [],
                          north_of_cottage_doors1)
Inside_Of_Cottage1 = Level("You are in a cottage with little furnishings, two windows let in some light",
                           inside_of_cottage_directions1, inside_of_cottage_occupants1, "", "", "", "", "", "", "", "",
                           "", "", [], inside_of_cottage_doors1)
Cottage_Attic1 = Level("You are in a small attic", cottage_attic_directions1, cottage_attic_occupants1, "", "", "", "",
                       "", "", "", "", "", "", [], cottage_attic_doors1)
Forest_Trail_Fork1.set_northeast(Forest_Trail_Northeast1)
Forest_Trail_Fork1.set_northwest(Forest_Trail_Northwest1)
Forest_Trail_Fork1.set_south(Dead_Forest_Trail_End1)
Forest_Trail_Northeast1.set_southwest(Forest_Trail_Fork1)
Forest_Trail_Northeast1.set_northeast(South_Of_Cottage1)
Forest_Trail_Northwest1.set_southeast(Forest_Trail_Fork1)
Forest_Trail_Northwest1.set_northwest(Forest_Canyon_Trail_End1)
Dead_Forest_Trail_End1.set_north(Forest_Trail_Fork1)
Forest_Canyon_Trail_End1.set_southeast(Forest_Trail_Northwest1)
South_Of_Cottage1.set_southwest(Forest_Trail_Northeast1)
South_Of_Cottage1.set_northwest(West_Of_Cottage1)
South_Of_Cottage1.set_west(West_Of_Cottage1)
South_Of_Cottage1.set_northeast(East_Of_Cottage1)
South_Of_Cottage1.set_east(East_Of_Cottage1)
West_Of_Cottage1.set_east(Inside_Of_Cottage1)
West_Of_Cottage1.set_southeast(South_Of_Cottage1)
West_Of_Cottage1.set_south(South_Of_Cottage1)
West_Of_Cottage1.set_northeast(North_Of_Cottage1)
West_Of_Cottage1.set_north(North_Of_Cottage1)
East_Of_Cottage1.set_west(Inside_Of_Cottage1)
East_Of_Cottage1.set_south(South_Of_Cottage1)
East_Of_Cottage1.set_southwest(South_Of_Cottage1)
East_Of_Cottage1.set_north(North_Of_Cottage1)
East_Of_Cottage1.set_northwest(North_Of_Cottage1)
North_Of_Cottage1.set_east(East_Of_Cottage1)
North_Of_Cottage1.set_southeast(East_Of_Cottage1)
North_Of_Cottage1.set_south(Inside_Of_Cottage1)
North_Of_Cottage1.set_southwest(West_Of_Cottage1)
North_Of_Cottage1.set_west(West_Of_Cottage1)
Inside_Of_Cottage1.set_north(North_Of_Cottage1)
Inside_Of_Cottage1.set_east(East_Of_Cottage1)
Inside_Of_Cottage1.set_west(West_Of_Cottage1)
Inside_Of_Cottage1.set_up(Cottage_Attic1)
Cottage_Attic1.set_down(Inside_Of_Cottage1)
Cottage_Window_West_Outside1.set_door_pair(Cottage_Window_West_Inside1)
Cottage_Window_West_Inside1.set_door_pair(Cottage_Window_West_Outside1)
Cottage_Window_East_Outside1.set_door_pair(Cottage_Window_East_Inside1)
Cottage_Window_East_Inside1.set_door_pair(Cottage_Window_East_Outside1)
Cottage_Door_Outside1.set_door_pair(Cottage_Door_Inside1)
Cottage_Door_Inside1.set_door_pair(Cottage_Door_Outside1)
Cottage_Trapdoor_Bottom1.set_door_pair(Cottage_Trapdoor_Top1)
Cottage_Trapdoor_Top1.set_door_pair(Cottage_Trapdoor_Bottom1)
Rabbit1.set_location(Forest_Trail_Northwest1)
Rabbit2.set_location(West_Of_Cottage1)
Rabbit3.set_location(Dead_Forest_Trail_End1)
Rabbit4.set_location(Forest_Trail_Northwest1)
Forest_Trail_Fork1.set_actions()
Forest_Trail_Northeast1.set_actions()
Forest_Trail_Northwest1.set_actions()
Dead_Forest_Trail_End1.set_actions()
Forest_Canyon_Trail_End1.set_actions()
South_Of_Cottage1.set_actions()
West_Of_Cottage1.set_actions()
East_Of_Cottage1.set_actions()
North_Of_Cottage1.set_actions()
Inside_Of_Cottage1.set_actions()
Cottage_Attic1.set_actions()

Hunger = PersonalityTraits(10, 5, 1, 5, 5)
Thirst = PersonalityTraits(10, 5, 1, 5, 6)
Social = PersonalityTraits(10, 5, 1, 5, 3)
Safety = PersonalityTraits(10, 5, 1, 5, 4)
Bored = PersonalityTraits(10, 5, 1, 5, 2)
emotions_traits = [Hunger, Thirst, Social, Safety, Bored]
Emotions = Personality(emotions_traits)
Emotions.exist()
Emotions.evaluate([[1, 1, 0, 1], [0, 2, 1, 1], [1, 2, 0, 1], [4, 7, 0, 1], [4, 1, 3, 1], [1, 1, 4, 1]])
print(Emotions.optimal_action)


def main():
    GlobalContanor.location = Forest_Trail_Fork1
    clock = pygame.time.Clock()
    timer = 0
    player_box = InputBox(20, 150, 200, 32, GlobalContanor.player_input)
    level_display_box = DisplayBox(20, 20, 400, 32, GlobalContanor.level_show_text, 100, 100, 100)
    action_display_box = DisplayBox(20, 70, 400, 32, GlobalContanor.action_show_text, 100, 100, 100)
    relocate_container = DisplayRelocator(level_display_box, action_display_box, player_box)
    pygame.display.set_caption("Text Based Adventure Game")
    running = True
    while running:
        GlobalContanor.location.visited()
        GlobalContanor.location_changed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            player_box.handle_event(event)
        player_box.update()
        level_display_box.update(GlobalContanor.level_show_text)
        action_display_box.update(GlobalContanor.action_show_text)
        relocate_container.relocate()
        GlobalContanor.screen.fill((0, 0, 0))
        player_box.draw(GlobalContanor.screen)
        level_display_box.draw(GlobalContanor.screen)
        action_display_box.draw(GlobalContanor.screen)
        pygame.display.flip()
        timer += 1
        if timer == 120:
            timer = 0
            GlobalContanor.gameTime += 1
            print(GlobalContanor.gameTime)
            print(GlobalContanor.location.animal_actions)
        if GlobalContanor.gameTime == 97:
            GlobalContanor.gameTime = 0
        clock.tick(60)


if __name__ == '__main__':
    main()
    pygame.quit()
