from typing import cast

from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import Loader
from panda3d.core import NodePath, Texture


class SpaceJam(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Tell VS Code/Pylance that camera is a NodePath.
        camera = cast(NodePath, self.camera)

        # Turn off Panda3D's default mouse camera controls.
        self.disableMouse()

        # Camera position.
        camera.setPos(0, -60, 10)
        camera.lookAt(0, 70, 0)

        # Press Escape to close the program.
        self.accept("escape", self.userExit)

        # Set up everything in the scene.
        self.SetupScene()


    def SetupScene(self):

        # Tell VS Code/Pylance the correct Panda3D types.
        loader = cast(Loader, self.loader)
        render = cast(NodePath, self.render)


        # ==================================================
        # UNIVERSE
        # ==================================================

        self.Universe: NodePath = cast(
            NodePath,
            loader.loadModel(
                "./Assets/Universe/Universe.x"
            )
        )

        self.Universe.reparentTo(render)

        self.Universe.setScale(15000)

        universeTexture: Texture = cast(
            Texture,
            loader.loadTexture(
                "./Assets/Universe/Universe.jpg"
            )
        )

        self.Universe.setTexture(universeTexture, 1)


        # ==================================================
        # PLANET 1 - MERCURY
        # ==================================================

        self.Planet1: NodePath = cast(
            NodePath,
            loader.loadModel(
                "./Assets/Planets/protoPlanet.x"
            )
        )

        self.Planet1.reparentTo(render)

        self.Planet1.setPos(-30, 70, 18)

        self.Planet1.setScale(7)

        mercuryTexture: Texture = cast(
            Texture,
            loader.loadTexture(
                "./Assets/Planets/mercury.jpg"
            )
        )

        self.Planet1.setTexture(mercuryTexture, 1)


        # ==================================================
        # PLANET 2 - VENUS
        # ==================================================

        self.Planet2: NodePath = cast(
            NodePath,
            loader.loadModel(
                "./Assets/Planets/protoPlanet.x"
            )
        )

        self.Planet2.reparentTo(render)

        self.Planet2.setPos(-18, 100, -14)

        self.Planet2.setScale(9)

        venusTexture: Texture = cast(
            Texture,
            loader.loadTexture(
                "./Assets/Planets/venus.jpg"
            )
        )

        self.Planet2.setTexture(venusTexture, 1)


        # ==================================================
        # PLANET 3 - EARTH
        # ==================================================

        self.Planet3: NodePath = cast(
            NodePath,
            loader.loadModel(
                "./Assets/Planets/protoPlanet.x"
            )
        )

        self.Planet3.reparentTo(render)

        self.Planet3.setPos(22, 75, 12)

        self.Planet3.setScale(9)

        earthTexture: Texture = cast(
            Texture,
            loader.loadTexture(
                "./Assets/Planets/earth.jpg"
            )
        )

        self.Planet3.setTexture(earthTexture, 1)


        # ==================================================
        # PLANET 4 - MARS
        # ==================================================

        self.Planet4: NodePath = cast(
            NodePath,
            loader.loadModel(
                "./Assets/Planets/protoPlanet.x"
            )
        )

        self.Planet4.reparentTo(render)

        self.Planet4.setPos(40, 105, -10)

        self.Planet4.setScale(8)

        marsTexture: Texture = cast(
            Texture,
            loader.loadTexture(
                "./Assets/Planets/mars.jpg"
            )
        )

        self.Planet4.setTexture(marsTexture, 1)


        # ==================================================
        # PLANET 5 - JUPITER
        # ==================================================

        self.Planet5: NodePath = cast(
            NodePath,
            loader.loadModel(
                "./Assets/Planets/protoPlanet.x"
            )
        )

        self.Planet5.reparentTo(render)

        self.Planet5.setPos(-34, 135, -8)

        self.Planet5.setScale(12)

        jupiterTexture: Texture = cast(
            Texture,
            loader.loadTexture(
                "./Assets/Planets/jupiter.jpg"
            )
        )

        self.Planet5.setTexture(jupiterTexture, 1)


        # ==================================================
        # PLANET 6 - SATURN
        # ==================================================

        self.Planet6: NodePath = cast(
            NodePath,
            loader.loadModel(
                "./Assets/Planets/protoPlanet.x"
            )
        )

        self.Planet6.reparentTo(render)

        self.Planet6.setPos(30, 145, 28)

        self.Planet6.setScale(11)

        saturnTexture: Texture = cast(
            Texture,
            loader.loadTexture(
                "./Assets/Planets/saturn.jpg"
            )
        )

        self.Planet6.setTexture(saturnTexture, 1)


        # ==================================================
        # SPACE STATION
        # ==================================================

        self.SpaceStation: NodePath = cast(
            NodePath,
            loader.loadModel(
                "./Assets/Space Station/spaceStation.x"
            )
        )

        self.SpaceStation.reparentTo(render)

        self.SpaceStation.setPos(0, 105, 22)

        self.SpaceStation.setScale(0.8)

        self.SpaceStation.setHpr(30, 10, 0)

        stationTexture: Texture = cast(
            Texture,
            loader.loadTexture(
                "./Assets/Space Station/SpaceStation1_Dif2.png"
            )
        )

        self.SpaceStation.clearTexture()
        self.SpaceStation.setTexture(stationTexture, 1)


        # ==================================================
        # PLAYER SPACESHIP
        # ==================================================

        # Use the .egg version because it is Panda3D's native
        self.Player: NodePath = cast(
            NodePath,
            loader.loadModel(
                "./Assets/Spaceships/Dumbledore.egg"
            )
        )

        self.Player.reparentTo(render)

        self.Player.setPos(0, 35, -4)

        self.Player.setScale(3)

        # Rotate the ship so it is easier to see.
        self.Player.setHpr(180, 0, 0)

        playerTexture: Texture = cast(
            Texture,
            loader.loadTexture(
                "./Assets/Spaceships/spacejet_C.png"
            )
        )

        # Remove the original texture information and
        # explicitly apply the correct ship texture.
        self.Player.clearTexture()
        self.Player.setTexture(playerTexture, 1)

# START PROGRAM
app = SpaceJam()
app.run()