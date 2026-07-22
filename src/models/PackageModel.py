from pydantic import validator, Field
from typing import List, Union, Literal, Optional
from sdks.novavision.src.base.model import Package, Config, Inputs, Configs, Outputs, Output, Input, Image, Request, Response

class InputOne(Input):
    name: Literal["inputOne"] = "inputOne"
    value: Union[List[Image], Image]
    type: Literal["object"] = "object"
    field: Literal["input"] = "input"
    class Config:
        title = "Image Input 1"

class InputTwo(Input):
    name: Literal["inputTwo"] = "inputTwo"
    value: Union[List[Image], Image]
    type: Literal["object"] = "object"
    field: Literal["input"] = "input"
    class Config:
        title = "Image Input 2"

class InputThree(Input):
    name: Literal["inputThree"] = "inputThree"
    value: Union[List[Image], Image]
    type: Literal["object"] = "object"
    field: Literal["input"] = "input"
    class Config:
        title = "Image Input 3"

class OutputOne(Output):
    name: Literal["outputOne"] = "outputOne"
    value: Union[list, str]
    type: Literal["object"] = "object"
    field: Literal["output"] = "output"
    class Config:
        title = "Result Output 1"

class OutputTwo(Output):
    name: Literal["outputTwo"] = "outputTwo"
    value: Union[list, str]
    type: Literal["object"] = "object"
    field: Literal["output"] = "output"
    class Config:
        title = "Result Output 2"

class OutputThree(Output):
    name: Literal["outputThree"] = "outputThree"
    value: Union[list, str]
    type: Literal["object"] = "object"
    field: Literal["output"] = "output"
    class Config:
        title = "Result Output 3"

class OptionAIntegerField(Config):
    name: Literal["OptionAIntegerField"] = "OptionAIntegerField"
    value: int = Field(default=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "Integer Field for A"

class OptionAStringField(Config):
    name: Literal["OptionAStringField"] = "OptionAStringField"
    value: str = Field(default="demo A")
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "String Field for A"

class OptionA(Config):
    optionAIntegerField: OptionAIntegerField
    optionAStringField: OptionAStringField
    name: Literal["OptionA"] = "OptionA"
    value: Literal["OptionA"] = "OptionA"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "Method A"

class OptionBFloatField(Config):
    name: Literal["OptionBFloatField"] = "OptionBFloatField"
    value: float = Field(default=1.5)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "Float Field for B"

class OptionBStringField(Config):
    name: Literal["OptionBStringField"] = "OptionBStringField"
    value: str = Field(default="demo B")
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "String Field for B"

class OptionB(Config):
    optionBFloatField: OptionBFloatField
    optionBStringField: OptionBStringField
    name: Literal["OptionB"] = "OptionB"
    value: Literal["OptionB"] = "OptionB"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "Method B"

class DemoDependentDropdown(Config):
    name: Literal["demoDependentDropdown"] = "demoDependentDropdown"
    value: Union[OptionA, OptionB]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    class Config:
        title = "Select Method"
        schema_extra = {
            "shortDescription": "Method Selection"
        }

class ExecutorOneInputs(Inputs):
    inputOne: InputOne
    value: str = "Inputs"
    type: Literal["object"] = "object"
    field: Literal["input"] = "input"

class ExecutorOneConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown
    value: str = "Configs"
    type: Literal["object"] = "object"
    field: Literal["config"] = "config"

class ExecutorOneOutputs(Outputs):
    outputOne: OutputOne
    value: str = "Outputs"
    type: Literal["object"] = "object"
    field: Literal["output"] = "output"

class ExecutorOneRequest(Request):
    inputs: Optional[ExecutorOneInputs]
    configs: ExecutorOneConfigs
    class Config:
        schema_extra = {"target": "configs"}

class ExecutorOneResponse(Response):
    outputs: ExecutorOneOutputs

class ExecutorOne(Config):
    name: Literal["ExecutorOne"] = "ExecutorOne"
    value: Union[ExecutorOneRequest, ExecutorOneResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Executor One"
        schema_extra = {"target": {"value": 0}}

class ExecutorTwoInputs(Inputs):
    inputTwo: InputTwo
    inputThree: InputThree
    value: str = "Inputs"
    type: Literal["object"] = "object"
    field: Literal["input"] = "input"

class ExecutorTwoConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown
    value: str = "Configs"
    type: Literal["object"] = "object"
    field: Literal["config"] = "config"

class ExecutorTwoOutputs(Outputs):
    outputTwo: OutputTwo
    outputThree: OutputThree
    value: str = "Outputs"
    type: Literal["object"] = "object"
    field: Literal["output"] = "output"

class ExecutorTwoRequest(Request):
    inputs: Optional[ExecutorTwoInputs]
    configs: ExecutorTwoConfigs
    class Config:
        schema_extra = {"target": "configs"}

class ExecutorTwoResponse(Response):
    outputs: ExecutorTwoOutputs

class ExecutorTwo(Config):
    name: Literal["ExecutorTwo"] = "ExecutorTwo"
    value: Union[ExecutorTwoRequest, ExecutorTwoResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Executor Two"
        schema_extra = {"target": {"value": 0}}

class ConfigExecutor(Config):
    name: Literal["configExecutor"] = "configExecutor"
    value: Union[ExecutorOne, ExecutorTwo]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    class Config:
        title = "Executor Options"
        schema_extra = {"target": "value"}

class PackageConfigs(Configs):
    executor: ConfigExecutor
    value: str = "Configs"
    type: Literal["object"] = "object"
    field: Literal["config"] = "config"

class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["DemoPackage"] = "DemoPackage"
    uID = "1331112"
