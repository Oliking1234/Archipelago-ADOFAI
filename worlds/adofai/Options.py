from Options import Toggle, PerGameCommonOptions, Choice, Range, FreeText
from dataclasses import dataclass
class DeathLink(Toggle):
    display_name = "DeathLink"

class MainWorldsTuto(Toggle):
    display_name = "MainWorldsTuto"

class XtraWorlds(Toggle):
    display_name = "XtraWorlds"

class XtraWorldsTuto(Toggle):
    display_name = "XtraWorldsTuto"

class BWorld(Toggle):
    display_name = "BWorld"

class BWorldTuto(Toggle):
    display_name = "BWorldTuto"

class CrownWorlds(Toggle):
    display_name= "CronwWorlds"

class CrownWorldsTuto(Toggle):
    display_name= "CronwWorldsTuto"

class MuseDashWorlds(Toggle):
    display_name= "MuseDashWorlds"

class MuseDashWorldsTuto(Toggle):
    display_name= "MuseDashWorldsTuto"

class NeoCosmosWorlds(Toggle):
    display_name= "NeoCosmosWorlds"

class NeoCosmosWorldsTuto(Toggle):
    display_name= "NeoCosmosWorldsTuto"

class NeoCosmosWorldsEX(Toggle):
    display_name= "NeoCosmosWorldsEX"

class NeoCosmosWorldsEXTuto(Toggle):
    display_name= "NeoCosmosWorldsEXTuto"

class AprilFoolsWorlds(Toggle):
    display_name= "AprilFoolsWorlds"

class ARLibertasWorld(Toggle):
    display_name= "ARLibertasWorld"

class ARLibertasWorldTuto(Toggle):
    display_name= "ARLibertasWorldTuto"

class CosmicRadioWorlds(Toggle):
    display_name= "CosmicRadioWorlds"

class CosmicRadioWorldsTuto(Toggle):
    display_name= "CosmicRadioWorldsTuto"

class CosmicRadioWorldsEX(Toggle):
    display_name= "CosmicRadioWorldsEX"

class CompletionGoal(Choice):
    display_name = "CompletionGoal"
    option_allX = 0
    option_goalLevels = 1
    default = 0 

class PercentageGoalCompletion(Range):
    display_name = "PercentageGoalCompletion"
    range_start = 0
    range_end = 100
    default = 80

class GoalLevels(FreeText):
    display_name="GoalLevels"


@dataclass
class ADOFAIOptions(PerGameCommonOptions):
    death_link: DeathLink
    main_worlds_tuto: MainWorldsTuto
    xtra_worlds: XtraWorlds
    xtra_worlds_tuto: XtraWorldsTuto
    b_world: BWorld
    b_world_tuto: BWorldTuto
    crown_worlds: CrownWorlds
    crown_worlds_tuto: CrownWorldsTuto
    muse_dash_worlds: MuseDashWorlds
    muse_dash_worlds_tuto: MuseDashWorldsTuto
    neo_cosmos_worlds: NeoCosmosWorlds
    neo_cosmos_worlds_tuto: NeoCosmosWorldsTuto
    neo_cosmos_worlds_ex: NeoCosmosWorldsEX
    neo_cosmos_worlds_ex_tuto: NeoCosmosWorldsEXTuto
    april_fools_worlds: AprilFoolsWorlds
    ar_libertas_world: ARLibertasWorld
    ar_libertas_world_tuto: ARLibertasWorldTuto
    cosmic_radio_worlds: CosmicRadioWorlds
    cosmic_radio_worlds_tuto: CosmicRadioWorldsTuto
    cosmic_radio_worlds_ex: CosmicRadioWorldsEX
    percentage_goal_completion: PercentageGoalCompletion
    completion_goal: CompletionGoal
    goal_levels: GoalLevels
