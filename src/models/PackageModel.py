from pydantic import Field
from typing import List, Union, Literal, Optional
from sdks.novavision.src.base.model import Package, Config, Inputs, Configs, Outputs, Output, Input, Image, Request, Response

# ----------------- INPUTS -----------------
class InputImageOne(Input):
    name: Literal["inputImageOne"] = "inputImageOne"
    value: Union[List[Image], Image]
    type: str = "object"
    class Config:
        title = "Image Input 1"

class InputImageTwo(Input):
    name: Literal["inputImageTwo"] = "inputImageTwo"
    value: Union[List[Image], Image]
    type: str = "object"
    class Config:
        title = "Image Input 2"

class InputImageThree(Input):
    name: Literal["inputImageThree"] = "inputImageThree"
    value: Union[List[Image], Image]
    type: str = "object"
    class Config:
        title = "Image Input 3"

class ExecutorOneInputs(Inputs):
    inputImageOne: InputImageOne

class ExecutorTwoInputs(Inputs):
    inputImageTwo: InputImageTwo
    inputImageThree: InputImageThree

# ----------------- CONFIGS -----------------
class OptionAIntegerField(Config):
    name: Literal["OptionAIntegerField"] = "OptionAIntegerField"
    value: int = Field(default=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "Integer Field for A"

class OptionA(Config):
    name: Literal["OptionA"] = "OptionA"
    optionAIntegerField: OptionAIntegerField
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

class OptionB(Config):
    name: Literal["OptionB"] = "OptionB"
    optionBFloatField: OptionBFloatField
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
        json_schema_extra = {
            "shortDescription": "Method Selection"
        }

class ExecutorOneConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown

class ExecutorTwoConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown

# ----------------- OUTPUTS -----------------
class OutputImageOne(Output):
    name: Literal["outputImageOne"] = "outputImageOne"
    value: Union[List[Image], Image]
    type: str = "object"
    class Config:
        title = "Result Output 1"

class OutputImageTwo(Output):
    name: Literal["outputImageTwo"] = "outputImageTwo"
    value: Union[List[Image], Image]
    type: str = "object"
    class Config:
        title = "Result Output 2"

class OutputImageThree(Output):
    name: Literal["outputImageThree"] = "outputImageThree"
    value: Union[List[Image], Image]
    type: str = "object"
    class Config:
        title = "Result Output 3"

class ExecutorOneOutputs(Outputs):
    outputImageOne: OutputImageOne

class ExecutorTwoOutputs(Outputs):
    outputImageTwo: OutputImageTwo
    outputImageThree: OutputImageThree

# ----------------- REQUEST/RESPONSE -----------------
class ExecutorOneRequest(Request):
    inputs: Optional[ExecutorOneInputs] = None
    configs: ExecutorOneConfigs
    class Config:
        json_schema_extra = {"target": "configs"}

class ExecutorOneResponse(Response):
    outputs: ExecutorOneOutputs

class ExecutorTwoRequest(Request):
    inputs: Optional[ExecutorTwoInputs] = None
    configs: ExecutorTwoConfigs
    class Config:
        json_schema_extra = {"target": "configs"}

class ExecutorTwoResponse(Response):
    outputs: ExecutorTwoOutputs

# ----------------- EXECUTORS -----------------
class ExecutorOne(Config):
    name: Literal["ExecutorOne"] = "ExecutorOne"
    value: Union[ExecutorOneRequest, ExecutorOneResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Executor One"
        json_schema_extra = {"target": {"value": 0}}

class ExecutorTwo(Config):
    name: Literal["ExecutorTwo"] = "ExecutorTwo"
    value: Union[ExecutorTwoRequest, ExecutorTwoResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Executor Two"
        json_schema_extra = {"target": {"value": 0}}

class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[ExecutorOne, ExecutorTwo]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    class Config:
        title = "Task"
        json_schema_extra = {"target": "value"}

# ----------------- PACKAGE -----------------
class PackageConfigs(Configs):
    executor: ConfigExecutor

class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["DemoPackage"] = "DemoPackage"
    uID: str = "1331112"
