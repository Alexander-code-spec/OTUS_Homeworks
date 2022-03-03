from random import choice, randint, sample

from django.core.management.base import BaseCommand

from furniture.models import Furniture, FurnitureSupplier, FurnitureMaterial


class Command(BaseCommand):

    def handle(self, *args, **options):
        suppliers_name = ['Askona', 'Melody', 'Faktura', 'Leon', 'Verona']
        suppliers_email = [
            'Askona@askona.local',
            'Melody@melody.local',
            'Faktura@faktura.local',
            'Leon@leon.local',
            'Verona@verona.local',
        ]
        suppliers_address = [
            'Moscow, Kutuzovskiy pr., 14',
            'Moscow, Kutuzovskiy pr., 15',
            'Moscow, Kutuzovskiy pr., 16',
            'Moscow, Kutuzovskiy pr., 17',
            'Moscow, Kutuzovskiy pr., 18',
        ]
        suppliers_phone_number = [
            88888888888,
            88888888887,
            88888888886,
            88888888885,
            88888888884,
        ]
        supplier_obj = []
        for supplier_name, supplier_email, supplier_address, supplier_phone_number in zip(
                suppliers_name,
                suppliers_email,
                suppliers_address,
                suppliers_phone_number,
        ):
            _obj, created = FurnitureSupplier.objects.get_or_create(
                name=supplier_name,
                email=supplier_email,
                address=supplier_address,
                phone_number=supplier_phone_number,
            )
            supplier_obj.append(_obj)

        furniture_type = ['Диван', 'Кровать', 'Стул', 'Стол', 'Комод', 'Тумба']
        furniture_type_obj = []
        for furniture_type in furniture_type:
            # animal_kinds_obj[animal_kind] = AnimalKind.objects.create(name=animal_kind)
            _obj = Furniture.objects.create(
                type=furniture_type,
                supplier=choice(supplier_obj),
            )
            furniture_type_obj.append(_obj)

        material_items = ['DSP', 'WOOD', 'PLASTIC', 'MDF', 'LDSP']
        material_obj = []
        for material in material_items:
            _obj, created = FurnitureMaterial.objects.get_or_create(material=material)
            material_obj.append(_obj)

        for material in material_obj:
            furnitures = sample(furniture_type_obj, k=randint(1, len(furniture_type_obj)))
            for furn in furnitures:
                material.furniture.add(furn)
            material.save()