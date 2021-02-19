from django.core.management import BaseCommand

from motions.models import MotionCategory, MotionDifficulty, DebateFormat, MotionAgeRange, MotionType, \
    MotionTrainingFocus, MotionImproPrep, MotionWhereUsed, MotionLink


class Command(BaseCommand):
    help = 'Ineserts initial data.'

    def insert_categories(self):
        objs = [
            {'value': 'Art and Culture'},
            {'value': 'Business'},
            {'value': 'Criminal Justice System'},
            {'value': 'Development'},
            {'value': 'Economics'},
            {'value': 'Education'},
            {'value': 'Environment'},
            {'value': 'Family'},
            {'value': 'Feminism'},
            {'value': 'Freedoms'},
            {'value': 'International Relations'},
            {'value': 'LGBT+'},
            {'value': 'Media'},
            {'value': 'Medical Ethics'},
            {'value': 'Minority Communities'},
            {'value': 'Morality'},
            {'value': 'Politics'},
            {'value': 'Religion'},
            {'value': 'Science and Technology'},
            {'value': 'Geopolitical'},
            {'value': 'Social Policy'},
            {'value': 'Social Movements'},
            {'value': 'Sports'},
            {'value': 'Terrorism'},
            {'value': 'The Human Experience'}
        ]

        created_categories = list(
            MotionCategory.objects.filter(value__in=map(lambda x: x['value'], objs)).values_list('value', flat=True)
        )

        categories = []
        inserts = 0
        for obj in list(filter(lambda x: x['value'] not in created_categories, objs)):
            c = MotionCategory(value=obj['value'])
            categories.append(c)
            inserts += 1

        MotionCategory.objects.bulk_create(categories)

        if inserts:
            self.stdout.write(self.style.SUCCESS('%d MotionCategories have been successfully created' % inserts))
        else:
            self.stdout.write(self.style.WARNING('0 MotionCategories have been created'))

    def insert_difficulties(self):
        objs = [
            {'value': 'Begginer'},
            {'value': 'Medium'},
            {'value': 'Advanced'}
        ]

        created_difficulties = list(
            MotionDifficulty.objects.filter(value__in=map(lambda x: x['value'], objs)).values_list('value', flat=True)
        )

        difficulties = []
        inserts = 0
        for obj in list(filter(lambda x: x['value'] not in created_difficulties, objs)):
            d = MotionDifficulty(value=obj['value'])
            difficulties.append(d)
            inserts += 1

        MotionDifficulty.objects.bulk_create(difficulties)

        if inserts:
            self.stdout.write(self.style.SUCCESS('%d MotionDifficulties have been successfully created' % inserts))
        else:
            self.stdout.write(self.style.WARNING('0 MotionDifficulties have been created'))

    def insert_debate_formats(self):
        objs = [
            {'value': 'WS'},
            {'value': 'BP'},
            {'value': 'KP'}
        ]

        created_debate_formats = list(
            DebateFormat.objects.filter(value__in=map(lambda x: x['value'], objs)).values_list('value', flat=True)
        )

        debate_formats = []
        inserts = 0
        for obj in list(filter(lambda x: x['value'] not in created_debate_formats, objs)):
            df = DebateFormat(value=obj['value'])
            debate_formats.append(df)
            inserts += 1

        DebateFormat.objects.bulk_create(debate_formats)

        if inserts:
            self.stdout.write(self.style.SUCCESS('%d DebateFormats have been successfully created' % inserts))
        else:
            self.stdout.write(self.style.WARNING('0 DebateFormats have been created'))

    def insert_age_ranges(self):
        objs = [
            {'value': 'Elementary school'},
            {'value': 'Highscool'},
            {'value': 'University'}
        ]

        created_age_ranges = list(
            MotionAgeRange.objects.filter(value__in=map(lambda x: x['value'], objs)).values_list('value', flat=True)
        )

        age_ranges = []
        inserts = 0
        for obj in list(filter(lambda x: x['value'] not in created_age_ranges, objs)):
            ar = DebateFormat(value=obj['value'])
            age_ranges.append(ar)
            inserts += 1

        MotionAgeRange.objects.bulk_create(age_ranges)

        if inserts:
            self.stdout.write(self.style.SUCCESS('%d MotionAgeRanges have been successfully created' % inserts))
        else:
            self.stdout.write(self.style.WARNING('0 MotionAgeRanges have been created'))

    def insert_motion_types(self):
        objs = [
            {'value': 'Ban'},
            {'value': 'Prefference'},
            {'value': 'Governemnt'},
            {'value': 'action'},
            {'value': 'Support for X'}
        ]

        created_types = list(
            MotionType.objects.filter(value__in=map(lambda x: x['value'], objs)).values_list('value', flat=True)
        )

        types = []
        inserts = 0
        for obj in list(filter(lambda x: x['value'] not in created_types, objs)):
            t = MotionType(value=obj['value'])
            types.append(t)
            inserts += 1

        MotionType.objects.bulk_create(types)

        if inserts:
            self.stdout.write(self.style.SUCCESS('%d MotionTypes have been successfully created' % inserts))
        else:
            self.stdout.write(self.style.WARNING('0 MotionTypes have been created'))

    def insert_training_focuses(self):
        objs = [
            {'value': 'Principled arguments'},
            {'value': 'Comparative'},
            {'value': 'Model setting'},
            {'value': 'Impro prep'},
            {'value': 'Research focused'},
            {'value': 'Stakeholder analysis'},
        ]

        created_training_focuses = list(
            MotionTrainingFocus.objects.filter(value__in=map(lambda x: x['value'], objs)).values_list('value', flat=True)
        )

        training_focuses = []
        inserts = 0
        for obj in list(filter(lambda x: x['value'] not in created_training_focuses, objs)):
            tf = MotionTrainingFocus(value=obj['value'])
            training_focuses.append(tf)
            inserts += 1

        MotionTrainingFocus.objects.bulk_create(training_focuses)

        if inserts:
            self.stdout.write(self.style.SUCCESS('%d MotionTrainingFocuses have been successfully created' % inserts))
        else:
            self.stdout.write(self.style.WARNING('0 MotionTrainingFocuses have been created'))

    def insert_impro_prep(self):
        objs = [
            {'value': 'Impro'},
            {'value': 'Prep'}
        ]

        created_impro_prep = list(
            MotionImproPrep.objects.filter(value__in=map(lambda x: x['value'], objs)).values_list('value', flat=True)
        )

        impro_preps = []
        inserts = 0
        for obj in list(filter(lambda x: x['value'] not in created_impro_prep, objs)):
            tf = MotionImproPrep(value=obj['value'])
            impro_preps.append(tf)
            inserts += 1

        MotionImproPrep.objects.bulk_create(impro_preps)

        if inserts:
            self.stdout.write(self.style.SUCCESS('%d MotionImproPreps have been successfully created' % inserts))
        else:
            self.stdout.write(self.style.WARNING('0 MotionImproPreps have been created'))

    def insert_where_used(self):
        objs = []

        created_where_used = list(
            MotionWhereUsed.objects.filter(value__in=map(lambda x: x['value'], objs)).values_list('value', flat=True)
        )

        where_used = []
        inserts = 0
        for obj in list(filter(lambda x: x['value'] not in created_where_used, objs)):
            wu = MotionWhereUsed(value=obj['value'])
            where_used.append(wu)
            inserts += 1

        MotionWhereUsed.objects.bulk_create(where_used)

        if inserts:
            self.stdout.write(self.style.SUCCESS('%d MotionWhereUsed have been successfully created' % inserts))
        else:
            self.stdout.write(self.style.WARNING('0 MotionWhereUsed have been created'))

    def insert_links(self):
        objs = []

        created_links = list(
            MotionLink.objects.filter(value__in=map(lambda x: x['value'], objs)).values_list('value', flat=True)
        )

        links = []
        inserts = 0
        for obj in list(filter(lambda x: x['value'] not in created_links, objs)):
            ml = MotionLink(value=obj['value'])
            links.append(ml)
            inserts += 1

        MotionLink.objects.bulk_create(links)

        if inserts:
            self.stdout.write(self.style.SUCCESS('%d MotionLinks have been successfully created' % inserts))
        else:
            self.stdout.write(self.style.WARNING('0 MotionLinks have been created'))

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Inserting initial data'))
        self.insert_categories()
        self.insert_difficulties()
        self.insert_debate_formats()
        self.insert_age_ranges()
        self.insert_motion_types()
        self.insert_training_focuses()
        self.insert_impro_prep()
        self.insert_where_used()
        self.insert_links()
