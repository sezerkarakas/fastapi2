from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Union


class HeaderParameter(BaseModel):
    key: str
    value: str


class TestData(BaseModel):
    testName: str
    httpCode: int
    httpRequest: str
    testDuration: str
    url: str
    virtualUsers: int
    bodyParameters: Union[Dict[str, Any], str, None] = None
    headerParameters: Optional[List[HeaderParameter]] = None
    userId: Optional[str] = None
