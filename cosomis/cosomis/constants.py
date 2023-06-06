from extended_choices import Choices


OBSTACLES_FOCUS_GROUP = [
    "Obstacles of the farmers and breeders group", "Barriers of the women's group",
    "Barriers for Youth", "Barriers for ethnic minority groups"
]
GOALS_FOCUS_GROUP = [
    "Vision for the focus group of Farmers and breeders", "Vision for the women's focus group",
    "Vision for the youth focus group", "Vision for the focus group of ethnic minority groups"
]

ADMINISTRATIVE_LEVEL_TYPE = Choices(
    ("DÉPARTEMENT", "département", "Département"),
    ("COMMUNE", "commune", "Commune"),
    ("ARRONDISSEMENT", "arrondissement", "Arrondissement"),
    ("VILLAGE", "village", "Village"),
)


