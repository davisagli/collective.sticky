from plone.testing import z2
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting


class Layer(PloneSandboxLayer):
    
    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        import collective.sticky
        self.loadZCML(package=collective.sticky)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'collective.sticky:default')


FIXTURE = NetImpactLayer()
INTEGRATION_TESTING = IntegrationTesting(bases=(FIXTURE,), name='collective.sticky:Integration')
FUNCTIONAL_TESTING = FunctionalTesting(bases=(FIXTURE,), name='collective.sticky:Functional')
