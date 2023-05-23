from sw_api.models.planet import Planet
from sw_api.controllers.climates_controller import ClimatesController
from sw_api.controllers.terrains_controller import TerrainsController


class PlanetsController:

    def get_all_planets(self) -> list[Planet]:
        planets = Planet.objects.all()
        return planets

    def get_planet_by_id(self, planet_id: int) -> Planet:
        planet = Planet.objects.get(pk=planet_id)
        return planet

    def create_planet(self, planet_data: dict) -> Planet:
        planet_name = planet_data.get('name')
        planet_population = planet_data.get('population')
        planet, _ = Planet.objects.get_or_create(
            name=planet_name,
            defaults={'population': planet_population},
        )
        terrain_names = planet_data.get('terrains', [])
        climate_names = planet_data.get('climates', [])
        self.set_planet_terrains_and_climates_by_names(
            planet, terrain_names, climate_names,
        )
        planet.save()
        return planet

    def delete_planet_by_id(self, planet_id: int) -> None:
        Planet.objects.filter(id=planet_id).delete()

    def update_planet(self, planet_id: int, planet_data: dict) -> Planet:
        planet = self.get_planet_by_id(planet_id)
        terrain_names = planet_data.pop('terrains', None)
        climate_names = planet_data.pop('climates', None)
        for key, value in planet_data.items():
            setattr(planet, key, value)
        self.set_planet_terrains_and_climates_by_names(
            planet, terrain_names, climate_names,
        )
        planet.save()
        return planet

    def set_planet_terrains_and_climates_by_names(
        self,
        planet: Planet,
        terrain_names: list[str] | None,
        climate_names: list[str] | None,
    ) -> Planet:
        if terrain_names is not None:
            terrains = TerrainsController().get_or_create_terrains_by_names(terrain_names)
            planet.terrains.set(terrains)
        if climate_names is not None:
            climates = ClimatesController().get_or_create_climates_by_names(climate_names)
            planet.climates.set(climates)
        return planet
