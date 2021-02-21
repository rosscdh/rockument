from pathlib import Path
from django.test import TestCase
from rockument.apps.sponge.services import CommonSegmentService


class BasePayloadRootPathSegment(TestCase):
    fixture = """
    public/index.html
    """

    def setUp(self):
        self.fixture = [Path(line.strip()) for line in self.fixture.strip().split("\n")]
        self.service = CommonSegmentService(self.fixture)



class ExpectedPayloadRootPathSegmentTestCase(BasePayloadRootPathSegment):
    fixture = """
    public/index.html
    public/static/script.js
    public/static/style.css
    public/about/index.html
    public/some/other/path.html
    """
    
    def test_can_find_common_base(self):
        assert self.service.process() == 'public/', f"{self.service.process()} != public/"


class BadPayloadRootPathSegmentTestCase(BasePayloadRootPathSegment):
    fixture = """
    index.html
    static/script.js
    static/style.css
    about/index.html
    some/other/path.html
    """
    
    def test_can_find_common_base(self):
        assert self.service.process() == '', f"{self.service.process()} != ''"


class OtherPayloadRootPathSegmentTestCase(BasePayloadRootPathSegment):
    fixture = """
    some/other/site/index.html
    some/other/site/static/script.js
    some/other/site/static/style.css
    some/other/site/about/index.html
    some/other/site/some/other/path.html
    """
    
    def test_can_find_common_base(self):
        assert self.service.process() == 'site/', f"{self.service.process()} != 'site/'"