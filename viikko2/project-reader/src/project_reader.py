from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        sanak = tomli.loads(content)

        nimi = sanak.get("tool").get("poetry").get("name")

        kuvaus = sanak.get("tool").get("poetry").get("description")

        riippuvuudet = sanak.get("tool").get("poetry").get("dependencies").keys()

        devriippivuudet = sanak.get("tool").get("poetry").get("dev-dependencies").keys()

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, kuvaus, riippuvuudet, devriippivuudet)
