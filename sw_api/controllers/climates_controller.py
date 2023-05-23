from sw_api.models.climate import Climate


class ClimatesController:

    def get_or_create_climates_by_names(
        self,
        climate_names: list[str],
    ) -> list[Climate]:
        climates: list[Climate] = []
        for climate_name in climate_names:
            climate, _ = Climate.objects.get_or_create(name=climate_name)
            climate.save()
            climates.append(climate)
        return climates
