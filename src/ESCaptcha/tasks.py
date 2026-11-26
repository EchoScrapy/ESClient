from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any


@dataclass
class BaseTask:
    type: str

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class ImageToTextTask(BaseTask):
    body: str

    def __init__(self, body: str):
        super().__init__('ImageToTextTask')
        self.body = body


@dataclass
class TikTok3DTask(BaseTask):
    challenge: Dict[str, Any]

    def __init__(self, challenge: Dict[str, Any]):
        super().__init__('TikTok3DTask')
        self.challenge = challenge


@dataclass
class ReCaptchaAndroidTaskProxyLess(BaseTask):
    appKey: str
    appPackageName: str
    appAction: str
    sdkVersion: Optional[str] = None
    sdkInt: Optional[str] = None
    proxy: Optional[str] = None

    def __init__(self, site_key: str, package_name: str, action: str,
                 sdk_version: Optional[str] = None, sdk_int: Optional[str] = None,
                 proxy: Optional[str] = None):
        super().__init__('ReCaptchaAndroidTaskProxyLess')
        self.appKey = site_key
        self.appPackageName = package_name
        self.appAction = action
        self.sdkVersion = sdk_version
        self.sdkInt = sdk_int
        self.proxy = proxy


@dataclass
class ReCaptchaV2TaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str

    def __init__(self, url: str, site_key: str):
        super().__init__('ReCaptchaV2TaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key


@dataclass
class ReCaptchaV3TaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str
    pageAction: Optional[str] = None
    engine: Optional[str] = None

    def __init__(self, url: str, site_key: str, action: Optional[str] = None,
                 engine: Optional[str] = None):
        super().__init__('ReCaptchaV3TaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key
        self.pageAction = action
        self.engine = engine


@dataclass
class HCaptchaTaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str

    def __init__(self, url: str, site_key: str):
        super().__init__('HCaptchaTaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key


@dataclass
class TurnstileTaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str
    action: Optional[str] = None
    cData: Optional[str] = None
    proxy: Optional[str] = None

    def __init__(self, url: str, site_key: str, action: Optional[str] = None,
                 cdata: Optional[str] = None, proxy: Optional[str] = None):
        super().__init__('TurnstileTaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key
        self.action = action
        self.cData = cdata
        self.proxy = proxy


@dataclass
class FunCaptchaTaskProxyLess(BaseTask):
    websiteURL: str
    websitePublicKey: str

    def __init__(self, url: str, pub_key: str):
        super().__init__('FunCaptchaTaskProxyLess')
        self.websiteURL = url
        self.websitePublicKey = pub_key


@dataclass
class GeeTestTaskProxyLess(BaseTask):
    websiteURL: str
    gt: str
    challenge: str

    def __init__(self, url: str, gt: str, challenge: str):
        super().__init__('GeeTestTaskProxyLess')
        self.websiteURL = url
        self.gt = gt
        self.challenge = challenge


@dataclass
class GeeTestV4TaskProxyLess(BaseTask):
    websiteURL: str
    captchaId: str
    riskType: str
    voice: Optional[bool] = None
    proxy: Optional[str] = None

    def __init__(self, url: str, captcha_id: str, risk_type: str = 'slide',
                 voice: Optional[bool] = None, proxy: Optional[str] = None):
        super().__init__('GeeTestV4TaskProxyLess')
        self.websiteURL = url
        self.captchaId = captcha_id
        self.riskType = risk_type
        self.voice = voice
        self.proxy = proxy


@dataclass
class AmazonWafTaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str
    proxy: Optional[str] = None

    def __init__(self, url: str, site_key: str, proxy: Optional[str] = None):
        super().__init__('AmazonWafTaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key
        self.proxy = proxy


@dataclass
class TencentSliderTaskProxyLess(BaseTask):
    websiteURL: str
    appid: str
    proxy: Optional[str] = None

    def __init__(self, url: str, appid: str, proxy: Optional[str] = None):
        super().__init__('TencentSliderTaskProxyLess')
        self.websiteURL = url
        self.appid = appid
        self.proxy = proxy


@dataclass
class FriendlyCaptchaV1TaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str
    endpoint: Optional[str] = None
    puzzleEndpoint: Optional[str] = None

    def __init__(self, url: str, site_key: str, endpoint: Optional[str] = None,
                 puzzle_endpoint: Optional[str] = None):
        super().__init__('FriendlyCaptchaV1TaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key
        self.endpoint = endpoint
        self.puzzleEndpoint = puzzle_endpoint


@dataclass
class FriendlyCaptchaTaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str
    endpoint: Optional[str] = None
    userAgent: Optional[str] = None
    language: Optional[str] = None
    sdkUrl: Optional[str] = None

    def __init__(self, url: str, site_key: str, endpoint: Optional[str] = None,
                 user_agent: Optional[str] = None, language: Optional[str] = None,
                 sdk_url: Optional[str] = None):
        super().__init__('FriendlyCaptchaTaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key
        self.endpoint = endpoint
        self.userAgent = user_agent
        self.language = language
        self.sdkUrl = sdk_url


@dataclass
class CloudflareJsdTaskProxyLess(BaseTask):
    websiteURL: str
    proxy: Optional[str] = None

    def __init__(self, url: str, proxy: Optional[str] = None):
        super().__init__('CloudflareJsdTaskProxyLess')
        self.websiteURL = url
        self.proxy = proxy


class TaskFactory:
    @staticmethod
    def serialize(task: BaseTask) -> dict:
        if not isinstance(task, BaseTask):
            raise TypeError('Task must inherit BaseTask')
        return task.to_dict()
