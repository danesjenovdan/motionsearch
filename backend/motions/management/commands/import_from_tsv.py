from django.core.management import BaseCommand
from oauth2_provider.models import Application

from motions.models import (
    Motion,
    MotionCategory,
    MotionDifficulty,
    DebateFormat,
    MotionAgeRange,
    MotionType,
    MotionTrainingFocus,
    MotionImproPrep,
    MotionWhereUsed,
    MotionLink,
    MotionInfoText,
    MotionKeywords,
)
from users.models import User

import csv
import random


class Command(BaseCommand):
    help = "Ineserts initial data."

    def handle(self, *args, **options):
        with open("motions.tsv", "r") as infile:
            reader = csv.DictReader(infile, delimiter="\t")
            for row in reader:
                # create motion
                categories = MotionCategory.objects.filter(
                    id__in=[int(x) for x in row["category"].split(",")]
                )
                difficulties = MotionDifficulty.objects.filter(
                    id__in=[int(x) for x in row["difficulties"].split(",")]
                )
                debate_formats = DebateFormat.objects.filter(
                    id__in=[int(x) for x in row["debate_formats"].split(",")]
                )
                age_range = MotionAgeRange.objects.filter(
                    id__in=[int(x) for x in row["age_range"].split(",")]
                )
                type = MotionType.objects.filter(
                    id__in=[int(x) for x in row["type"].split(",")]
                )
                training_focus = MotionTrainingFocus.objects.filter(
                    id__in=[int(x) for x in row["training_focus"].split(",")]
                )
                impro_prep = MotionImproPrep.objects.filter(
                    id__in=[int(x) for x in row["impro_prep"].split(",")]
                )
                where_used = MotionWhereUsed.objects.filter(
                    id__in=[int(x) for x in row["where_used"].split(",")]
                )
                info_text = MotionInfoText.objects.filter(
                    id__in=[int(x) for x in row["info_text"].split(",")]
                )
                links = MotionLink.objects.filter(
                    id__in=[int(x) for x in row["links"].split(",")]
                )
                keywords = MotionKeywords.objects.filter(
                    id__in=[int(x) for x in row["keywords"].split(",")]
                )

                motion = Motion(
                    topic=row["topic"],
                    votes=row["votes"],
                    difficulties=random.choice(difficulties),
                    age_range=random.choice(age_range),
                    debate_formats=random.choice(debate_formats),
                    impro_prep=random.choice(impro_prep),
                    training_focus=random.choice(training_focus),
                    type=random.choice(type),
                )

                # save stuff
                motion.save()
                for category in categories:
                    motion.category.add(category)

                for usage in where_used:
                    motion.where_used.add(usage)

                for text in info_text:
                    motion.info_text.add(text)

                for link in links:
                    motion.links.add(link)

                for keyword in keywords:
                    motion.keywords.add(keyword)
