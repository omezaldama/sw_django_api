from sw_api.models.terrain import Terrain


class TerrainsController:

    def get_or_create_terrains_by_names(
        self,
        terrain_names: list[str],
    ) -> list[Terrain]:
        terrains: list[Terrain] = []
        for terrain_name in terrain_names:
            terrain, _ = Terrain.objects.get_or_create(name=terrain_name)
            terrain.save()
            terrains.append(terrain)
        return terrains
