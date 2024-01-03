# generated by datamodel-codegen:
#   filename:  RemoteRegistries.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class PyPi(BaseModel):
    class Config:
        extra = Extra.forbid

    enabled: bool
    packageName: str = Field(..., description="The name of the package on PyPi.")


class RemoteRegistries(BaseModel):
    class Config:
        extra = Extra.forbid

    pypi: Optional[PyPi] = None