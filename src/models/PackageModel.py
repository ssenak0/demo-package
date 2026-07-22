from pydantic import Field
from typing import List, Union, Literal, Optional
from sdks.novavision.src.base.model import Package, Executor, Param, Inputs, Configs, Outputs, Response, Request, Image

class ImageList(Param):
    value: List[Image]

# ----------------- INPUTS -----------------
class InputImageOne(Param):
    name: Literal["inputImageOne"] = "inputImageOne"
    value: ImageList
    type: Literal["imageList"] = "imageList"
    field: Literal["img"] = "img"
    class Config:
        title = "Image Input 1"

class InputImageTwo(Param):
    name: Literal["inputImageTwo"] = "inputImageTwo"
    value: ImageList
    type: Literal["imageList"] = "imageList"
    field: Literal["img"] = "img"
    class Config:
        title = "Image Input 2"

class InputImageThree(Param):
    name: Literal["inputImageThree"] = "inputImageThree"
    value: ImageList
    type: Literal["imageList"] = "imageList"
    field: Literal["img"] = "img"
    class Config:
        title = "Image Input 3"

class ExecutorOneInputs(Inputs):
    inputImageOne: InputImageOne
    value: str = "Inputs"
    type: Literal["object"] = "object"
    field: Literal["input"] = "input"

class ExecutorTwoInputs(Inputs):
    inputImageTwo: InputImageTwo
    inputImageThree: InputImageThree
    value: str = "Inputs"
    type: Literal["object"] = "object"
    field: Literal["input"] = "input"

# ----------------- CONFIGS -----------------
class OptionAIntegerField(Param):
    name: Literal["OptionAIntegerField"] = "OptionAIntegerField"
    value: int = Field(default=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "Integer Field for A"

class OptionA(Param):
    name: Literal["OptionA"] = "OptionA"
    optionAIntegerField: OptionAIntegerField
    value: Literal["OptionA"] = "OptionA"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "Method A"

class OptionBFloatField(Param):
    name: Literal["OptionBFloatField"] = "OptionBFloatField"
    value: float = Field(default=1.5)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "Float Field for B"

class OptionB(Param):
    name: Literal["OptionB"] = "OptionB"
    optionBFloatField: OptionBFloatField
    value: Literal["OptionB"] = "OptionB"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "Method B"

class DemoDependentDropdown(Param):
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
    value: str = "Configs"
    type: Literal["object"] = "object"
    field: Literal["config"] = "config"

class ExecutorTwoConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown
    value: str = "Configs"
    type: Literal["object"] = "object"
    field: Literal["config"] = "config"

# ----------------- OUTPUTS -----------------
class OutputImageOne(Param):
    name: Literal["outputImageOne"] = "outputImageOne"
    value: ImageList
    type: Literal["imageList"] = "imageList"
    field: Literal["img"] = "img"
    class Config:
        title = "Result Output 1"

class OutputImageTwo(Param):
    name: Literal["outputImageTwo"] = "outputImageTwo"
    value: ImageList
    type: Literal["imageList"] = "imageList"
    field: Literal["img"] = "img"
    class Config:
        title = "Result Output 2"

class OutputImageThree(Param):
    name: Literal["outputImageThree"] = "outputImageThree"
    value: ImageList
    type: Literal["imageList"] = "imageList"
    field: Literal["img"] = "img"
    class Config:
        title = "Result Output 3"

class ExecutorOneOutputs(Outputs):
    outputImageOne: OutputImageOne
    type: Literal["object"] = "object"
    field: Literal["output"] = "output"

class ExecutorTwoOutputs(Outputs):
    outputImageTwo: OutputImageTwo
    outputImageThree: OutputImageThree
    type: Literal["object"] = "object"
    field: Literal["output"] = "output"

# ----------------- REQUEST/RESPONSE -----------------
class ExecutorOneRequest(Request):
    inputs: Optional[ExecutorOneInputs]
    configs: ExecutorOneConfigs
    class Config:
        json_schema_extra = {"target": "configs"}

class ExecutorOneResponse(Response):
    outputs: ExecutorOneOutputs

class ExecutorTwoRequest(Request):
    inputs: Optional[ExecutorTwoInputs]
    configs: ExecutorTwoConfigs
    class Config:
        json_schema_extra = {"target": "configs"}

class ExecutorTwoResponse(Response):
    outputs: ExecutorTwoOutputs

# ----------------- EXECUTORS -----------------
class ExecutorOne(Executor):
    name: Literal["ExecutorOne"] = "ExecutorOne"
    value: Union[ExecutorOneRequest, ExecutorOneResponse]
    type: Literal["ExecutorOne"] = "ExecutorOne"
    field: Literal["executor"] = "executor"
    class Config:
        title = "Executor One"
        json_schema_extra = {"target": {"value": 0}}

class ExecutorTwo(Executor):
    name: Literal["ExecutorTwo"] = "ExecutorTwo"
    value: Union[ExecutorTwoRequest, ExecutorTwoResponse]
    type: Literal["ExecutorTwo"] = "ExecutorTwo"
    field: Literal["executor"] = "executor"
    class Config:
        title = "Executor Two"
        json_schema_extra = {"target": {"value": 0}}

class PackageExecutor(Executor):
    name: Literal["executor"] = "executor"
    value: Union[ExecutorOne, ExecutorTwo]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    class Config:
        title = "Task"
        json_schema_extra = {"target": "value"}

# ----------------- PACKAGE -----------------
class PackageModel(Package):
    type: Literal["component"] = "component"
    name: Literal["DemoPackage"] = "DemoPackage"
    uID: str = "1331112"
    executor: PackageExecutor
    field: Literal["executor"] = "executor"
    class Config:
        json_schema_extra = {"target": "executor"}
