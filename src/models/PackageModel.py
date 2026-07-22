from pydantic import validator, Field
from typing import List, Union, Literal
from sdks.novavision.src.base.model import Package, Config, Inputs, Configs, Outputs, Output, Input, Image

class InputOne(Input):
    name: Literal["inputOne"] = "inputOne"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image Input 1"

class InputTwo(Input):
    name: Literal["inputTwo"] = "inputTwo"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image Input 2"

class InputThree(Input):
    name: Literal["inputThree"] = "inputThree"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image Input 3"

class OutputOne(Output):
    name: Literal["outputOne"] = "outputOne"
    value: Union[list, str]
    type: str = "list"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, list):
            return "list"
        elif isinstance(value, str):
            return "string"

    class Config:
        title = "Result Output 1"

class OutputTwo(Output):
    name: Literal["outputTwo"] = "outputTwo"
    value: Union[list, str]
    type: str = "list"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, list):
            return "list"
        elif isinstance(value, str):
            return "string"

    class Config:
        title = "Result Output 2"

class OutputThree(Output):
    name: Literal["outputThree"] = "outputThree"
    value: Union[list, str]
    type: str = "list"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, list):
            return "list"
        elif isinstance(value, str):
            return "string"

    class Config:
        title = "Result Output 3"

class OptionAIntegerField(Config):
    name: Literal["OptionAIntegerField"] = "OptionAIntegerField"
    value: int = Field(default=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Integer Field for A"

class OptionABooleanField(Config):
    name: Literal["OptionABooleanField"] = "OptionABooleanField"
    value: bool = Field(default=True)
    type: Literal["boolean"] = "boolean"
    field: Literal["checkbox"] = "checkbox"

    class Config:
        title = "Boolean Field for A"

class OptionA(Config):
    optionAIntegerField: OptionAIntegerField
    optionABooleanField: OptionABooleanField
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
    value: str = Field(default="demo")
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
        json_schema_extra = {
            "shortDescription": "Method Selection"
        }

class ExecutorOneInputs(Inputs):
    inputOne: InputOne

class ExecutorOneConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown

class ExecutorOneOutputs(Outputs):
    outputOne: OutputOne

class ExecutorOne(Config):
    inputs: ExecutorOneInputs
    configs: ExecutorOneConfigs
    outputs: ExecutorOneOutputs
    name: Literal["ExecutorOne"] = "ExecutorOne"
    value: Literal["ExecutorOne"] = "ExecutorOne"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Executor One"

class ExecutorTwoInputs(Inputs):
    inputTwo: InputTwo
    inputThree: InputThree

class ExecutorTwoConfigs(Configs):
    demoDependentDropdown: DemoDependentDropdown

class ExecutorTwoOutputs(Outputs):
    outputTwo: OutputTwo
    outputThree: OutputThree

class ExecutorTwo(Config):
    inputs: ExecutorTwoInputs
    configs: ExecutorTwoConfigs
    outputs: ExecutorTwoOutputs
    name: Literal["ExecutorTwo"] = "ExecutorTwo"
    value: Literal["ExecutorTwo"] = "ExecutorTwo"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Executor Two"

class ConfigExecutor(Config):
    name: Literal["configExecutor"] = "configExecutor"
    value: Union[ExecutorOne, ExecutorTwo]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Executor Options"

class PackageConfigs(Configs):
    executor: ConfigExecutor

class PackageModel(Package):
    configs: PackageConfigs
    name: Literal["DemoPackage"] = "DemoPackage"
