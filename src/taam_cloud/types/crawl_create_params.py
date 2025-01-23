# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CrawlCreateParams",
    "ScrapeOptions",
    "ScrapeOptionsAction",
    "ScrapeOptionsActionUnionMember0",
    "ScrapeOptionsActionUnionMember1",
    "ScrapeOptionsJsonOptions",
    "ScrapeOptionsLocation",
]


class CrawlCreateParams(TypedDict, total=False):
    url: Required[str]
    """The base URL to start crawling from"""

    allow_backward_links: Annotated[bool, PropertyInfo(alias="allowBackwardLinks")]
    """Allow navigation to previously linked pages"""

    allow_external_links: Annotated[bool, PropertyInfo(alias="allowExternalLinks")]
    """Allow following external links"""

    exclude_paths: Annotated[List[str], PropertyInfo(alias="excludePaths")]
    """URL patterns to exclude from crawl"""

    ignore_sitemap: Annotated[bool, PropertyInfo(alias="ignoreSitemap")]
    """Ignore website sitemap"""

    include_paths: Annotated[List[str], PropertyInfo(alias="includePaths")]
    """URL patterns to include in crawl"""

    limit: int
    """Maximum number of pages to crawl"""

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum depth to crawl"""

    scrape_options: Annotated[ScrapeOptions, PropertyInfo(alias="scrapeOptions")]

    webhook: str
    """Webhook URL for crawl events"""


class ScrapeOptionsActionUnionMember0(TypedDict, total=False):
    milliseconds: Required[int]

    type: Required[Literal["wait"]]

    selector: str


class ScrapeOptionsActionUnionMember1(TypedDict, total=False):
    type: Required[Literal["screenshot", "click", "write", "press", "scroll", "scrape", "execute"]]

    selector: str

    text: str


ScrapeOptionsAction: TypeAlias = Union[ScrapeOptionsActionUnionMember0, ScrapeOptionsActionUnionMember1]


class ScrapeOptionsJsonOptions(TypedDict, total=False):
    prompt: str

    schema: object

    system_prompt: Annotated[str, PropertyInfo(alias="systemPrompt")]


class ScrapeOptionsLocation(TypedDict, total=False):
    country: str

    languages: List[str]


class ScrapeOptions(TypedDict, total=False):
    actions: Iterable[ScrapeOptionsAction]

    exclude_tags: Annotated[List[str], PropertyInfo(alias="excludeTags")]

    formats: List[Literal["markdown", "html", "rawHtml", "links", "screenshot", "screenshot@fullPage", "json"]]

    headers: Dict[str, object]

    include_tags: Annotated[List[str], PropertyInfo(alias="includeTags")]

    json_options: Annotated[ScrapeOptionsJsonOptions, PropertyInfo(alias="jsonOptions")]

    location: ScrapeOptionsLocation

    mobile: bool

    only_main_content: Annotated[bool, PropertyInfo(alias="onlyMainContent")]

    remove_base64_images: Annotated[bool, PropertyInfo(alias="removeBase64Images")]

    skip_tls_verification: Annotated[bool, PropertyInfo(alias="skipTlsVerification")]

    timeout: int

    wait_for: Annotated[int, PropertyInfo(alias="waitFor")]
